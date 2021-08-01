from utilities.parser import get_config, notification_settings, miner_settings
from utilities.logs import plots_today, plots_yesterday, old_balance, compare_chia, update_log
from utilities.miner import process_running, check_miner, check_balance, check_farm
from utilities.notifications import send_notifications
import os


''' Program Functions. Do not change. '''
# Get Configuration miner_parameters
config = get_config()
notifications = notification_settings(config)
miner_settings = miner_settings(config)
current_path = os.path.dirname(__file__)


def check_miners():
    check_chia = process_running('Chia')
    chia_balance = check_balance(miner_settings['chia_path'])
    previous_balance = old_balance(current_path)
    farm = check_farm(miner_settings['chia_path'])
    farm_size = float(farm[1])


    if miner_settings['always_notify'] and check_chia:
        send_notifications(notifications['miner_webhook_true'],
                    'LOOKS GOOD!',
                    'Miner is running.',
                    '3aab59',
                    [['__**CHIA BLOCKCHAIN RUNNING:**__', f'''{farm[0]}'''], ['__**TOTALS:**__', f'''Farm capacity: {farm_size:.2f} TiB
{'NEW COIN IN WALLET!!! Balance = ' if compare_chia(chia_balance, previous_balance) else 'Chia Balance = '}{chia_balance} xch''']])
    elif not check_chia:
        send_notifications(notifications['miner_webhook_false'],
                    '**CHIA BLOCKCHAIN IS NOT RUNNING.**',
                    'Restart the Chia process to resume mining.The HPOOL miner is still online.',
                    '9f0100',
                    [])
    else:
        pass

    update_log(current_path, chia_balance)


if __name__ == "__main__":
    check_miners()
