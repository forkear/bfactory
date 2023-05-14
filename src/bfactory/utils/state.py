#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from argparse import Namespace
import os
import shutil
from bfactory.inputs import manifest
from bfactory.inputs.manifest import Manifest


class Singleton (type):
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class State(metaclass=Singleton):

    update = False 
    run = False 
    force = False 
    template = None
    run_api = False 
    create_admin = False 


    def init(self, manifest: Manifest = None, path: str = ""):
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

    def check_path(self) -> bool:
        
        
        if os.path.exists(self.to_path):

            if self.update:
                print(f"[ W ] >> el path {self.to_path} se va a actualizar")
                return True


            if self.force or self.update:
                print(f"[ W ] >> el path {self.to_path} se va eliminar primero")
                shutil.rmtree(self.to_path)
                return True


            print(f"[ E ] >> el path {self.to_path} existe, usa:\n \t -f [ --force ] para borrarlo\n \t -u [ --update ] si se trata de un update")
            return False

        return True

    def mk_and_ch_dir(self, path: str) -> None:
        os.mkdir(path)
        os.chdir(path)
    
    
    def abspath(self, relative_path: str) -> str:
        """
        retorna el path absoluto en base al path de bfactory
        """
        import bfactory
        return os.path.join(os.path.dirname(bfactory.__file__), relative_path)
    
    
    def is_an_update(self):
        return self.update
        
