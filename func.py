__author__ = 'O. Leiko'

from pymatgen import MPRester
import os
import json
import requests
from pymatgen.io.cif import CifWriter
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
#Takes a pymatgen.core.structure.Structure object and a symprec.
#  Uses spglib to perform various symmetry finding operations.

def writer():
    '''Writes correct API key into the config.json file'''
    
    with open('config.json', 'w') as t:
        new_key = input("Enter valid MP API key: ")
        key_string = "{" + '"API_KEY":' + f'"{new_key}"' + "}"
        t.write(key_string)
        print('New key is established!')
    

def check_api_key(validity=True):
    """
    Managing to write correct API_KEY into config.json file
    """
    
    if validity == True:        
        req = input('Any manipulations with config.file will erase it previous content!\nDo you want to proceed?\nY/N ')        
        if req.lower() == 'y': writer()
        else: exit()    
    else: writer()

def API_checker():
    with open('config.json') as t:
        # sets up API KEY and checks its validity 
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
       
        return header

def element_q(formula):
    mpr = MPRester(header['API_KEY'])
    results = mpr.query({'pretty_formula':"SiO2"}, properties=['material_id', 'pretty_formula'])




def conv_str_cif_retriever(material_id, header):

    mpr = MPRester(header['API_KEY'])
    structure = mpr.get_structure_by_material_id(f'mp-{material_id}')
    space_ga = SpacegroupAnalyzer(structure)
    conventional_structure = space_ga.get_conventional_standard_structure()
    write = CifWriter(conventional_structure)
    if not os.path.isdir('cif_files'):
        os.mkdir('cif_files')
    
    file_path = os.path.join('cif_files', f'mp-{material_id}_conventional_standart.cif')
    write.write_file(file_path)

if __name__ == "__main__":
    print(os.path.isdir('cif_files'))

