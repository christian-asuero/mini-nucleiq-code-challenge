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