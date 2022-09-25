#!/usr/bin/env python
#import sys

import argparse
import pathlib

import textwrap
from banners import TITLE_BANNER
from inputdata.manifest import Manifest
from inputdata.validators import ManifestFileType
from tests.run_tests import run_tests
from utils.paths import Paths
from engine import engine
from startproject.startproject import StartProject


fpaths = Paths()


class TestAction(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if 'test' in values:
            if run_tests():
                exit(0)
            exit(1)
        setattr(namespace, self.dest, values)


parser = argparse.ArgumentParser(
    prog='bfactory',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent(TITLE_BANNER),
    epilog='Gracias a Django',
)


parser.add_argument(
    'test',
    nargs='?',
    help='Ejecutar test de unidad',
    action=TestAction,
    default=None
)

parser.add_argument(
    '--manifest',
    '-m',
    type=ManifestFileType(),
    help='Archivo que contine el manifiesto de la API en formato json',
    required=False
)

parser.add_argument(
    '--path',
    '-p',
    type=pathlib.Path,
    help='Path destino',
    required=False
)


parser.add_argument(
    '--force',
    '-f',
    nargs='*',
    type=pathlib.Path,
    help='Si existe Path destino lo borra',
    required=False
)


parser.add_argument(
    '--run',
    '-r',
    nargs='*',
    type=pathlib.Path,
    help='Ejecuta localmente la api luego de crearla',
    required=False
)


if __name__ == '__main__':

    args = parser.parse_args()

    manifest = getattr(args, 'manifest')
    to_path = getattr(args, 'path')
    force = getattr(args, 'force', None) != None
    run_api = getattr(args, 'run', None) != None
   
    if not manifest or not to_path:
        parser.print_help()
        exit(1)

    if not fpaths.check_path(to_path, force):
        exit(2)

    try:

        manifest = Manifest(manifest.name)
        fpaths.manifest = manifest
        fpaths.to_path = to_path

        engine = engine.Engine(manifest=manifest)
        
        if engine.create_api() and run_api:
            sp = StartProject(engine=engine)
            sp.run()

    except Exception as e:
        print(f"[ E ] >> {e}")
        exit(3)
