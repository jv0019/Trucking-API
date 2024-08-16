from marshmallow import Schema, fields

class LoadSchema(Schema):
    id = fields.Str(dump_only=True)
    loading_point = fields.Str(required=True)
    unloading_point = fields.Str(required=True)
    product_type = fields.Str(required=True)
    truck_type = fields.Str(required=True)
    no_of_trucks = fields.Int(required=True)
    weight = fields.Float(required=True)
    comment = fields.Str()
    shipper_id = fields.Str(required=True)
    date = fields.Str(required=True)

load_schema = LoadSchema()
loads_schema = LoadSchema(many=True)
