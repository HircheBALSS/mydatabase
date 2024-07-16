from flask import Blueprint, jsonify, request, session
from tables import Personne


register_bp = Blueprint('register', __name__)

@register_bp.route('/enregistrement', methods=['POST'])
def enregistrement():
    from instance import db_session
    data = request.get_json()
    hashed_password = Personne().hash_password(data['c'])
    
    personne_existante = Personne.query.filter_by(nom=data['nom']).first()
    if personne_existante:
        return jsonify({'message':'un compte existe deja'})

    nouvelle_personne = Personne(
        nom=data['nom'], prenom=data['prenom'], abonne=data['abonne'], password=hashed_password)
    db_session.add(nouvelle_personne)
    db_session.commit()
    
    return jsonify({'message': 'compte cree'})
