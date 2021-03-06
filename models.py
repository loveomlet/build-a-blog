from app import db
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(255))
    posted = db.Column(db.Boolean)

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.posted = False