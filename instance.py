import inspect
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

from tables import Base

load_dotenv()

app = Flask(__name__)

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = "127.0.0.1"
db_port = 3300
db_name = os.getenv("DB_NAME")

# connexion

db_url = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)
db_session = scoped_session(sessionmaker(bind=engine))
Base.query = db_session.query_property()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':

    # Vérifie si les tables existent
    # inspector = inspect.inspect(engine)
    # if not inspector.has_table('ma_table'):
    #     Base.metadata.create_all(bind=engine)
    #     print("Les tables ont été créées avec succès.")
    # else:
    #     print("Les tables existent déjà.")


    from livrescontrollers import livres_blueprint
    from personnecontrollers import personnes_blueprint
    from empruntcontrollers import emprunts_blueprint
    from remisecontrollers import remises_blueprint
    from registre import register_bp
    # from auth import auth_bp
    

    app.register_blueprint(livres_blueprint, url_prefix='/livre/')
    app.register_blueprint(personnes_blueprint, url_prefix='/personne/')
    app.register_blueprint(emprunts_blueprint, url_prefix='/emprunt/')
    app.register_blueprint(remises_blueprint, url_prefix='/remise/')
    # app.register_blueprint(auth_bp, url_prefix='/auth/')
    app.register_blueprint(register_bp, url_prefix='/register/')

# deburger

    app.run(debug=True)

