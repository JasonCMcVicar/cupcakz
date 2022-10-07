"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):

    __tablename__ = "cupcakz"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.Text,
                     nullable=False)
    size = db.Column(db.Text,
                        nullable=False)
    rating = db.Column(db.Integer,
                        nullable=False)
    image = db.Column(db.Text,
                          nullable=False,
                          default='https://tinyurl.com/demo-cupcake')

    def __repr__(self):
        rep = f'<Cupcake: {self.flavor} {self.size} {self.rating} {self.image}, id={self.id} >'
        return rep

    def serialize(self):
        """Return object with id, flavor, size, rating, and image."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image,
            }