import pathlib
import os
import yaml

def get_config():
    directory = pathlib.Path().resolve()
    file_name = 'config.yaml'
    file_path = os.path.join(directory, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Unable to find the config.yaml file. Expected location: {file_path}")
    f = open(file_path, 'r')
    config = yaml.load(stream=f, Loader=yaml.Loader)
    f.close()
    return config


def notification_settings(config):
    notifications = config.get('notifications', None)
    return notifications


def system_settings(config):
    system_settings = config.get('system_parameters', None)
    return system_settings


def plotter_settings(config):
    plotter_settings = config.get('plotting_parameters', None)
    return plotter_settings


def miner_settings(config):
    miner_settings = config.get('miner_parameters', None)
    return miner_settings
