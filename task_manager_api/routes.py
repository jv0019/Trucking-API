from flask import Blueprint, request, jsonify, abort
from models import Load
from schemas import load_schema, loads_schema
from database import db
from flask import render_template

load_bp = Blueprint('load_bp', __name__)

@load_bp.route('/load', methods=['POST'])
def add_load():
    data = request.get_json()
    if not data or not all(k in data for k in ('loadingPoint', 'unloadingPoint', 'productType', 'truckType', 'noOfTrucks', 'weight', 'shipperId', 'date')):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_load = Load(
        loading_point=data['loadingPoint'],
        unloading_point=data['unloadingPoint'],
        product_type=data['productType'],
        truck_type=data['truckType'],
        no_of_trucks=data['noOfTrucks'],
        weight=data['weight'],
        comment=data.get('comment', ''),
        shipper_id=data['shipperId'],
        date=data['date']
    )
    db.session.add(new_load)
    db.session.commit()
    return jsonify({"message": "Load details added successfully", "load": load_schema.dump(new_load)}), 201

@load_bp.route('/load', methods=['GET'])
def get_loads():
    shipper_id = request.args.get('shipperId')
    loads = Load.query.filter_by(shipper_id=shipper_id).all()
    result = loads_schema.dump(loads)  # Serialize the loads
    return jsonify(result), 200  # Use jsonify to return a JSON response

@load_bp.route('/load/<load_id>', methods=['GET'])
def get_load(load_id):
    load = Load.query.get_or_404(load_id)
    result = load_schema.dump(load)  # Serialize the single load
    return jsonify(result), 200  # Use jsonify to return a JSON response

@load_bp.route('/load/<load_id>', methods=['PUT'])
def update_load(load_id):
    load = Load.query.get_or_404(load_id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    load.loading_point = data.get('loadingPoint', load.loading_point)
    load.unloading_point = data.get('unloadingPoint', load.unloading_point)
    load.product_type = data.get('productType', load.product_type)
    load.truck_type = data.get('truckType', load.truck_type)
    load.no_of_trucks = data.get('noOfTrucks', load.no_of_trucks)
    load.weight = data.get('weight', load.weight)
    load.comment = data.get('comment', load.comment)
    load.date = data.get('date', load.date)

    db.session.commit()
    return load_schema.jsonify(load), 200

@load_bp.route('/load/<load_id>', methods=['DELETE'])
def delete_load(load_id):
    load = Load.query.get_or_404(load_id)
    db.session.delete(load)
    db.session.commit()
    return jsonify({"message": "Load deleted successfully"}), 204

