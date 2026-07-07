from unittest.mock import patch, Mock
from nucleiq import matrix

######################################
#             Test Unit              #
######################################

@patch('nucleiq.requests.get')
def test_matrix_unit(get_mock):
    response_false = Mock()
    response_false.text = '{"name": "mock", "cells": [0, 1, 1, 0]}'
    get_mock.return_value = response_false
    
    res = matrix('mock')
    
    assert res['name'] == 'mock'
    assert res['cells'] == [0, 1, 1, 0]
    
    get_mock.assert_called_once()
    
######################################
#         Integration Test           #
######################################

def test_matrix_integration():
    res = matrix('sample-a')
    
    assert 'name' in res
    assert 'cells' in res
    assert res['name'] == 'sample-a'
    assert type(res['cells']) is list