# app.py
from flask import Flask
from flask_cors import CORS
from src.infra.http_server.http_server import create_app
from flask.cli import FlaskGroup
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app()
CORS(app)

cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
