from app import db

class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.String(500), index=True, unique=True)
    body = db.Column(db.String(5000), index=True, unique=True)
    tags = db.Column(db.String(300), index=True, unique=False)

    def as_dict(self):
        obj_d = {
            'title': self.title,
            'description': self.description,
            'body': self.body,
            'tags': self.tags,
        }
        return obj_d

    def __repr__(self):
        return '<Record %r>' % (self.title)

