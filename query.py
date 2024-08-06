import requests

def query_ip_api(input_file, output_file):
    with open(input_file, 'r') as infile:
        ip_addresses = infile.readlines()

    results = []
    for ip_address in ip_addresses:
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

    with open(output_file, 'w') as outfile:
        for result in results:
            outfile.write(result + '\n')

if __name__ == "__main__":
    input_file = 'files/iplist.txt'
    output_file = 'files/countries.txt'
    query_ip_api(input_file, output_file)
