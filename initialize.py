import os
import shutil
from datetime import datetime
from module_log import log_writer

'''
Initializing the project
making necessary folders and files
Folder hierarchy:
    Material_name(ex: Na3P1S4)
        1_MD
        2_NNP
        3_SPINNER
        4_AMP
        5_SCAN
'''

def initialize(material_name, base_path=os.getcwd()):
    
    # get the base path
    base_path = os.getcwd()

    # Check if the folder already exists
    if os.path.exists(material_name):
        print(f"Folder '{material_name}' already exists. Ending the function.")
        return

    # Get the current time
    now = datetime.now()
    now_str = now.strftime('%y%m%d_%H%M%S')

    # Make the folder
    os.mkdir(material_name)
    os.chdir(material_name)
    log_writer('Initialization is started.\n', f'{base_path}/{material_name}', mode='w')
    # copy necessary files
    copy_files(material_name, base_path)

    log_writer('Initialization is done.\n', f'{base_path}/{material_name}')

   
def copy_files(material_name, base_path):
    files4md_path = f'{base_path}/files/files4md'
    files4nnp_path = f'{base_path}/files/files4nnp'
    files4spinner_path = f'{base_path}/files/files4spinner'
    files4amp_path = f'{base_path}/files/files4amp'

    md_target_path = f'{base_path}/{material_name}/1_MD'
    nnp_target_path = f'{base_path}/{material_name}/2_NNP'
    spinner_target_path = f'{base_path}/{material_name}/3_SPINNER'
    amp_target_path = f'{base_path}/{material_name}/4_AMP'

    shutil.copytree(files4md_path, md_target_path)
    shutil.copytree(files4nnp_path, nnp_target_path)
    shutil.copytree(files4spinner_path, spinner_target_path)
    shutil.copytree(files4amp_path, amp_target_path)
    
    
if __name__ == '__main__':
    initialize('Na3P1S4')