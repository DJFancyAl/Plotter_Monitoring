from utilities.parser import (
get_config, notification_settings, system_settings, plotter_settings)
from utilities.logs import plots_today, plots_yesterday
from utilities.miner import check_miner, process_running
from utilities.notifications import send_notifications
from utilities.plot_checks import get_running_plots


''' Program Functions. Do not change. '''
# Get Configuration miner_parameters
config = get_config()
notifications = notification_settings(config)
system_settings = system_settings(config)
plotter_settings = plotter_settings(config)


def check_plotter():
    plots = get_running_plots()

    if process_running('powershell.exe') and system_settings['always_notify']:
        send_notifications(notifications['plotter_webhook'],
                    '__**Plot manager is running.**__',
                    f'''{plots['plot_count']} plots are currently running.''',
                    '3aab59',
                    [['__**Plots:**__', f'''{plots_yesterday(plotter_settings['pslog_path'])} plots were completed yesterday.
{plots_today(plotter_settings['pslog_path'])} plots completed today.''']])
    # ['__**Plots:**__', f'''{plotter_settings['pslog_path'])} plots were completed yesterday.
    elif check_manager() and not system_settings['always_notify']:
        pass
    else:
        send_notifications(notifications['system_webhook'],
                    '__**PLOT MANAGER IS NOT RUNNING.**__',
                    'Restart the manager to resume plotting.',
                    '9f0100',
                    [])


if __name__ == "__main__":
    check_plotter()
