#!/usr/bin/env python
import unittest

from inputdata.manifest import Manifest
from engine.engine import Engine


from utils.paths import Paths

fpaths = Paths()

class EngineTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        to_path = '/tmp/test_bfactory'
        path_manifest = 'tests/manifest_test.json'
        force = False

        manifest = Manifest(file_path_manifest=path_manifest)
        fpaths.manifest = manifest    
        fpaths.to_path = to_path
        fpaths.check_path(to_path, force)
        self.engine = Engine(manifest=manifest)

    def test_model_creation(self):
        self.engine.run()
