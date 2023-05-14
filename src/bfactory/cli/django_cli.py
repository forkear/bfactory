#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from bfactory.core.engine import Engine
from bfactory.utils.state import State 


state=State()

class DjangoCli():

    def __init__(self, engine: Engine ):
        self.engine = engine
        state.chdir_project()
         

    def run(self) -> bool:
        self.update()
        os.system('python manage.py runserver 127.0.0.1:8181')
        return True 

    def update(self) -> bool:
        os.system('python manage.py makemigrations api')
        os.system('python manage.py migrate')
        return True
    
    def create_admin(self) -> bool:
        os.system('python manage.py createsuperuser --username admin --email admin@local.local --skip-check')
        return True