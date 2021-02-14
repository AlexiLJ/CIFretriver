__author__ = "O. Leiko"

import os 
from utilities import Retriever
from pymatgen.electronic_structure.plotter import BSPlotter

if 'config.json' not in os.listdir():
    # create config file if it is not in directory
    open('config.json', 'a').close()

reqs = Retriever() #create retriever object

nice_formula = input('Enter pretty formula (like SnO2): ')

reqs.element_q(nice_formula) #retrieving structure query

mat_id = input("Enter material id: ")

reqs.conv_str_cif_retriever(mat_id) # retrieve and save as .cif file required structure


# bs = mpr.get_bandstructure_by_material_id('mp-' + mat_id)
# print(f'Band gap info {bs.get_band_gap()}')
# BSPlotter(bs).show()

