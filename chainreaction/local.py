def filter_local_ips(input_file, output_file, country_code="IR"):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file {input_file}: {e}")
        return

    local_ips = []
    for line in lines:
        try:
            ip_address, code, isp = line.strip().split(" - ")
            if code == country_code:
                local_ips.append(ip_address)
        except ValueError:
            print(f"Skipping malformed line: {line.strip()}")
        except Exception as e:
            print(f"An error occurred while processing line: {line.strip()}: {e}")

    try:
        with open(output_file, 'w') as outfile:
            for ip in local_ips:
                outfile.write(ip + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the file {output_file}: {e}")

if __name__ == "__main__":
    input_file = 'chainreaction/countries.txt'
    output_file = 'chainreaction/local.txt'
    filter_local_ips(input_file, output_file)
