import base64
import json
import re

def extract_address(config):
    if config.startswith(('vless://', 'ss://', 'hysteria2://', 'trojan://')):
        match = re.search(r'@([^:]+)', config)
        if match:
            return match.group(1)
    elif config.startswith('vmess://'):
        try:
            decoded = base64.b64decode(config[8:]).decode('utf-8')
            json_data = json.loads(decoded)
            return json_data.get('add', '')
        except:
            pass
    return ''

def get_unique_addresses(file_path):
    addresses = set()
    encodings = ['utf-8', 'utf-8-sig', 'utf-16', 'latin-1']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                for line in file:
                    line = line.strip()
                    address = extract_address(line)
                    if address:
                        addresses.add(address)
            print(f"Successfully read the file using {encoding} encoding.")
            break
        except UnicodeDecodeError:
            print(f"Failed to decode with {encoding}, trying next encoding...")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return []
        except IOError as e:
            print(f"An I/O error occurred: {str(e)}")
            return []
    else:
        print(f"Error: Unable to decode the file with any of the attempted encodings.")
        return []

    return list(addresses)

def write_addresses_to_file(addresses, output_file_path):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for address in addresses:
                output_file.write(address + '\n')
        print(f"Unique addresses have been saved to {output_file_path}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {str(e)}")

def main():
    input_file_path = 'chainreaction/config.txt'
    output_file_path = 'chainreaction/ex.txt'

    unique_addresses = get_unique_addresses(input_file_path)

    if unique_addresses:
        write_addresses_to_file(unique_addresses, output_file_path)
        print(f"Total unique addresses: {len(unique_addresses)}")
    else:
        print("No addresses were extracted or an error occurred.")

if __name__ == "__main__":
    main()
