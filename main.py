__author__ = "O. Leiko"

import os 
from utilities import Retriever
import logging.config


if 'config.json' not in os.listdir():
    # create config file if it is not in directory
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger()
    logger.info("creating config.json file \n")
    open('config.json', 'a').close()

reqs = Retriever() #create retriever object

nice_formula = input('Enter pretty formula (like SnO2): ')

reqs.element_q(nice_formula) #retrieving structure query

mat_id = input("Enter material id: ")

reqs.conv_str_cif_retriever(mat_id) # retrieve and save as .cif file required structure

reqs.get_bandstructure(mat_id)


