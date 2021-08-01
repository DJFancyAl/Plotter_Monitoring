import re
import psutil
import os
from subprocess import check_output
from datetime import date, timedelta


''' Program Functions. Do not change. '''
def process_running(processName):
    processes = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName in proc.name():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def check_miner(path):
    log_path = f'{path}\\windows\\log\\'
    log_date = (str(date.today())).replace('-', '')
    log_last = (str(date.today() - timedelta(days = 1))).replace('-', '')
    suffix = re.findall(r"(\d\d)$", log_date)
    last_suffix = re.findall(r"(\d\d)$", log_last)
    current_log = log_path + "miner.log-" + log_date + "-" + suffix[0] + ".log"
    last_log = log_path + "miner.log-" + log_last + "-" + last_suffix[0] + ".log"

    try:
        with open(current_log,'r') as reader:
            last_line = reader.readlines()[-1]
    except:
        with open(last_log,'r') as reader:
            last_line = reader.readlines()[-1]

    capacity = re.findall(r"capacity=\"(\d*\.\d*) TB\" file", last_line)

    return capacity[0]

def check_balance(directory):
    command = r".\chia.exe wallet show"

    os.chdir(directory)
    wallet = check_output(command)
    try:
        chia = re.findall(r'\-Total Balance: (\d*\.\d*) xch', str(wallet))
        return chia[0]
    except:
        return 0


def check_farm(directory):
    command = r".\chia.exe farm summary"

    os.chdir(directory)
    try:
        farm = check_output(command)
    except:
        farm = 0
    # chia = re.findall(r'\-Total Balance: (\d*\.\d*) xch', str(wallet))
    plot_count = re.findall(r'(Plot count for all harvesters: \d*)', str(farm))
    total_size = re.findall(r'Total size of plots: (\d*\.\d*) \w*', str(farm))

    return [plot_count[0], total_size[0]]
