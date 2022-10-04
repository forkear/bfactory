#!/usr/bin/env python


import glob
from io import BytesIO
import shutil
from zipfile import ZipFile
from urllib.request import urlopen
import os
from bfactory.inputs.manifest import Manifest
from bfactory.config.settings import URL_BASE_BACKEND
from bfactory.utils.render import render_to_file
from bfactory.utils.crypto import get_random_secret_key
from bfactory.utils.paths import Paths

fpaths = Paths()


def get_zip_base_project(slug: str, path: str = None) -> bool:
    """
        Se encarga de descargar el archivo zip de un proyecto
        base creado en django para nuestra futura api. 
        Luego de descargar el zip lo descomprime en el path dado
        y a continuacion se renombran los directorios y los imports
        para que sea igual que el slug de nuestra api autogenerada
    """

    print("> geting main.zip")
    if not path:
        path = fpaths.base_path

    resp = urlopen(URL_BASE_BACKEND)

    base_path_name = os.path.join(path, slug)

    print("> main.zip in memory ")

    zipfile = ZipFile(BytesIO(resp.read()))

    zipfile.extractall(path=path)

    # eliminamos codigo viejo
    shutil.rmtree(base_path_name, ignore_errors=True)

    # renombramos directorios base
    print("> renombramos directorios ")

    os.rename('forkear-backend-main/forkear-backend',
              f'forkear-backend-main/{slug}')
    os.rename('forkear-backend-main', f'{slug}')

    print("> refactorizamos el codigo base ")

    for filepath in glob.iglob('./**/*.py', recursive=True):
        with open(filepath) as file:
            s = file.read()
        s = s.replace('forkear-backend', slug)
        with open(filepath, "w") as file:
            file.write(s)
    print("> proyecto base listo :-) ")

    return True


def crear_configuracion_del_proyecto(manifest: Manifest) -> bool:
    """
        Crea el archivo myconf.py
    """

    values = {
        'secret_key': get_random_secret_key(),
        'database': manifest.database,
        'auth': manifest.auth,
    }
    render_to_file(template='myconf.py',
                   file_name=fpaths.path_myconf, values=values)
    return True


