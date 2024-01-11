# !/usr/bin/env python
# Application factory
#  With an application factory, your project’s structure becomes more organized. It encourages you to separate different
#  parts of your application, like routes, configurations, and initializations, into different files later on.
#  This encourages a cleaner and more maintainable codebase.

import os
from dotenv import load_dotenv
from flask import Flask

# pages is where we create our blueprint and defined the two routes
from board import pages, posts, database

load_dotenv()

def create_app():
    app = Flask(__name__)

    # When you use app.config.from_prefixed_env() you have access to all environment variables that start with FLASK_
    app.config.from_prefixed_env()
    # you can access them with app.config.get() with the variable named after this prefix. That’s why you pass DATABASE
    # instead of FLASK_DATABASE into .get(). For any other environment variables that don’t start with FLASK_, you can use os.getenv().

    database.init_app(app)
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)

    print(os.getenv('ENVIRONMENT'))
    print(app.config.get('DATABASE'))
    return app
