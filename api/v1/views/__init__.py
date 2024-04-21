#!/usr/bin/python3
"""Script that creates the Blueprint Flask Class and import modules"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


# Importa todo desde el paquete api.v1.views.index
# Esta importación se coloca aquí para evitar problemas de importación circular y no es recomendada por PEP8,
# por lo tanto, es normal que PEP8 se queje al respecto. Este archivo no será verificado por PEP8.
from api.v1.views.index import *