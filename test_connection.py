from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

@app.route('/')
def index():
    try:
        logger.debug("Tentando executar SELECT no banco de dados")
        result = db.session.execute(text('SELECT id, name, type, balance, financial_institution_id FROM public.account'))
        rows = result.fetchall()
        data = []
        return jsonify('Connection Ok')
    except Exception as e:
        logger.error(f'Connection failed: {e}')
        return {
            "error": "Database error",
            "details": str(e)
        }, 500

if __name__ == '__main__':
    app.run(debug=True)
