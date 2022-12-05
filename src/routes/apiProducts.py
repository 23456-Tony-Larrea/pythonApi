from flask import Blueprint, request, jsonify
from models.ProductsModel import ProductsModel

main = Blueprint('api_products', __name__)

@main.route('/', methods=['GET'])
def get_products():
    try:
        products = ProductsModel.getProducts()
        return jsonify(products)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/<int:id>', methods=['GET'])
def get_products_id(id):
    try:
        products = ProductsModel.getProductsId(id)
        return jsonify(products)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/', methods=['POST'])
def add_products():
    try:
        products = request.get_json()
        affected_rows = ProductsModel.add_products(products)
        return jsonify({'affected_rows': affected_rows})
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500 

@main.route('/<int:id>', methods=['PUT'])
def update_product(id):
    try:
        products = request.get_json()
        affected_rows = ProductsModel.update_product(products,id)
        return jsonify({'affected_rows': affected_rows})
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500       

@main.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        affected_rows = ProductsModel.delete_product(id)
        return jsonify({'affected_rows': affected_rows})
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500