from flask import Blueprint, request, jsonify
from tables import Personne

personnes_blueprint = Blueprint('personnes', __name__)

@personnes_blueprint.route('/personnes', methods=['POST'])
def ajouter_personne():
    from instance import db_session
    data = request.json
    nom = data.get('nom')
    prenom = data.get('prenom')
    abonne = data.get('abonne', False)
    password = data.get('password')
    personne = Personne(nom=nom, prenom=prenom, abonne=abonne, password=password)
    db_session.add(personne)
    db_session.commit()
    return 'Personne ajoutée avec succès', 201

@personnes_blueprint.route('/personnes', methods=['GET'])
def obtenir_personnes():
    from instance import db_session
    personnes = db_session.query(Personne).all()
    personnes_json = [personne.to_dict() for personne in personnes]
    return jsonify(personnes_json), 200

@personnes_blueprint.route('/personnes/<int:personne_id>', methods=['GET'])
def obtenir_personne(personne_id):
    from instance import db_session
    personne = db_session.query(Personne).get(personne_id)
    if personne:
        return jsonify(personne.to_dict()), 200
    else:
        return 'Personne non trouvée', 404

@personnes_blueprint.route('/personnes/<int:personne_id>', methods=['PUT'])
def mettre_a_jour_personne(personne_id):
    from instance import db_session
    personne = db_session.query(Personne).get(personne_id)
    if personne:
        data = request.json
        nom = data.get('nom')
        prenom = data.get('prenom')
        abonne = data.get('abonne')
        password = data.get('password')
        personne.nom = nom
        personne.prenom = prenom
        personne.abonne = abonne
        personne.password = password
        db_session.commit()
        return 'Personne mise à jour avec succès', 200
    else:
        return 'Personne non trouvée', 404

@personnes_blueprint.route('/personnes/<int:personne_id>', methods=['DELETE'])
def supprimer_personne(personne_id):
    from instance import db_session
    personne = db_session.query(Personne).get(personne_id)
    if personne:
        db_session.delete(personne)
        db_session.commit()
        return 'Personne supprimée avec succès', 200
    else:
        return 'Personne non trouvée', 404
