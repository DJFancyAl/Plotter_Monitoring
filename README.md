# Plotter Monitoring

## Description

This tool is designed for use with __Chia__ cryptocurrency mining setups and is useful for anywone who is Plotting and/or mining Chia currency.

The __"Plotter Monitoring"__ package is a set of tools which can be used to monitor the machine which is creating Chia "Plots" and farming Chia. The package includes several tools including:

* System Monitoring
* Plotter Monitoring
* Miner Monitoring

We'll describe each of these tools below, as well as how to configure them.

## Usage

This toolkit has been designed to be used to suit the needs of the individual user. The user can use any of the tools below as often or inoften as they would like to suit their needs. They may choose to not use the tools at all - especially after the plotting process has completed. To avoid using machine resources, especially during the plotting process, the __"Plotter Monitoring"__ package does not require a process to always be running.

The user should use _Windows task manager_ (or a similar scheduling application) to run each of the tools below on a schedule. Using this method allows you to schedule each tool to run hourly, daily, weekly, or on any other cycle you choose!

## Tools

### 1. System Monitoring

Creating Chia "Plots" is a time consuming process which requires a lot of computer resources. Optimizing the plotting process requires the machine to use as much of these resources as possible, however we want to avoid overworking the system and causing a crash at all costs. Also, any significant increases or decreases in computer resources could be indicitive of another issue, such as the plotting application has stopped working.

This tool uses _psutil_ to check the CPU and RAM usage of the plotting machine and compares them against high and low values (as set by the user). If either the CPU or RAM useage exceeds these thresholds then the user were be notified through Discord to take action.

### 2. Plotter Monitoring

Creating a Chia plot can take hours or even days to complete. If creation of a plot fails, then the plotting process needs to be restarted from the beginning. Additionally, if the plotting process is not running, then time is wasted in an effort to build the Chia farm.

This tool checks to see if the plotting process is still running on the machine. If the plotting process is stopped then it will notify the user through Discord to take action. If the plotting process is running, then the user may be notified with the value of plots that have been completed yesterday and today.

### 3. Miner Monitoring

Once a Chia farm has been created through plotting - then mining may begin. Mining requires the Chia blockchain to be running constantly to earn that precious, valuable* Chia coin. If the Chia blockchain stops running then mining will stop and time earning coin will be wasted.

This tool looks to see if the Chia blockchain is running. If the blockchain is not running then the user is notified through Discord to take action and restart the blockchain process. If the block chain is running, then the blockchain is running, then the user may be notified with some useful data including:

* Total plot count
* Total size of plots
* Total farm capacity
* Total balance of XCH Chia coin
* If new Chia coin has been added to the wallet

## Configuration

The __Plotter Monitor__ package requires some basic configuration to work for the individual user. Additionally, it provides some options that customize the usage of tools. Settings and configuration are handled in a _config.yaml_ file. To create this file - copy the _config.yaml.default_ file and then rename it to _config.yaml_ for user configuration. *DO NOT MAKE CHANGES TO THE DEFAULT FILE. ONLY MAKE CHANGES TO YOUR NEW CONFIG FILE*

Once you have created the new configuration file, you may begin changing parameters to suit your needs. Here are descriptions of the necessary and unnecessary parameters:

### Notifications

Notifications are sent to Discord webhooks. You may use the same webhook for multiple parameters, or different ones based on how you would like notifications delivered.

* __system_webhook__ - The Discord webhook where notifications where "System Monitoring" notifications will sent.
* __plotter_webhook__ - The Discord webhook where notifications where "Plotter Monitoring" notifications will sent.
* __miner_webhook_true__ - The Discord webhook where notifications where "Miner Monitoring" notifications will sent if recurring notifications are set.
* __miner_webhook_false__ - The Discord webhook where notifications where "Miner Monitoring" notifications will sent only if the miner is not running.

### System Parameters

Use these settings to confugire how the system monitor runs. You may need to change these parameters several times to find the threshhold which works best for you.

* __always_notify__ - If False - it will only notify the plot manager is not running or a threshhold is broken.
* __cpu_high__ - Will notify if it exceeds this threshhold (in percent)
* __cpu_low__ - Will notify if below this threshhold (in percent)
* __ram_high__ - Will notify if it exceeds this threshhold (in percent)
* __ram_low__ - Will notify if below this threshhold (in percent)

### Plotting Parameters

Use this setting to configure how the plotter monitor runs.

* __pslog_path__ - The folder where the PSChiaPlotter logs are located - __MUST BE SET.__  Example: _C:\Users\CurrentUser\.chia\mainnet\plotter_

### Miner Parameters

Use these settings to configure how the miner monitor runs.

* __always_notify__ - If False - it will only notify if a mining process is not running.
* __hpool_path__ - The folder where your HPOOL Miner is located. - __MUST BE SET.__ Example: _C:\Users\CurrentUser\Documents\HPool-Miner-chia-v1.4.1-0-windows_
* __chia_path__ - The folder where your Chia.exe is located. - __MUST BE SET.__ Example: _C:\Users\CurrentUser\AppData\Local\chia-blockchain\app-1.2.2\resources\app.asar.unpacked\daemon_
