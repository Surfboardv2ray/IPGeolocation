import base64
import json
import os

# Global variable to keep track of processed proxies
proxy_counter = 0

# List of addresses to be changed
addresses_to_change = ["www.speedtest.net", "speedtest.net", "zula.ir", "www.zula.ir", "parsvds.ir", "www.parsvds.ir"]

def rename_vmess_address(proxy, new_address):
    global proxy_counter
    base64_str = proxy.split('://')[1]
    missing_padding = len(base64_str) % 4
    if missing_padding:
        base64_str += '=' * (4 - missing_padding)
    try:
        decoded_str = base64.b64decode(base64_str).decode('utf-8')
        proxy_json = json.loads(decoded_str)
        
        # Only change if the address matches one of the specified values
        if proxy_json['add'] in addresses_to_change:
            proxy_json['add'] = new_address
            proxy_counter += 1
            encoded_str = base64.b64encode(json.dumps(proxy_json).encode('utf-8')).decode('utf-8')
            renamed_proxy = 'vmess://' + encoded_str
            print(f"Renamed VMess proxy (#{proxy_counter}): {renamed_proxy}")  # Debugging
            return renamed_proxy
        else:
            print(f"Skipped VMess proxy with address {proxy_json['add']}")  # Debugging
            return None

    except Exception as e:
        print("Error processing VMess proxy: ", e)
        return None

def rename_vless_address(proxy, new_address):
    global proxy_counter
    try:
        parts = proxy.split('@')
        userinfo = parts[0]
        hostinfo = parts[1]
        hostinfo_parts = hostinfo.split(':')

        # Only change if the address matches one of the specified values
        if hostinfo_parts[0] in addresses_to_change:
            hostinfo_parts[0] = new_address
            hostinfo = ':'.join(hostinfo_parts)
            renamed_proxy = userinfo + '@' + hostinfo
            proxy_counter += 1
            print(f"Renamed VLess proxy (#{proxy_counter}): {renamed_proxy}")  # Debugging
            return renamed_proxy
        else:
            print(f"Skipped VLess proxy with address {hostinfo_parts[0]}")  # Debugging
            return None

    except Exception as e:
        print("Error processing VLess proxy: ", e)
        return None

def process_proxies(input_file, output_file, new_address):
    with open(input_file, 'r') as f, open(output_file, 'w') as out_f:
        proxies = f.readlines()
        for proxy in proxies:
            proxy = proxy.strip()
            if proxy.startswith('vmess://'):
                renamed_proxy = rename_vmess_address(proxy, new_address)
            elif proxy.startswith('vless://'):
                renamed_proxy = rename_vless_address(proxy, new_address)
            else:
                renamed_proxy = None  # Skip non-vmess/vless proxies

            if renamed_proxy is not None:
                out_f.write(renamed_proxy + '\n')

# Example usage
input_file = 'limitbreaker/limited.txt'
output_file = 'limitbreaker/limitbreaker.txt'
new_address = '85.9.120.11'

process_proxies(input_file, output_file, new_address)

