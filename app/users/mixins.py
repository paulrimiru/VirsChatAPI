from flask_restful import reqparse


class SignupMixin(object):

    req_parser = reqparse.RequestParser()
    req_parser.add_argument('username', type=str, required=True)
    req_parser.add_argument('usertype', type=str, required=True)
    req_parser.add_argument('email', type=str, required=True)
    req_parser.add_argument('password', type=str, required=True)

class SignInMixin(object):

    req_parser = reqparse.RequestParser()
    req_parser.add_argument('email', type=str, required=True)
    req_parser.add_argument('password', type=str, required=True)
    