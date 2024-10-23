import pandas as pd

pl_hosts = pd.read_csv('final_planethost_list.txt', comment='#', names=['star'], dtype={'star':str})
singles = pd.read_csv('final_singles_list.txt', comment='#', names=['star'], dtype={'star':str})
binaries = pd.read_csv('final_binaries_list.txt', comment='#', names=['star'], dtype={'star':str})

def missing_stars():
    missing = []
    for starname in pl_hosts['star'].values:
        if starname in singles['star'].values:
            print('{} is a single star'.format(starname))
        elif starname in binaries['star'].values:
            print('{} is a binary star'.format(starname))
        else:
            print('{} is missing from the singles and binaries lists'.format(starname))
            missing += [starname]
    return missing
