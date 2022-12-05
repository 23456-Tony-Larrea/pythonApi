from flask import Blueprint, request, jsonify
from models.InvoiceModel import InvoicesModel 

main = Blueprint('api_invoice', __name__)

@main.route('/', methods=['GET'])
def get_invoices():
    try:
        invoice = InvoicesModel.getInvoice()
        return jsonify(invoice)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/<int:id>', methods=['GET'])
def get_invoices_id(id):
    try:
        invoices = InvoicesModel.getInvoicesId(id)
        return jsonify(invoices)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/', methods=['POST'])
def add_invoices():
    try:
        invoices = request.get_json()
        affected_rows = InvoicesModel.add_invoice(invoices)
        return jsonify({'affected_rows': affected_rows})
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500 

@main.route('/<int:id>', methods=['PUT'])
def update_invoice(id):
    try:
        invoice = request.get_json()
        affected_rows = InvoicesModel.update_invoices(invoice,id)
        return jsonify({'affected_rows': affected_rows})
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500       

@main.route('/<int:id>', methods=['DELETE'])
def delete_invoice(id):
    try:
        affected_rows = InvoicesModel.delete_invoice(id)
        return jsonify({'affected_rows': affected_rows})
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500