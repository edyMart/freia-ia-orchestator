from flask import Blueprint, jsonify

""" Instanciar la ruta """
Description_BP = Blueprint('Description_BP', __name__)

@Description_BP.route('', methods=['POST'])
def oauth():
    return jsonify({"response": ""})