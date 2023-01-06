# Plotter Monitoring

## Description

This tool is designed for use with __Chia__ cryptocurrency mining setups and is useful for anywone who is Plotting and/or mining Chia currency.

The __"Plotter Monitoring"__ package is a set of tools which can be used to monitor the machine which is creating Chia "Plots" and farming Chia. The package includes several tools including:

* System Monitoring
* Plotter Monitoring
* Miner Monitoring

We'll describe each of these tools below, as well as how to configure them.

## Usage



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
