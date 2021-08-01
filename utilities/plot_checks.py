import re
import psutil

# Contains functions for monitoring the running plots.
def get_chia_executable_name():
    return f'chia{".exe"}'


def _contains_in_list(string, lst, case_insensitive=False):
    if case_insensitive:
        string = string.lower()
    for item in lst:
        if case_insensitive:
            item = item.lower()
        if string not in item:
            continue
        return True
    return False


def get_manager_processes():
    processes = []
    for process in psutil.process_iter():
        try:
            if not re.search(r'^pythonw?(?:\d+\.\d+|\d+)?(?:\.exe)?$', process.name(), flags=re.I):
                continue
            if not _contains_in_list('python', process.cmdline(), case_insensitive=True) or \
                    not _contains_in_list('stateless-manager.py', process.cmdline()):
                continue
            processes.append(process)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return processes


def get_running_plots():
    chia_processes = []
    chia_executable_name = get_chia_executable_name()
    for process in psutil.process_iter():
        try:
            if chia_executable_name not in process.name() and 'python' not in process.name().lower():
                continue
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
        try:
            if 'plots' not in process.cmdline() or 'create' not in process.cmdline():
                continue
        except (psutil.ZombieProcess, psutil.NoSuchProcess):
            continue
        if process.parent():
            try:
                parent_commands = process.parent().cmdline()
                if 'plots' in parent_commands and 'create' in parent_commands:
                    continue
            except (psutil.AccessDenied, psutil.ZombieProcess):
                pass
        chia_processes.append([process])

    running_plots = {
        'plot_count': len(chia_processes)
    }
    return running_plots
