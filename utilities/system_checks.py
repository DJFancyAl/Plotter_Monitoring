import psutil
import socket

def check_system(cpu_high, cpu_low, ram_high, ram_low):
    cpu_percent = psutil.cpu_percent(2)
    ram_usage = psutil.virtual_memory()

    if cpu_percent>cpu_high and ram_usage.percent>ram_high:
        return f'''__**High CPU and RAM Usage detected. Resolve issue immediately.**__

CPU Usage: {cpu_percent}%
RAM Usage: {ram_usage.percent}%'''
    elif cpu_percent>cpu_high and ram_usage.percent<ram_high:
        return f'''__**High CPU Usage detected. Check for problems.**__

CPU Usage: {cpu_percent}%
RAM Usage: {ram_usage.percent}%'''
    elif cpu_percent<cpu_high and ram_usage.percent>ram_high:
        return f'''__**High RAM Usage detected. Check for problems.**__

CPU Usage: {cpu_percent}%
RAM Usage: {ram_usage.percent}%'''
    elif cpu_percent<cpu_low or ram_usage.percent<ram_low:
        return f'''__**Low CPU or RAM usage. Plotter has stopped or plotting has completed.**__

CPU Usage: {cpu_percent}%
RAM Usage: {ram_usage.percent}%'''
    else:
        pass
