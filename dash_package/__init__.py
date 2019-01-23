from flask import Flask

import dash

server = Flask(__name__)


app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')
