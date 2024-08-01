from flask import Blueprint, jsonify

""" Instanciar la ruta """
Services_BP = Blueprint('Services_BP', __name__)

@Services_BP.route('/', methods=['POST'])
def oauth():
    return jsonify({"response": ""})