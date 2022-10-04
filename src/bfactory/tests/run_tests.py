#!/usr/bin/env python
import unittest

from bfactory.tests.manifest_test import ManifestTest
from bfactory.tests.engine_tests import EngineTest


def create_suite(classes, unit_tests_to_run):
    
    suite = unittest.TestSuite()
    unit_tests_to_run_count = len( unit_tests_to_run )

    for _class in classes:
        _object = _class()
        for function_name in dir( _object ):
            if function_name.lower().startswith( "test" ):
                if unit_tests_to_run_count > 0 \
                        and function_name not in unit_tests_to_run:
                    continue
                suite.addTest( _class( function_name ) )
    return suite

def run_tests() -> bool:
    runner = unittest.TextTestRunner()
    classes =  [
        ManifestTest,
        EngineTest,
    ]

    unit_tests_to_run =  [ ]
    result = runner.run( create_suite( classes, unit_tests_to_run ) )
    return result.wasSuccessful()
    