

def check_api_key(validity=True):
    """
    Managing to write correct API_KEY into config.json file
    """
    def writer():
        with open('config.json', 'w') as t:
            new_key = input("Enter valid MP API key: ")
            key_string = "{" + '"API_KEY":' + f'"{new_key}"' + "}"
            t.write(key_string)
            print('New key is established, rerun script')
    
    if validity == True:        
        req = input('Any manipulations with config.file will erase it previous content!\nDo you want to proceed?\nY/N ')
        
        if req.lower() == 'y': writer()
        else: exit()
    
    else: writer()

