import os
import time
import winreg

def delete_network_address_value():
    try:
        # Define the registry path for the network adapter
        reg_path = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\0003"
        
        # Open the registry key with permissions to delete values
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE) as reg_key:
            try:
                # Delete the 'NetworkAddress' value if it exists
                winreg.DeleteValue(reg_key, "NetworkAddress")
                print("Successfully deleted 'NetworkAddress' value.")
            except FileNotFoundError:
                print("'NetworkAddress' value does not exist.")
    except PermissionError:
        print("Permission denied. Please run this script with administrative privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")

def doReset():
    os.system("netsh interface set interface Wi-Fi admin=disable")
    time.sleep(1)
    delete_network_address_value()
    time.sleep(1)
    os.system("netsh interface set interface Wi-Fi admin=enable")

doReset()
