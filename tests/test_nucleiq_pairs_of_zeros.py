import pytest
from nucleiq import pairs_of_zeros

######################################
#        Parameterized tests         #
######################################

@pytest.mark.parametrize("mock_data, expected_result",
    [
        ({"cells": [0, 1, 0, 1, 0, 1, 0, 1, 1, 1]}, "POSITIVE"),
    
        ({"cells": [0, 1, 0, 1, 1, 1, 1, 1, 1, 1]}, "NEGATIVE"),
        
        ({"cells": [0, 1, 0, 1, 0, 1, 1, 1, 1, 1]}, "NEGATIVE")
    ]
)

def test_pairs_of_zeros(mock_data, expected_result):
    result = pairs_of_zeros(mock_data)
    assert result == expected_result