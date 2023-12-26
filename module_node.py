import subprocess
import time
'''
Function to get the information of empty nodes
1. use 'sinfo' command to get the information of nodes(using subprocess)
2. parse the information
3. return the list of empty nodes
'''
def get_empty_nodes():
    # 1. use 'sinfo' command to get the information of nodes(using subprocess)
    sinfo = subprocess.Popen(['sinfo'], stdout=subprocess.PIPE)
    sinfo_out, sinfo_err = sinfo.communicate()
    sinfo_out = sinfo_out.decode('utf-8').split('\n')
    sinfo_out = sinfo_out[1:-1]

    # 2. parse the information
    empty_nodes = []
    for line in sinfo_out:
        line = line.split()
        if line[4] == 'idle':
            empty_nodes.append(line[0])

    # 3. return the list of empty nodes
    return empty_nodes

def wait_for_job(job_id):
    while True:
        result = subprocess.run(['squeue', '-j', str(job_id)], stdout=subprocess.PIPE)
        if str(job_id) not in result.stdout.decode('utf-8'):
            break
        time.sleep(60)  # wait for 60 seconds before checking again
    
if __name__ == '__main__':
    # test get_empty_nodes()
    print(get_empty_nodes())
    wait_for_job(13120)