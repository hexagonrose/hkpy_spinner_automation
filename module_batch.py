'''
Module for writing/modifying batch files
Use SLURM commands
'''

import os
from module_node import get_empty_nodes

cores_per_node_odin = {
    'csc1' : 16,
    'csc2' : 32,
    'loki1' : 16,
    'loki2' : 20,
    'loki3' : 24,
    'loki4' : 28,
    'gpul'  : 28
}

def write_batchfile_4_md_odin(material, base_path, md_src, node=1, time='04-00:00'):
    # 1. Get into the 1_MD folder
    os.chdir(f'{base_path}/{material}/1_MD')
    # 2. get empty nodes
    empty_nodes = get_empty_nodes()

    # 3. Write the batch file
    with open('run_md.sh', 'w') as file:
        file.write(f'''#!/bin/bash 
#SBATCH --nodes={node}
#SBATCH --partition={empty_nodes[-1]}
#SBATCH --ntasks={cores_per_node_odin[empty_nodes[-1]]}
#SBATCH --job-name=MD_{material}
#SBATCH --time={time}
#SBATCH --output=STDOUT.%N.%j.out
#SBATCH --error=STDERR.%N.%j.err 


md_path={md_src}
python3 $md_path/main.py configure_test.yaml $SLURM_NTASKS
''')
        
if __name__ == '__main__':
    material = 'Na3P1S4'
    base_path = os.getcwd()
    md_src = '/data/haekwan98/python_spinner_auto_hk/md_src'
    write_batchfile_4_md_odin(material, base_path, md_src, node=1, time='04-00:00')
