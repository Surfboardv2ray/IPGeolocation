import requests
import time

def query_ip_api(input_file, output_file):
    with open(input_file, 'r') as infile:
        ip_addresses = infile.readlines()

    results = []
    for i, ip_address in enumerate(ip_addresses):
        ip_address = ip_address.strip()
        try:
            response = requests.get(f'http://ip-api.com/line/{ip_address}')
            lines = response.text.split('\n')
            if lines[0] == 'success':
                country_code = lines[2]
                isp = lines[10]
                result = f"{ip_address} - {country_code} - {isp}"
                results.append(result)
                print(f"Processed {ip_address}: {result}")
            else:
                print(f"Query failed for IP: {ip_address}")
        except requests.RequestException as e:
            print(f"Request error for IP: {ip_address}: {e}")
        
        # Add a delay to handle rate limiting
        if (i + 1) % 45 == 0:
            print("Rate limit reached, waiting for 60 seconds...")
            time.sleep(60)

    with open(output_file, 'w') as outfile:
        for result in results:
            outfile.write(result + '\n')

if __name__ == "__main__":
    input_file = 'chainreaction/iplist.txt'
    output_file = 'chainreaction/countries.txt'
    query_ip_api(input_file, output_file)
