import ipaddress

ipv6_prefix = input("Bitte geben Sie den IPv6-Präfix an: ")
output_file = input("Bitte geben Sie den Dateinamen an: ")+".txt"
domain = input("Bitte geben Sie die Domain an: ")

print(f"Die Datei {output_file} wird erstellt.")
print("Bitte warten...")

def generate_ipv6_ptr_records(ipv6_prefix, output_file):
    network = ipaddress.IPv6Network(ipv6_prefix, strict=False)
    
    with open(output_file, 'w') as file:
        for ip in network:
            reversed_dns = '.'.join(reversed(str(ip).replace(':', ''))) + '.ip6.arpa'
            ptr_record = f"{reversed_dns} 60 IN PTR {domain}."
            file.write(ptr_record + '\n')

generate_ipv6_ptr_records(ipv6_prefix, output_file)

print("Fertig! Deine datei wurde Erfolgreich erstellt.")
