# Description

Python script that connects to chosen Kasa smart plug and turns it on and off depending on your device's battery level. If battery level drops below the lower limit, it turns the plug on and turns it off if it reaches the upper limit. 

It is intended to keep your device's battery level between a bounded range for optimal battery health.

# Usage

```
python main.py -p <plug_alias> [-l LOWER_LIMIT] [-u UPPER_LIMIT]
```

**Required Arguments:**

`-p PLUG_ALIAS, --plug PLUG_ALIAS` - The alias of the smart plug to control.

**Optional Arguments:** 

`-l LOWER_LIMIT, --lower-limit LOWER_LIMIT` - The battery percentage that will turn the plug on. Default is 30.

`-u UPPER_LIMIT, --upper-limit UPPER_LIMIT` - The battery percentage that will turn the plug off. Default is 80.


**Example:**

```
python main.py -p mac_plug
```

This will control the smart plug with alias "mac_plug", turning it on when the battery drops below 30% and off above 80%.


To customize the thresholds:

```
python main.py -p mac_plug -l 20 -u 90 
```

Now mac_plug will turn on at 20% and off at 90%.

The program runs continuously monitoring the battery. Press Ctrl+C to exit.

## Running in Background

To run the program in the background:

```
nohup python main.py -p mac_plug &
```

This will run it in the background and continue executing even after disconnecting from the terminal session it was started on.

## Stopping the Background Process

First, check for the process ID (PID) of the background program:

```
ps aux | grep python
```

This will list all running python processes. Find the PID of the target process.

Then kill it by PID:

```
kill <PID>
```