__author__ = "O. Leiko"

import os 
from func import Retriever
from pymatgen.electronic_structure.plotter import BSPlotter

if 'config.json' not in os.listdir():
    # create config file if it is not in directory
    open('config.json', 'a').close()

reqs = Retriever()

nice_formula = input('Enter nice formula (like SnO2): ')
reqs.element_q(nice_formula)
#print(req.mpr)
mat_id = input("Enter material id: ")

reqs.conv_str_cif_retriever(mat_id)


# bs = mpr.get_bandstructure_by_material_id('mp-' + mat_id)
# print(f'Band gap info {bs.get_band_gap()}')
# BSPlotter(bs).show()


# print(header)
# response = requests.get('https://www.materialsproject.org/rest/v2/materials/Fe2O3/vasp', header)
# data=response.json()
#print(data)
'''
    results = mpr.query({'pretty_formula':"SiO2"}, properties=['material_id', 'pretty_formula'])
    print(results)
'''