import os
import yaml
import subprocess
from module_batch import write_batchfile_4_md_odin
from module_node import wait_for_job
from module_log import log_writer

def set_md(material, base_path, premelt=True, convergence_test=True, find_Tm=True, melt=True, quench=True, anneal=True):
    # 1. Get into the 1_MD folder
    os.chdir(f'{base_path}/{material}/1_MD')

    # 2. Modify configure_test.yaml
    with open('configure_test.yaml', 'r') as file:
        config = yaml.safe_load(file)

        # 2-1. Modify the steps to proceed
        config['Actions']['premelt'] = premelt
        config['Actions']['convergence_test'] = convergence_test
        config['Actions']['find_Tm'] = find_Tm
        config['Actions']['melt'] = melt
        config['Actions']['quench'] = quench
        config['Actions']['anneal'] = anneal

        # 2-2. Modify the material name
        config['composition'] = material

    with open('configure_test.yaml', 'w') as file:
        yaml.dump(config, file)
    
    log_writer('MD is set.\n', f'{base_path}/{material}')

def do_md(material, base_path, md_src):
    # 1. write batch file for MD
    write_batchfile_4_md_odin(material, base_path, md_src, node=1, time='04-00:00')

    # 2. run MD and wait!
    result = subprocess.run(['sbatch', 'run_md.sh'], stdout=subprocess.PIPE)
    job_id = int(result.stdout.decode('utf-8').split()[-1])
    wait_for_job(job_id)
    
if __name__ == '__main__':
    set_md('Na3P1S4', os.getcwd(), premelt=False)