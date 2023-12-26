import yaml


def generate_yaml_file_4_md(filepath, actions, composition, pot_dir, gam, mpicommand, npar, std):
    data = {
      'Actions': actions,
      'composition': composition,
      'pot_dir': pot_dir,
      'vasp_config': {
        'gam': gam,
        'mpicommand': mpicommand,
        'npar': npar,
        'std': std
      }
    }

    with open(filepath, 'w') as file:
      yaml.dump(data, file)

# Example usage
if __name__ == '__main__':
    actions = {
    'anneal': True,
    'convergence_test': True,
    'find_Tm': True,
    'melt': True,
    'premelt': True,
    'quench': True
    }
    composition = 'Na3P1S4'
    pot_dir = '/data/vasp4us/pot/PBE54/'
    gam = '/data/vasp4us/vasp6/loki_6.2.0/vasp_gam'
    mpicommand = 'mpirun'
    npar = 4
    std = '/data/vasp4us/vasp6/loki_6.2.0/vasp_std'

