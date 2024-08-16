from datetime import datetime
from database import db
import uuid

class Load(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    loading_point = db.Column(db.String(80), nullable=False)
    unloading_point = db.Column(db.String(80), nullable=False)
    product_type = db.Column(db.String(80), nullable=False)
    truck_type = db.Column(db.String(80), nullable=False)
    no_of_trucks = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String(200))
    shipper_id = db.Column(db.String(36), nullable=False)
    date = db.Column(db.String, nullable=False)
