from datetime import datetime
from app import db


class FallEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    John = db.Column(db.String(120))
    Mandy = db.Column(db.String(120))
    Chris = db.Column(db.String(120))

    @property
    def serialize(self):
        return {
            'timestamp': self.timestamp,
            'John': self.John,
            'Mandy': self.Mandy,
            'Chris': self.Chris,
        }

    def __repr__(self):
        return '<timestamp {}, John {}, Mandy {}, Chris {}>'.format(self.timestamp, self.John, self.Mandy, self.Chris)