'''
Total Automation code for the spinner
'''

import os
import shutil
import yaml
import sys
import argparse
from datetime import datetime

from initialize import initialize
from module_log import log_writer

from module_md import set_md, do_md

# read parameters
parameters = yaml.safe_load(open('parameters.yaml', 'r'))

## 0. Init Settings
material_name = parameters['material']
proceed_init = parameters['init']['proceed']

## 1. MD Settings
proceed_md = parameters['md']['proceed']
premelt = parameters['md']['premelt']
convergence_test = parameters['md']['convergence_test']
find_Tm = parameters['md']['find_Tm']
melt = parameters['md']['melt']
quench = parameters['md']['quench']
anneal = parameters['md']['anneal']

## 2. NNP Settings
proceed_nnp = True

## 3. SPINNER Settings
proceed_spinner = True

## Path settings
if parameters['paths']['base_path']:
    base_path = parameters['paths']['base_path']
else:
    base_path = os.getcwd()
md_src_path = parameters['paths']['md_src_path']



##################################################################################################################
if __name__ == '__main__':
    # 1. Initialize the project
    if proceed_init:
        initialize(material_name, base_path)
    

    # 2. do MD
    if proceed_md:
        set_md(material_name, base_path)
        do_md(material_name, base_path, md_src_path)
        

    # 3. do NNP
    if proceed_nnp:
        log_writer('NNP is started.\n', base_path)
        log_writer('NNP is done.\n', base_path)

    # 4. do SPINNER

    # 5. do AMP