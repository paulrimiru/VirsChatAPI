from datetime import datetime

from flask import g
from flask_restful import reqparse, fields, marshal_with
from sqlalchemy.exc import IntegrityError


from app.users.mixins import SignupLoginMixin
from app.users.models import AppUser, PasswordReset

from app.utils.auth import auth_required, admin_required, generate_token
from app.utils.errors import EMAIL_IN_USE, CODE_NOT_VALID, BAD_CREDENTIALS

from app import db, bcrypt, app


user_fields = {
    'id': fields.Integer,
    'email': fields.String
}

@app.route('/api/v1/user')
class UserAPI(SignupLoginMixin):

    @auth_required
    @marshal_with(user_fields)
    def get(self):
        return g.current_user

    def post(self):
        args = self.req_parser.parse_args()

        user = AppUser(email=args['email'], password=args['password'])
        db.session.add(user)

        try:
            db.session.commit()
        except IntegrityError:
            return EMAIL_IN_USE

        return {
            'id': user.id,
            'token': generate_token(user)
        }, 201

@app.route('/api/v1/authenticate')
class AuthenticationAPI(SignupLoginMixin):

    def post(self):
        args = self.req_parser.parse_args()

        user = db.session.query(AppUser).filter(AppUser.email==args['email']).first()
        if user and bcrypt.check_password_hash(user.password, args['password']):

            return {
                'id': user.id,
                'token': generate_token(user)
            }

        return BAD_CREDENTIALS

@app.route('/api/v1/password-reset/request')
class PasswordResetRequestAPI():

    def post(self):
        req_parser = reqparse.RequestParser()
        req_parser.add_argument('email', type=str, required=True)
        args = req_parser.parse_args()

        user = db.session.query(AppUser).filter(AppUser.email==args['email']).first()
        if user:
            password_reset = PasswordReset(user=user)
            db.session.add(password_reset)
            db.session.commit()
            # TODO: Send the email using any preferred method

        return {}, 201

@app.route('/api/v1/password-reset/confirm')
class PasswordResetConfirmAPI():

    def post(self):
        req_parser = reqparse.RequestParser()
        req_parser.add_argument('code', type=str, required=True)
        req_parser.add_argument('password', type=str, required=True)
        args = req_parser.parse_args()

        password_reset = db.session.query(PasswordReset
                            ).filter(PasswordReset.code==args['code']
                            ).filter(PasswordReset.date>datetime.now()).first()

        if not password_reset:
            return CODE_NOT_VALID

        password_reset.user.set_password(args['password'])
        db.session.delete(password_reset)
        db.session.commit()

        return {}, 200


@app.route('/api/v1/admin')
class AdminOnlyAPI():

    @admin_required
    def get(self):
        return {}, 200
