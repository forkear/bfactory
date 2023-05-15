#!/usr/bin/env python
import unittest

from bfactory.inputs.manifest import Manifest
from bfactory.utils.state import State
state = State()

class ManifestTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.manifest_path = state.abspath('tests/manifest_test.json')
        self.manifest = Manifest(file_path_manifest=self.manifest_path)

    def test_version(self):
        self.assertEqual(self.manifest.app_version, "1")
    
    def test_model(self):
        schema = self.manifest.get_shema()
        models = self.manifest.get_models()
        self.assertEqual(3, len(models))
        self.assertEqual("Author", models[0].name)
        self.assertEqual("Book", models[1].name)
        self.assertEqual("Todo", models[2].name)
        






