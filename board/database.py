# The sqlite3 module, a built-in Python module for interacting with SQLite databases
import sqlite3
# click, a Python package for creating command-line interfaces (CLI)
import click

# The current_app object points to the Flask application handling the current activity. You can use it to access
# application-specific data like your environment variables. The use of current_app makes your code more flexible
from flask import current_app, g
# With g, Flask provides you with a global namespace object that you can use as temporary storage when a user makes a
# request, such as sending a form. Each request has its own g object, which resets at the end of the request. This is
# useful for storing data that might be accessed multiple times during the request, such as a database connection,
# avoiding the need to create new connections for every single database operation within the same request


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

@click.command("init-db")
def init_db_command():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))

    click.echo('Database Successfully Initialized')


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

