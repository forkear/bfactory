#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from bfactory.cli.django_cli import DjangoCli
from bfactory.utils.state import State
from bfactory.core.engine import Engine
from bfactory.inputs.arguments import parser
from bfactory.inputs.manifest import Manifest



def main():

    
    args = parser.parse_args()

    state = State()    
    state.to_path = getattr(args, 'path', None)
    state.update = getattr(args, 'update', None) != None 
    state.force = getattr(args, 'force', None) != None
    state.run_api = getattr(args, 'run', None) != None
    state.template = getattr(args, 'template', None)
    state.create_admin = getattr(args, 'createadmin', None) != None

    manifest = getattr(args, 'manifest', None)
    
    if not manifest or not state.to_path:
        parser.print_help()
        return False

    if not state.check_path():
        return False

    try:

        state.manifest = Manifest(manifest.name)

        engine = Engine()
        api_created = engine.create_api()

        if api_created:
            django_cli = DjangoCli(engine=engine)
            if state.is_an_update():
                django_cli.update()

            if state.create_admin:
                django_cli.create_admin()

            if state.run_api:
                django_cli.run()
        

    except Exception as e:
        print(f"[ E ] >> {e}")
        exit(3)




if __name__ == '__main__':
    main()
