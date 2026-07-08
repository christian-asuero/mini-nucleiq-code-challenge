import json
import requests

'''
Phase 1: Read the matrix
Input: Matrix with samples
Output: Dictionary of a given sample
'''

def matrix(sample):
    
    response = requests.get(f'https://raw.githubusercontent.com/cellsia/mini-nucleiq-code-challenge/main/samples/{sample}.json')
    response.raise_for_status()
    data = json.loads(response.text)
    return data

'''
Phase 2: Algorithms
Condition 1: Pairs of 0
Input: Cell list of matrix
Output: String with response 'POSITIVE' or 'NEGATIVE'
'''

def pairs_of_zeros(data):
    list_cells = data['cells']
    total = len(list_cells) 
    pairs = 0
    
    for index in range(0, total, 2):
        if list_cells[index] == 0:
            pairs += 1
            
    if pairs > (total * 0.3):
        return 'POSITIVE'
    else:
        return 'NEGATIVE'
    
'''
Phase 2: Algorithms
Condition 2: Adjacent 1s
Input: Cell list of matrix
Output: String with response 'POSITIVE' or 'NEGATIVE'
'''

def adjacent_ones(data):
    list_cells = data['cells']
    total = len(list_cells) 
    adjacent = 0
    
    for index in range(0, total):
        ones = list_cells[index] == 1
        ones_left = (index > 0) and (list_cells[index - 1] == 1)
        ones_right = (index < total - 1) and (list_cells[index + 1] == 1)

        if ones and (ones_right or ones_left):
            adjacent += 1
            
    if adjacent > (total * 0.2):
        return 'POSITIVE'
    else:
        return 'NEGATIVE'