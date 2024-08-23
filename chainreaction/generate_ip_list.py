import ipaddress

def generate_ip_list(input_file, output_file):
    with open(input_file, 'r') as infile:
        ip_ranges = infile.readlines()
    
    ip_list = []
    for ip_range in ip_ranges:
        ip_range = ip_range.strip()
        try:
            ip_network = ipaddress.ip_network(ip_range)
            ip_list.extend([str(ip) for ip in ip_network.hosts()])
        except ValueError as e:
            print(f"Skipping invalid IP range '{ip_range}': {e}")

    with open(output_file, 'w') as outfile:
        for ip in ip_list:
            outfile.write(ip + '\n')

if __name__ == "__main__":
    input_file = 'chainreaction/exrange.txt'
    output_file = 'chainreaction/iplist.txt'
    generate_ip_list(input_file, output_file)
