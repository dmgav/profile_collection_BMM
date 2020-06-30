
DATA = os.path.join(os.getenv('HOME'), 'Data', 'bucket') + '/'

from BMM.functions           import now, colored, run_report, boxedtext
from BMM.functions           import error_msg, warning_msg, go_msg, url_msg, bold_msg, verbosebold_msg, list_msg, disconnected_msg, info_msg, whisper
run_report('\tlogging')
from BMM.logging             import report, BMM_log_info, BMM_msg_hook


run_report('\tuser')
from BMM.user import BMM_User
run_report('\tdetector ROIs')
from BMM.referencefoils import ReferenceFoils
foils = ReferenceFoils()
run_report('\treference foils')
from BMM.rois import ROI
rois = ROI()


BMMuser = BMM_User()
BMMuser.start_experiment_from_serialization()

if BMMuser.pds_mode is None:
    try:                        # do the right then when "%run -i"-ed
        BMMuser.pds_mode = get_mode()
    except:                     # else wait until later to set this correctly, get_mode() defined in 74-mode.py
        pass
## some backwards compatibility....
whoami           = BMMuser.show_experiment()
start_experiment = BMMuser.start_experiment
end_experiment   = BMMuser.end_experiment

run_report('\tmirror trigonometry')
from BMM.mirror_trigonometry import move_m2, move_m3









RE.msg_hook = BMM_msg_hook