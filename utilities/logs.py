from utilities.parser import get_config, miner_settings
from utilities.miner import check_balance
import logging
import re
import os
from datetime import date, timedelta


''' Program Functions. Do not change. '''
def plots_today(log_path):
    plot_count = 0
    logs = []
    correct_day = str(date.today().strftime("%a %b %d"))
    correct_day = correct_day.replace('01',' 1').replace('02',' 2').replace('03',' 3').replace('04',' 4').replace('05',' 5').replace('06',' 6').replace('07',' 7').replace('08',' 8').replace('09',' 9')
    current = str(date.today()).replace('-','_')
    yesterday = str(date.today() - timedelta(days = 1)).replace('-','_')

    for log in os.listdir(log_path):
        today = re.search(current, log)
        day_before = re.search(yesterday, log)

        if today or day_before:
            logs.append(log)

    for log in logs:
        with open(log_path + '\\' + log,'r') as reader:
            lines = reader.readlines()

        complete_plot = re.search('Renamed final file from', lines[-1])
        right_day = re.search(correct_day, lines[-3])

        if complete_plot and right_day:
            plot_count += 1

    return plot_count


def plots_yesterday(log_path):
    plot_count = 0
    logs = []
    yesterday = str(date.today() - timedelta(days = 1)).replace('-','_')
    yesterday2 = str(date.today() - timedelta(days = 2)).replace('-','_')
    correct_day = str((date.today() - timedelta(days = 1)).strftime("%a %b %d"))
    correct_day = correct_day.replace('01',' 1').replace('02',' 2').replace('03',' 3').replace('04',' 4').replace('05',' 5').replace('06',' 6').replace('07',' 7').replace('08',' 8').replace('09',' 9')

    for log in os.listdir(log_path):
        day = re.search(yesterday, log)
        day2 = re.search(yesterday2, log)

        if day or day2:
          logs.append(log)

    for log in logs:
        with open(log_path + '\\' + log,'r') as reader:
            lines = reader.readlines()

        complete_plot = re.search('Renamed final file from', lines[-1])
        right_day = re.search(correct_day, lines[-3])

        if complete_plot and right_day:
            plot_count += 1

    return plot_count


def old_balance(path):
    log_path = path + "\\logs\\balance.log"
    logging.basicConfig(filename=log_path,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filemode='a')
    logger=logging.getLogger()

    with open(log_path,'r') as reader:
        line = reader.readlines()[-1]

    old_balance = re.findall('Chia Balance: (\d*\.\d*)', line)
    return old_balance[0]

def compare_chia(new_balance, old_balance):
    if float(new_balance) > float(old_balance):
         return True
    return False


def update_log(log_path, chia_balance):
    logging.basicConfig(filename=log_path + "\\logs\\balance.log",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filemode='a')
    logger=logging.getLogger()

    logger.setLevel(logging.INFO)
    logger.info('Chia Balance: ' + chia_balance)
