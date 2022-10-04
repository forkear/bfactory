#!/usr/bin/env python
import json
from typing import Dict, List

class Field():

    def __init__(self, obj:Dict):

        self.name = obj['name']
        self.type = obj['type']
        self.req = obj['req']
        if 'default' in obj:
            self.default = obj['default']
        if 'fk' in obj:
            self.fk = obj['fk']
        else:
            self.default = None
    
    def __str__(self) -> str:
        return f"{self.name} - {self.type}"  



class Model():
    
    def __init__(self, obj:Dict):
        self.name=obj['name']
        self.fields = [ Field(field) for field in obj['attrs']]
    
    def __str__(self) -> str:
        return f"Model: {self.name}"
         

class Database:
    
    def __init__(self, obj: Dict ):
        self.db_type = obj.get('type', 'sqlite')
        self.db_name = obj.get('name', 'default_db_name')
        self.db_user = obj.get('username', 'default_db_user')
        self.db_pass = obj.get('password', 'default_db_pass')
        self.db_host = obj.get('username', '127.0.0.1')
        self.db_port = obj.get('username', '5432')
    
    def __str__(self) -> str:
        return f"Database [{self.db_type}] Name: {self.db_name}"



class Manifest():
    """
        Manifest
    """
    
    def __init__(self, file_path_manifest: str ):
        self.file_path_manifest=file_path_manifest 
        self.load()
    
    def load(self) -> None:

        with open(self.file_path_manifest) as f:
            manifest_json = json.load(f)
        f.close()

        
        self.app_name = manifest_json['name']
        self.app_slug = self.app_name.strip().replace(' ','_').lower()

        self.app_version=manifest_json['version']
        self.auth=manifest_json['auth']
        
        self.database = Database(obj=manifest_json['database'])
        
        self.schema = manifest_json['schema']


    def get_shema(self) -> Dict:
        return self.schema

    def get_models(self) -> List:
        return [ Model(model) for model in self.schema ]


    def _str_schema(self) -> str:
        s = "\n\t"
        for objeto in self.schema:
            s+=f"\t* {objeto['name']}:\n"
            for attr in objeto['attrs']:
                s+=f"\t\t\t{attr['name']} : {attr['type']}\n"
        return s
        

    def _str_config(self) -> str:

        str_config = f'''\nManifest:
            App: {self.app_name}
            Version: {self.app_version}
            Schema: {self._str_schema()}
        '''

        return str_config


    def __str__(self) -> str:
        return self._str_config()

