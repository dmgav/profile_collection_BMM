#####################################################################################
# This uses the drive tool (written in go) from https://github.com/odeke-em/drive   #
# and installed in $HOME/go/bin/                                                    #
#                                                                                   #
# This is an inelegant solution using a system call.  I could not make heads        #
# or tails out of Google's python API.                                              #
#                                                                                   #
# Until we have access to central stores here at BNL, this is ... good enough...    #
#####################################################################################
# Still need to manually grant access to the drive folder to each user, same for    #
# Slack.                                                                            #
#####################################################################################

import os, subprocess, shutil

from bluesky_queueserver.manager.profile_tools import set_user_ns

##from IPython import get_ipython
##user_ns = get_ipython().user_ns

gdrive_folder = os.path.join(os.environ['HOME'], 'gdrive')



@set_user_ns
def copy_to_gdrive(fname, *, user_ns):
    BMMuser = user_ns['BMMuser']
    user_gdrive_folder = os.path.join(gdrive_folder, 'Data', BMMuser.name, BMMuser.date)
    print(f'copying {fname} to {user_gdrive_folder}')
    shutil.copyfile(os.path.join(BMMuser.folder, fname), os.path.join(user_gdrive_folder, fname))
    return()

def synch_gdrive_folder(prefix=''):
    print(f'{prefix}updating {gdrive_folder}')
    here = os.getcwd()
    os.chdir(gdrive_folder)
    subprocess.run(['/home/xf06bm/go/bin/drive', 'push', '-quiet']) 
    os.chdir(here)
    return()

@set_user_ns
def make_gdrive_folder(prefix='', *, user_ns):
    BMMuser = user_ns['BMMuser']
    user_folder = os.path.join(gdrive_folder, 'Data', BMMuser.name, BMMuser.date)
    os.makedirs(user_folder, exist_ok=True)
    for f in ('dossier', 'prj', 'snapshots', 'XRF'):
        os.makedirs(os.path.join(user_folder, f), exist_ok=True)
    synch_gdrive_folder(prefix)
    return(user_folder)
