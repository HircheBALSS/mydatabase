from flask import Blueprint, request, jsonify
from tables import Emprunt

emprunts_blueprint = Blueprint('emprunts', __name__)

@emprunts_blueprint.route('/emprunts', methods=['POST'])
def ajouter_emprunt():
    from instance import db_session
    data = request.json
    livre_id = data.get('livre_id') 
    personne_id = data.get('personne_id')  
    heure_emprunt = data.get('date_emprunt')  
    emprunt = Emprunt(livre_id=livre_id, personne_id=personne_id, heure_emprunt=heure_emprunt)
    db_session.add(emprunt)
    db_session.commit()
    return 'Emprunt ajouté avec succès', 201 

@emprunts_blueprint.route('/emprunts', methods=['GET'])
def obtenir_emprunts():
    from instance import db_session
    emprunts = db_session.query(Emprunt).all()
    emprunts_json = [emprunt.to_dict() for emprunt in emprunts]
    return jsonify(emprunts_json), 200

@emprunts_blueprint.route('/emprunts/<int:emprunt_id>', methods=['GET'])
def obtenir_emprunt(emprunt_id):
    from instance import db_session
    emprunt = db_session.query(Emprunt).get(emprunt_id)
    if emprunt:
        return jsonify(emprunt.to_dict()), 200
    else:
        return 'Emprunt non trouvé', 404

@emprunts_blueprint.route('/emprunts/<int:emprunt_id>', methods=['PUT'])
def mettre_a_jour_emprunt(emprunt_id):
    from instance import db_session
    emprunt = db_session.query(Emprunt).get(emprunt_id)
    if emprunt:
        data = request.json
        livre_id = data.get('livre_id') 
        personne_id = data.get('personne_id')  
        heure_emprunt = data.get('date_emprunt')  
        emprunt.livre_id = livre_id
        emprunt.personne_id = personne_id
        emprunt.heure_emprunt = heure_emprunt
        db_session.commit()
        return 'Emprunt mis à jour avec succès', 200
    else:
        return 'Emprunt non trouvé', 404

@emprunts_blueprint.route('/emprunts/<int:emprunt_id>', methods=['DELETE'])
def supprimer_emprunt(emprunt_id):
    from instance import db_session
    emprunt = db_session.query(Emprunt).get(emprunt_id)
    if emprunt:
        db_session.delete(emprunt)
        db_session.commit()
        return 'Emprunt supprimé avec succès', 200
    else:
        return 'Emprunt non trouvé', 404
