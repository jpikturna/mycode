#!/usr/bin/env python3
"""Alta3 Research || Author:  jppikturna@gmail.com"""

import crayons

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys():
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}')
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to send command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# start the main
def main():
    """called at runtime"""

    #dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print(f"Welcome to the {crayons.blue('Network')} Device Command Pusher") 

    ## get dataset
    print("\nData set found\n")

    ## run
    commandpush(devicecmd)

if __name__ == "__main__":
    main()
