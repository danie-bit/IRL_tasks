from flask_sqlalchemy import SQLAlchemy
import string
import random

db = SQLAlchemy()
class URLModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.short_code:
            self.short_code = self.generate_short_code()

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choices(characters, k=5))
            already_exists = URLModel.query.filter_by(short_code=code).first()
            if not already_exists:
                return code
