from utilities.parser import get_config, notification_settings, system_settings
from utilities.notifications import send_notifications
from utilities.miner import process_running
from utilities.system_checks import check_system

''' Program Functions. Do not change. '''
# Get Configuration miner_parameters
config = get_config()
notifications = notification_settings(config)
system_settings = system_settings(config)

def check_plotter():
    body = check_system(system_settings['cpu_high'], system_settings['cpu_low'], system_settings['ram_high'], system_settings['ram_low'])

    if body and process_running('powershell.exe'):
        send_notifications(notifications['system_webhook'],
                    '',
                    body,
                    '9f0100',
                    [])
    elif body == None and not process_running('powershell.exe'):
        send_notifications(notifications['system_webhook'],
                    '__**PLOT MANAGER HAS STOPPED RUNNING:**__',
                    'The PSChiaPlotter Plot manager has stopped. Please restart the program to resume plotting.',
                    '9f0100',
                    [])
    else:
        pass

if __name__ == "__main__":
    check_plotter()
