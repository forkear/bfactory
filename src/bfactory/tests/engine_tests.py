#!/usr/bin/env python
import unittest

from bfactory.inputs.manifest import Manifest
from bfactory.core.engine import Engine
from bfactory.utils.paths import Paths

fpaths = Paths()

class EngineTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        to_path = '/tmp/test_bfactory'
        if not fpaths.check_path(to_path, force=True):
            exit(2)
        path_manifest = 'bfactory/tests/manifest_test.json'
        force = False

        manifest = Manifest(file_path_manifest=path_manifest)
        fpaths.manifest = manifest    
        fpaths.to_path = to_path
        fpaths.check_path(to_path, force)
        self.engine = Engine(manifest=manifest)

    def test_model_creation(self):
        self.engine.create_api()
