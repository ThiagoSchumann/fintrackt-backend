# app.py
from src.infra.http_server.http_server import create_app, db
from flask.cli import FlaskGroup

app = create_app()
cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
