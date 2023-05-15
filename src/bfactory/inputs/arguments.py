from bfactory.config.settings import TITLE_BANNER
from bfactory.inputs.validators import ManifestFileType
from bfactory.tests.run_tests import run_tests
import argparse
import pathlib
import textwrap

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
    #description=textwrap.dedent(TITLE_BANNER),
    epilog='//thx_to = [ Python, Django, Jinja, Django REST framework ]\n',
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
    help='Si existe Path destino lo borra',
    required=False
)

parser.add_argument(
    '--update',
    '-u',
    nargs='*',
    help='Actualiza la aplicacion',
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

parser.add_argument(
    '--template',
    '-t',
    type=pathlib.Path,
    help='definir el path o url del template base para crear la api',
    required=False
)


parser.add_argument(
    '--createadmin',
    '-a',
    nargs='*',
    help='Crea el usuario admin',
    required=False
)

