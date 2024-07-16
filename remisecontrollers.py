from flask import Blueprint, request, jsonify
from tables import Remise

remises_blueprint = Blueprint('remises', __name__)

@remises_blueprint.route('/remises', methods=['POST'])
def ajouter_remise():
    from instance import db_session
    data = request.json
    emprunt_id = data.get('emprunt_id') 
    heure_remise = data.get('heure_remise')  
    remise = Remise(emprunt_id=emprunt_id, heure_remise=heure_remise)
    db_session.add(remise)
    db_session.commit()
    return 'Remise ajoutée avec succès', 201 

@remises_blueprint.route('/remises', methods=['GET'])
def obtenir_remises():
    from instance import db_session
    remises = db_session.query(Remise).all()
    remises_json = [remise.to_dict() for remise in remises]
    return jsonify(remises_json), 200

@remises_blueprint.route('/remises/<int:remise_id>', methods=['GET'])
def obtenir_remise(remise_id):
    from instance import db_session
    remise = db_session.query(Remise).get(remise_id)
    if remise:
        return jsonify(remise.to_dict()), 200
    else:
        return 'Remise non trouvée', 404

@remises_blueprint.route('/remises/<int:remise_id>', methods=['PUT'])
def mettre_a_jour_remise(remise_id):
    from instance import db_session
    remise = db_session.query(Remise).get(remise_id)
    if remise:
        data = request.json
        emprunt_id = data.get('emprunt_id') 
        heure_remise = data.get('heure_remise')  
        remise.emprunt_id = emprunt_id
        remise.heure_remise = heure_remise
        db_session.commit()
        return 'Remise mise à jour avec succès', 200
    else:
        return 'Remise non trouvée', 404

@remises_blueprint.route('/remises/<int:remise_id>', methods=['DELETE'])
def supprimer_remise(remise_id):
    from instance import db_session
    remise = db_session.query(Remise).get(remise_id)
    if remise:
        db_session.delete(remise)
        db_session.commit()
        return 'Remise supprimée avec succès', 200
    
    return 'Remise non trouvée', 404
