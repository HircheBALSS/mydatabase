from flask import Blueprint, request, jsonify
from tables import Livre

livres_blueprint = Blueprint('livres', __name__)

@livres_blueprint.route('/livres', methods=['POST'])
def ajouter_livre():
    from instance import db_session  
    data = request.json
    titre = data.get('titre') 
    auteur = data.get('auteur') 
    annee = data.get('annee')  
    livre = Livre(titre=titre, auteur=auteur, annee=annee)
    db_session.add(livre)
    db_session.commit()
    return 'Livre ajouté avec succès', 201 

@livres_blueprint.route('/livres', methods=['GET'])
def obtenir_livres():
    from instance import db_session  
    from instance import db_session
    livres = db_session.query(Livre).all()
    livres_json = [livre.to_dict() for livre in livres]
    return jsonify(livres_json), 200

@livres_blueprint.route('/livres/<int:livre_id>', methods=['GET'])
def obtenir_livre(livre_id):
    from instance import db_session  
    livre = db_session.query(Livre).get(livre_id)
    if livre:
        return jsonify(livre.to_dict()), 200
    else:
        return 'Livre non trouvé', 404

@livres_blueprint.route('/livres/<int:livre_id>', methods=['PUT'])
def mettre_a_jour_livre(livre_id):
    from instance import db_session  
    livre = db_session.query(Livre).get(livre_id)
    if livre:
        data = request.json
        titre = data.get('titre') 
        auteur = data.get('auteur')
        annee = data.get('annee')  
        livre.titre = titre
        livre.auteur = auteur
        livre.annee = annee
        db_session.commit()
        return 'Livre mis à jour avec succès', 200
    else:
        return 'Livre non trouvé', 404

@livres_blueprint.route('/livres/<int:livre_id>', methods=['DELETE'])
def supprimer_livre(livre_id):
    from instance import db_session 
    livre = db_session.query(Livre).get(livre_id)
    if livre:
        db_session.delete(livre)
        db_session.commit()
        return 'Livre supprimé avec succès', 200
    else:
        return 'Livre non trouvé', 404
