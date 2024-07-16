# # from flask import app, jsonify, request, session
# # from tables import Personne
# # from instance import db_session
# # from flask import Flask

# # @app.route('/authentification', methods=['POST'])
# # def authentification():
# #     data = request.get_json()
# #     hashed_password = Personne().hash_password(data['password'])
# #     personne_authentifiee = db_session.query(Personne).filter_by(nom=data['nom'], password=hashed_password).first()

# #     if personne_authentifiee:
# #         return jsonify({'message': 'Authentification réussie'})
# #     else:
# #         return jsonify({'message': 'Authentification échouée'})

# from tables import Personne
# from flask import Blueprint, request, jsonify
# from flask_jwt import JWT, jwt_required, current_identity
# from flask import app, Flask


# auth_bp = Blueprint('auth', __name__)

# def authenticate(nom, password):
#     personne = Personne.get_by_username(nom)
#     if personne and personne.verify_password(password):
#         return personne

# def identity(payload):
#     user_id = payload['identity']
#     return Personne.query.get(user_id)

# jwt = JWT(app, authenticate, identity)

# @auth_bp.route('/authentification', methods=['POST'])
# @jwt_required()
# def authentification():
#     return jsonify({'message': 'Authentification réussie', 'user': current_identity.to_dict()})
