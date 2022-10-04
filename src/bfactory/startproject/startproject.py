#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from bfactory.core.engine import Engine
from bfactory.utils.paths import Paths 


fpaths=Paths()

class StartProject():

    def __init__(self, engine: Engine ):
        self.engine = engine 

    def run(self) -> bool:
        fpaths.chdir_project()
        os.system('python manage.py makemigrations api')
        os.system('python manage.py migrate')
        os.system('python manage.py createsuperuser --username admin --email admin@local.local --skip-check')
        os.system('python manage.py runserver 127.0.0.1:8181')
        
        return True 
    