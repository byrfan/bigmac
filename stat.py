import winreg

def get_value_if_exists(key_path: str, value_name: str):
    """Checks if a specific value exists in a registry subkey and returns its value if found."""
    try:
        # Open the registry key with read permissions
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as reg_key:
            try:
                # Try to query the value by name and return it
                value, _ = winreg.QueryValueEx(reg_key, value_name)
                return value
            except FileNotFoundError:
                # If the value is not found, return None
                return None
    except FileNotFoundError:
        # If the key itself doesn't exist, return None
        print(f"Registry key not found: {key_path}")
        return None
    except Exception as e:
        # Handle other exceptions if necessary
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Registry path to the adapter (Modify as needed)
    key_to_check = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\0003"
    value_to_check = "NetworkAddress"

    mac_address = get_value_if_exists(key_to_check, value_to_check)
    
    if mac_address:
        print(f"The value '{value_to_check}' exists and its MAC address is: {mac_address}")
    else:
        print(f"The value '{value_to_check}' does not exist in the subkey.")


