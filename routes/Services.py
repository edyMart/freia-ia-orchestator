from flask import Blueprint, request, jsonify
from services.Agent import Agent as agent

""" Instanciar la ruta """
Services_BP = Blueprint('Services_BP', __name__)
Agent = agent()


@Services_BP.route('description', methods=['POST'])
def description():
    body_description = request.json
    response = Agent.description(body_description)

    return response

@Services_BP.route('regionalize', methods=['POST'])
def regionalize():
    body_description = request.json
    response = Agent.description(body_description)

    return response

@Services_BP.route('spellcheck', methods=['POST'])
def spellcheck():
    body_description = request.json
    response = Agent.spellcheck(body_description)

    return response

@Services_BP.route('images/description', methods=['POST'])
def images_description():
    body_description = request.json
    response = Agent.images_description(body_description)

    return response

@Services_BP.route('products/img', methods=['POST'])
def products_img():
    body_description = request.json
    response = Agent.products_img(body_description)

    return response