__author__ = 'O. Leiko'

from pymatgen import MPRester
import os
import json
import requests
import pandas as pd
from pymatgen.io.cif import CifWriter
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
#Takes a pymatgen.core.structure.Structure object and a symprec.
#  Uses spglib to perform various symmetry finding operations.

class Retriever:
    def __init__(self): 

        header = self.API_checker()
        self.mpr = MPRester(header['API_KEY'])
        
    
    def writer(self):
        '''Writes correct API key into the config.json file'''
        
        with open('config.json', 'w') as t:
            new_key = input("Enter valid MP API key: ")
            key_string = "{" + '"API_KEY":' + f'"{new_key}"' + "}"
            t.write(key_string)
            print('New key is established!\nRe-run code plz..') 

    def check_api_key(self, validity=True):
        """
        Managing to write correct API_KEY into config.json file
        """
        
        if validity == True:        
            req = input('Any manipulations with config.file will erase it previous content!\nDo you want to proceed?\nY/N ')        
            if req.lower() == 'y': self.writer()
            else: exit()    
        else: self.writer()

    def API_checker(self):
        with open('config.json') as t:
            # sets up API KEY and checks its validity 
            try:
                header = json.load(t)
                if not type(header) == dict:
                    raise TypeError 
                test = requests.get('https://www.materialsproject.org/rest/v2/api_check', header)
                if not test.json()['response']['api_key_valid']:
                    print('Invalid MP API KEY')
                    self.check_api_key(validity=False)
                    exit()
            except (TypeError, json.decoder.JSONDecodeError):
                print('Make sure you provided correct API and config.json file')
                self.check_api_key()
                exit()       
        
            return header

    def element_q(self, formula):

        results = self.mpr.query({'pretty_formula':f"{formula}"}, properties=['material_id', 'pretty_formula', 'spacegroup.crystal_system', 'spacegroup.symbol'])
        df=pd.DataFrame.from_records(results)
        print(df)
        save = input('Do you want to save query to .csv file? Y/N ')
        

        if save.lower() == 'y':
            if not os.path.isdir('csv_data_set_for_elements'):
                os.mkdir('csv_data_set_for_elements')
            path_file = os.path.join('csv_data_set_for_elements', f'{formula}.csv')
            df.to_csv(path_file)


        #df.to_csv(f'{file_name}.csv')
        #for r in results[0:5]:
        #    print(r)



    def conv_str_cif_retriever(self, material_id):

        structure = self.mpr.get_structure_by_material_id(f'{material_id}')
        space_ga = SpacegroupAnalyzer(structure)
        conventional_structure = space_ga.get_conventional_standard_structure()
        write = CifWriter(conventional_structure)
        if not os.path.isdir('cif_files'):
            os.mkdir('cif_files')
        
        file_path = os.path.join('cif_files', f'{material_id}_conventional_standart.cif')
        write.write_file(file_path)

    if __name__ == "__main__":
        print(os.path.isdir('cif_files'))

