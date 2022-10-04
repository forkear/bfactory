#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from bfactory.utils.paths import Paths
from bfactory.core.engine import Engine
from bfactory.inputs.arguments import parser
from bfactory.inputs.manifest import Manifest
from bfactory.startproject.startproject import StartProject

fpaths = Paths()

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

        engine = Engine(manifest=manifest)
        
        if engine.create_api() and run_api:
            sp = StartProject(engine=engine)
            sp.run()

    except Exception as e:
        print(f"[ E ] >> {e}")
        exit(3)



if __name__ == '__main__':
    main()
