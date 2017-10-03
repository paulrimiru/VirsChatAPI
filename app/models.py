from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    usertype = db.Column(db.String(128))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    
    def __init__(self, username, usertype, email, password):
        """initialize with username."""
        self.username = username
        self.usertype = usertype
        self.email = email
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Users: {}>".format(self.username)
