#!/usr/bin/env python
import unittest

from bfactory.inputs.manifest import Manifest
from bfactory.core.engine import Engine
from bfactory.utils.state import State

state = State()

class EngineTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        state.to_path = '/tmp/test_bfactory'
        state.force = True
        if not state.check_path():
            exit(2)
        
        self.manifest_path = state.abspath('tests/manifest_test.json')
        self.manifest = Manifest(file_path_manifest=self.manifest_path)
        
        state.manifest = self.manifest    
        
        self.engine = Engine()

    def test_model_creation(self):
        self.engine.create_api()
