import socket
import os

def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

def read_domains(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        domains = {line.strip() for line in file}
    return domains

def write_to_file(file_path, data, mode='a'):
    with open(file_path, mode) as file:
        for line in data:
            file.write(line + '\n')

def main():
    domain_file = 'domainresolve/domain.txt'
    ip_resolved_file = 'domainresolve/ip+resolved.txt'
    ip_domain_file = 'domainresolve/ip+domain.txt'

    domains = read_domains(domain_file)

    resolved_ips = set()
    ip_domain_pairs = set()

    if os.path.exists(ip_resolved_file):
        resolved_ips.update(read_domains(ip_resolved_file))
    if os.path.exists(ip_domain_file):
        existing_pairs = read_domains(ip_domain_file)
        for pair in existing_pairs:
            _, ip = pair.split(' - ')
            resolved_ips.add(ip)

    for domain in domains:
        ip = resolve_domain(domain)
        if ip and ip not in resolved_ips:
            resolved_ips.add(ip)
            ip_domain_pairs.add(f'{domain} - {ip}')

    write_to_file(ip_resolved_file, resolved_ips, mode='w')
    write_to_file(ip_domain_file, ip_domain_pairs, mode='w')

if __name__ == '__main__':
    main()

