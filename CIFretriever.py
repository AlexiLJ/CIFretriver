__author__ = "O. Leiko"

from pymatgen import MPRester
import os 
import json
import requests
from errors import check_api_key
from pymatgen.io.cif import CifWriter

from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
#Takes a pymatgen.core.structure.Structure object and a symprec.
#  Uses spglib to perform various symmetry finding operations.

from pymatgen.electronic_structure.plotter import BSPlotter

if 'config.json' not in os.listdir():
    # create config file if it is not in directory
    open('config.json', 'a').close()

with open('config.json') as t:
    # set up API KEY and checks its validity 
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

mpr = MPRester(header['API_KEY'])

mat_id = input("Enter material id: mp-")
structure = mpr.get_structure_by_material_id(f'mp-{mat_id}')
space_ga = SpacegroupAnalyzer(structure)
conventional_structure = space_ga.get_conventional_standard_structure()

w = CifWriter(conventional_structure)
w.write_file(f'mp-{mat_id}_conventional_standart.cif')



'''
MP_ID = 'mp-19017'

bs = mpr.get_bandstructure_by_material_id(MP_ID)
print(f'Band gap info {bs.get_band_gap()}')
BSPlotter(bs).show()
'''
# print(header)
# response = requests.get('https://www.materialsproject.org/rest/v2/materials/Fe2O3/vasp', header)
# data=response.json()
#print(data)
'''
    results = mpr.query({'pretty_formula':"SiO2"}, properties=['material_id', 'pretty_formula'])
    print(results)
'''