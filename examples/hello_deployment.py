# -*- coding: utf-8 -*-
import dash
import dash_html_components as html


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello WSGI'),
])

wsgi_app = app.server
