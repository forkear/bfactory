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
        self.manifest_path = fpaths.abspath('bfactory/tests/manifest_test.json')
        self.manifest = Manifest(file_path_manifest=self.manifest_path)
        fpaths.manifest = self.manifest    
        fpaths.to_path = to_path
        fpaths.check_path(to_path, force=False)
        self.engine = Engine(manifest=self.manifest)

    def test_model_creation(self):
        self.engine.create_api()
