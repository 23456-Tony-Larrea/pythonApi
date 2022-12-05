from flask import Blueprint, request, jsonify
from models.PersonsModel import PersonsModel

main = Blueprint('api_persons', __name__)

@main.route('/', methods=['GET'])
def get_persons():
    try:
        persons = PersonsModel.getPersons()
        return jsonify(persons)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/<int:id>', methods=['GET'])
def get_persons_id(id):
    try:
        person = PersonsModel.getPersonsId(id)
        return jsonify(person)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/', methods=['POST'])
def add_person():
    try:
        person = request.get_json()
        affected_rows = PersonsModel.add_person(person)
        return jsonify({'affected_rows': affected_rows})
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500 

@main.route('/<int:id>', methods=['PUT'])
def update_person(id):
    try:
        person = request.get_json()
        affected_rows = PersonsModel.update_person(person,id)
        return jsonify({'affected_rows': affected_rows})
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500       

@main.route('/<int:id>', methods=['DELETE'])
def delete_person(id):
    try:
        affected_rows = PersonsModel.delete_person(id)
        return jsonify({'affected_rows': affected_rows})
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500