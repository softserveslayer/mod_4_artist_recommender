from flask import render_template
from dash_package import server
import pdb



@server.route('/apartments')
def render_apartments():
    return 'hello'
