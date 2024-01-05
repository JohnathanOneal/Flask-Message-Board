# !/usr/bin/env python
# Application factory
#  With an application factory, your project’s structure becomes more organized. It encourages you to separate different
#  parts of your application, like routes, configurations, and initializations, into different files later on.
#  This encourages a cleaner and more maintainable codebase.

from flask import Flask

# pages is where we create our blueprint and defined the two routes
from board import pages, posts


def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)

    return app
