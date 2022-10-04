#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import os
import shutil
from bfactory.inputs import manifest
from bfactory.inputs.manifest import Manifest


class Singleton (type):
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Paths(metaclass=Singleton):

    manifest: Manifest = None
    to_path: str = ""

    def __init__(self, manifest: Manifest = None, path: str = ""):
        self.manifest = manifest
        self.to_path = path

    def __str__(self):
        return f"PATH: {self.to_path} MANIFEST: {self.manifest}"

    @property
    def base_path(self) -> str:
        if not self.manifest:
            return "#"
        return self.to_path

    @property
    def project(self) -> str:
        if not self.manifest:
            return "#"
        return os.path.join(self.to_path, self.manifest.app_slug)

    @property
    def path_app(self) -> str:
        return os.path.join(self.project, 'apps')

    @property
    def path_app_api(self) -> str:
        return os.path.join(self.path_app, 'api')

    @property
    def path_myconf(self) -> str:
        if not self.manifest:
            return "#"

        return os.path.join(self.manifest.app_slug, self.manifest.app_slug, 'myconf.py')

    def chdir_project(self) -> None:
        os.chdir(self.project)

    def path_file_from_project(self, file_name: str) -> str:

        return os.path.join(self.project, file_name)

    def path_file_from_app_api(self, file_name: str) -> str:

        return os.path.join(self.path_app_api, file_name)

    def check_path(self, path: str, force: bool) -> bool:

        if os.path.exists(path):
            if force:
                print(f"[ W ] >> el path {path} se va eliminar primero")
                shutil.rmtree(path)
                return True

            print(f"[ E ] >> el path {path} existe, usa -f / --force para borrarlo")
            return False

        return True

    def mk_and_ch_dir(self, path: str) -> None:
        os.mkdir(path)
        os.chdir(path)
