import urllib
import json
import re
import requests
import os.path
import os.path

# File root
BASE_URL = 'http://apps.araport.org/docs/matrix_app/'

def get_data(dtype,fname,fthreshold):
    """
    Retrieve the data
    """

    d_threshold=''
    j_name=''
    if fthreshold == 0.5:
        d_threshold = 'f05'
        j_name = fname + '_genes_05.json'
    elif fthreshold == 0.75:
        d_threshold = 'f075'
        j_name = fname + '_genes_075.json'
        
    # Build path
    # example: https://apps.araport.org/docs/matrix_app/class/c5_genes_05.json
    # example: https://apps.araport.org/docs/matrix_app/subclass/sc5_genes_05.json
    # example: https://apps.araport.org/docs/matrix_app/pathways/kp04626_genes_05.json
    JURL = BASE_URL + dtype + '/' + d_threshold + '/' + j_name;

    json_data = requests.get(JURL).json()
    print json.dumps(json_data, indent=2)
        

    
    
