# CIFretriver
This python app retrieves data from the Materialproject API 
===========================================================
1. Make sure to get MP API KEY: https://materialsproject.org/open;
2. Install requirements with python -m pip install -r  requirements.txt
   or look at https://pymatgen.org/installation.html if you have aby installation issues or MacOS;
3. Run main.py module, it will require  the API KEY you've got and creates config.json file
   required for API authentification;
4. Insert "pretty formula" aka "SnO2" or "TiO2", then a query will be got;
5. You can save the query by the same name as 'pretty formula'.csv if you want, into 
    'csv_data_set_for_elements' directory that will be created or updated authomatically;
6. Then you cna insert a material_id, this will retrieve you the conventional standart structure
   cif file for requested material;
