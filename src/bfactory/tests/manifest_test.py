#!/usr/bin/env python
import unittest

from bfactory.inputs.manifest import Manifest

class ManifestTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.manifest_path = 'bfactory/tests/manifest_test.json'
        self.manifest = Manifest(file_path_manifest=self.manifest_path)

    def test_version(self):
        self.assertEqual(self.manifest.app_version, "1")
    
    def test_model(self):

        schema = self.manifest.get_shema()
        models = self.manifest.get_models()
        self.assertEqual(1, len(models))
        self.assertEqual("Tarea", models[0].name)
        






