#from pymatgen import MPRester
import os 
import json
import requests
from errors import check_api_key
#with MPRester() as mpr:
    # You can pass in a formula to get_materials_ids
    # print(mpr.get_structure_from_mp('SnO2'))  #mpr.get_materials_ids("LiFePO4"), mpr.get_pretty_formula("LiFePO4"))

if 'config.json' not in os.listdir():
    # create config file if it is not in directory
    open('config.json', 'a').close()

with open('config.json') as t:
    # set up API KEY
    try:
        header = json.load(t)
        if not type(header) == dict:
            raise TypeError 

        test = requests.get('https://www.materialsproject.org/rest/v2/api_check', header)
        
        if not test.json()['response']['api_key_valid']:
            print('Invalid MP API KEY')
            check_api_key(validity=False)
        
    except (TypeError, json.decoder.JSONDecodeError):
        print('Make sure you provided correct API and config.json file')
        check_api_key()
        exit()



print(header)
response = requests.get('https://www.materialsproject.org/rest/v2/materials/Fe2O3/vasp', header)
data=response.json()
#print(data)
'''
    results = mpr.query({'pretty_formula':"SiO2"}, properties=['material_id', 'pretty_formula'])
    print(results)
'''