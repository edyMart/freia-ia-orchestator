from flask import Blueprint, request, jsonify
from services.Agent import Agent as agent

""" Instanciar la ruta """
Services_BP = Blueprint('Services_BP', __name__)
Agent = agent()


@Services_BP.route('description', methods=['POST'])
def oauth():
    body_description = request.json
    response = Agent.description(body_description)

    return response