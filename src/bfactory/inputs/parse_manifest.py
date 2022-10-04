#!/usr/bin/env python

import json

class ParseManifest():

    
    def __init__(self, file_path_manifest: str ):
        self.file_path_manifest=file_path_manifest 
        self.load()
    
    def load(self) -> None:

        with open(self.file_path_manifest) as f:
            self.conf = json.load(f)
        f.close()

        self.app_name=self.conf['name']
        self.app_version=self.conf['version']
        self.auth=self.conf['auth']
        self.database = self.conf['database']
        self.schema = self.conf['schema']


    def show_conf(self) -> None:
        
        print(f"\n\nNombre de la app: {self.app_name}")
        print(f"Version: {self.app_version}")

        print("Schema:")
        for objeto in self.schema:
            (f"\t-{objeto['name']}")
            for attr in objeto['attrs']:
                print(f"\t\t-{attr['type']}\t-> {attr['name']}")

