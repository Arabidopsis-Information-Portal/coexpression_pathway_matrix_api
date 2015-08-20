import urllib
import json
import re
import requests
import os.path
import os.path

# File root
BASE_URL = 'http://apps.araport.org/docs/matrix_app/'

def get_data(dtype,fname):
    """
    Retrieve the data
    """

    # Build path
    # example: https://apps.araport.org/docs/matrix_app/class/c5_genes_05.json
    FILENAME = BASE_URL + dtype + '/' +fname + '.json'
        
    json_data = requests.get(FILENAME).json()
    print json.dumps(json_data, indent=2)
        

    
    
