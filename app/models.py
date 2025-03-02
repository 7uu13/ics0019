from config import db

class Kohvikud(db.Model):
    __tablename__ = 'sookla'
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    operator = db.Column(db.String(100), nullable=False)
    time_open = db.Column(db.String(100), nullable=False)
    time_close = db.Column(db.String(100), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "operator": self.operator,
            "time_open": self.time_open,
            "time_close": self.time_close,
        }
