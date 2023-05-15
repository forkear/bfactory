#!/usr/bin/env python

from jsonschema import  validate

from bfactory.inputs.manifest import Manifest



#!/usr/bin/env python
import unittest

from bfactory.inputs.manifest import Manifest
from bfactory.inputs.validators import validar_manifiesto
from bfactory.utils.state import State
state = State()

class JsonSchemaTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.manifest_path = state.abspath('tests/manifest_test.json')
        self.jsonschema_path = state.abspath('inputs/manifest.schema.json')

    def test_validate_schema(self):
        resultado = validar_manifiesto(self.manifest_path)
        self.assertEqual(resultado, True)
        









