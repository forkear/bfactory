#!/usr/bin/env python

import os
from typing import List
import json 
import argparse
from jsonschema import Draft202012Validator, ErrorTree, SchemaError, ValidationError, validate

from bfactory.utils.state import State


V_ENTORNO = [
    "BFACTORY_BUILD_PATH",
]


def validar_variables_de_entorno() -> bool:
    """
        Un simple validador de variables de entorno
    """
    success = True 
    for v in V_ENTORNO:
        if not v in os.environ:
            print(f"No esta definida la variable {v} ")
            success=False
    
    return success


def validar_manifiesto(file_name:str) -> bool:
    """
        Un simple validador del manifiesto.
        Verifica:
            - si existe el archivo
            - si es un json valido

        TODO:
            - validar la estructura del manifiesto
    """
    state = State()
    manifest = {}
    schema = {}
    jsonschema_path = state.abspath('inputs/manifest.schema.json')


    #verifico si existe el archivo:
    if not os.path.exists(file_name):
        print("El archivo de manifiesto no existe")
        return False 

    try:
        with open(file_name) as f:
            manifest = json.load(f)
        f.close()
    except Exception as e:
        
        print("[ E ] >> El archivo de manifiesto no es un JSON valido")
        return False 

    try:
        
        with open(jsonschema_path) as sf:
            schema = json.load(sf)
        sf.close()
        validator = Draft202012Validator(schema=schema)
        errors = list(validator.iter_errors(manifest))
        if not errors:
            return True 
        
        print("[ E ] >> El manifiesto no es valido")
        for error in errors:
            print(error.message)

        return False    
    
    except ValidationError as ve:
        print("[ E ] >> El archivo de manifiesto valido")
        return False


class ManifestFileType(argparse.FileType):

    def __call__(self, filename):
        
        resp = super(ManifestFileType, self).__call__(filename)
        if not validar_manifiesto(file_name=filename):
            raise argparse.ArgumentTypeError('No es un manifiesto valido')
        return resp 
