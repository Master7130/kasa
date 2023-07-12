import sys
import signal
import argparse
import time
import psutil
import asyncio
from kasa import Discover, SmartPlug
from yaspin import yaspin

def signal_handler(sig, frame):
    print('\nTerminating program.')
    sys.exit(0)

def check_battery(lower_lim, upper_lim):
    battery = psutil.sensors_battery()
    level = int(battery.percent)

    if (level >= upper_lim):
        return "X"
    elif (level <= lower_lim):
        return "O"
    else:
        return "X"
    
async def find_plug(alias):
    devices = await Discover.discover()

    for addr, dev in devices.items():
        if dev.alias == alias:
            return addr
        else:
            continue
    
    return False

async def main(plug_addr):
    plug = SmartPlug(plug_addr)

    while True:
        status = check_battery(args.lower_limit, args.upper_limit)

        if status == "X":
            await plug.turn_off()
        elif status == "O":
            await plug.turn_on()
    
        time.sleep(10)


signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--plug", type=str, required=True, help="plug you want to modify")
parser.add_argument("-l", "--lower-limit", type=int, default=30, help="battery lower limit")
parser.add_argument("-u", "--upper-limit", type=int, default=80, help="battery upper limit")

args = parser.parse_args()

print("Finding plug")
with yaspin():
    plug_addr = asyncio.run(find_plug(args.plug))

if plug_addr:
    print("Plug found!")
    asyncio.run(main(plug_addr))
else:
    sys.exit("Plug could not be found", 1)