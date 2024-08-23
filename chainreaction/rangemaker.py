import socket

def read_ips(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def process_ip(ip):
    try:
        # Check if it is a domain
        if not ip.replace('.', '').isdigit():
            ip = socket.gethostbyname(ip.strip())
        parts = ip.strip().split('.')
        if len(parts) == 4 and all(0 <= int(part) <= 255 for part in parts):
            return f"{parts[0]}.{parts[1]}.{parts[2]}.0/30"
        else:
            return None
    except socket.gaierror:
        # Domain could not be resolved
        return None
    except ValueError:
        # Invalid IP parts
        return None

def write_ips(filename, ips):
    with open(filename, 'w') as file:
        for ip in ips:
            file.write(ip + "\n")

def main():
    input_file = 'chainreaction/ex.txt'
    output_file = 'chainreaction/exrange.txt'
    ips = read_ips(input_file)
    processed_ips = set()
    for ip in ips:
        ip_range = process_ip(ip.strip())
        if ip_range and ip_range not in processed_ips:
            processed_ips.add(ip_range)
    write_ips(output_file, processed_ips)

if __name__ == "__main__":
    main()
