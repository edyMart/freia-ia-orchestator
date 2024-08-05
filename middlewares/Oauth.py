from services.Oauth import Oauth as oauth
from flask import request, jsonify

Oauth = oauth()

def OauthMiddleware():

    endpoint = request.endpoint.split('.')[0]
    print("Viene aqui", endpoint)
    if(endpoint != "Oauth_BP"):

        if 'Authorization' not in request.headers:
            response = jsonify({"error": "Authorization is required"})
            response.status_code = 400
            return response
        else:
            Auth = request.headers['Authorization']
            OauthValidate = Oauth.tokenVerify(Auth)

            print("Oauth", OauthValidate)

            if OauthValidate != 201:
                return jsonify({"error": "Invalid token"})