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