import random
import os
import winreg
import time

def generate_random_mac() -> str:
    """Generates a random MAC address with the first octet set to 02."""
    # The first octet is fixed as '02' to signify a locally administered MAC address
    mac = [0x02]  # First octet is '02'
    
    # Generate the remaining 5 octets (each a pair of hexadecimal digits)
    mac += [random.randint(0x00, 0xFF) for _ in range(5)]
    
    # Convert the list of integers to a continuous string of hexadecimal digits without separators
    return ''.join(f"{b:02X}" for b in mac)

def set_random_mac_address():
    """Sets a random MAC address in the registry."""
    try:
        # Define the registry path for the network adapter
        reg_path = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\0003"
        
        # Generate a random MAC address
        random_mac = generate_random_mac()  # Properly call the function here

        # Open the registry key with permissions to set values
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE) as reg_key:
            try:
                # Set the 'NetworkAddress' value to the random MAC address
                winreg.SetValueEx(reg_key, "NetworkAddress", 0, winreg.REG_SZ, random_mac)
                print(f"Successfully set random MAC address: {random_mac}")
            except Exception as e:
                print(f"Failed to set MAC address: {e}")
    except PermissionError:
        print("Permission denied. Please run this script with administrative privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")


def doRandomize():
    os.system("netsh interface set interface Wi-Fi admin=disable")
    time.sleep(1)
    set_random_mac_address()
    time.sleep(1)
    os.system("netsh interface set interface Wi-Fi admin=enable")

doRandomize()
