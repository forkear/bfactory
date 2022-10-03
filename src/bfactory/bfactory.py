#!/usr/bin/env python

import argparse
import pathlib

import textwrap
from bfactory.config.settings import TITLE_BANNER
from bfactory.inputdata.manifest import Manifest
from bfactory.inputdata.validators import ManifestFileType
from bfactory.tests.run_tests import run_tests
from bfactory.utils.paths import Paths
from bfactory.engine import engine
from bfactory.startproject.startproject import StartProject


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



def main():
 

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

        eng = engine.Engine(manifest=manifest)
        
        if eng.create_api() and run_api:
            sp = StartProject(engine=eng)
            sp.run()

    except Exception as e:
        print(f"[ E ] >> {e}")
        exit(3)



if __name__ == '__main__':
    main()
