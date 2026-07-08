import pytest
from nucleiq import adjacent_ones

######################################
#        Parameterized tests         #
######################################

@pytest.mark.parametrize("mock_data, expected_result",
    [
        ({"cells": [0, 1, 1, 1, 0]}, "POSITIVE"),
    
        ({"cells": [1, 0, 1, 0, 0]}, "NEGATIVE"),
        
        ({"cells": [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]}, "NEGATIVE"),
        
        ({"cells": [1, 1, 0, 0, 0, 0, 0, 0, 1, 1]}, "POSITIVE")
    ]
)

def test_adjacent_ones(mock_data, expected_result):
    result = adjacent_ones(mock_data)
    assert result == expected_result