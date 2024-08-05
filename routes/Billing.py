from flask import Blueprint, request


""" Instanciar la ruta """
Billing_BP = Blueprint('Billing_BP', __name__)



@Billing_BP.route('/create', methods=['POST'])
def oauth():
    body_auth = request.json
    return ""