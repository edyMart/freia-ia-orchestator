from flask import Blueprint, request, jsonify
from services.Oauth import Oauth as oauth

""" Instanciar la ruta """
Oauth_BP = Blueprint('Oauth_BP', __name__)

Oauth = oauth()

@Oauth_BP.route('/authorize', methods=['POST'])
def oauth():
    body_auth = request.json
    response = Oauth.authorize(body_auth)
    return response

@Oauth_BP.route('/register', methods=['POST'])
def register():
    body_auth = request.json
    response = Oauth.register(body_auth)
    return response

@Oauth_BP.route('/token/verify', methods=['POST'])
def token_verify():
    Auth = request.headers['Authorization']
    response = Oauth.verify(Auth)
    return response