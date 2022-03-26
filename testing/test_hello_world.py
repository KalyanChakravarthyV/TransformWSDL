"""
License: CC0-1.0 (Public Domain)
"""

from io import StringIO
from unittest.mock import patch

import pytest

import transform_wsdl

@pytest.mark.parametrize("argument_values", [True, 1, 1.0])
def test_example(argument_values):
    assert True == argument_values

def test_get_usage():
    assert transform_wsdl.get_usage() == "transform_wsdl <wsdl_location>"

def test_print_hello():
    with patch('sys.stdout', new=StringIO()) as dummy_out:
        transform_wsdl.hello_world()
        assert dummy_out.getvalue() == "Hello World!\n"

