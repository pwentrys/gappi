from flask import render_template
from flask_cors import *


icon_base = '/images/manifest/'
icon_file = 'icon-'
icon_ext = '.png'
icon_path_array = []
icon_sizes = [
    (48, 48),
    (72, 72),
    (96, 96),
    (144, 144),
    (192, 192),
    (512, 512)
]

for size in icon_sizes:
    icon_path_array.append(f'{icon_base}{icon_file}{size[0]}x{size[1]}{icon_ext}')


def app_routes(app):
    # ---------------------------------------------------------------------------- #
    #                                                                              #
    #                           Landing Page                                       #
    #                                                                              #
    # ---------------------------------------------------------------------------- #
    @app.route('/index')
    @app.route('/index.html')
    @app.route('/')
    @cross_origin()
    def index():
        return render_template('index.html', page_title=app.__name__, icons=icon_sizes)

    @app.route('/home')
    @app.route('/home.html')
    @cross_origin()
    def home():
        return render_template('home.html', page_title=app.__name__, icons=icon_sizes)

    @app.route('/todo')
    @app.route('/todo.html')
    @cross_origin()
    def todo():
        return render_template('todo.html', page_title=app.__name__, icons=icon_sizes)
