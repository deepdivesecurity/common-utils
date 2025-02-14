#!/usr/bin/env python

import ipaddress

def check_if_ip_belongs_to_subnet(ip: str, network: str) -> bool: 
    ip_obj = ipaddress.ip_address(ip)
    network_obj = ipaddress.ip_network(network, strict=False)

    return ip_obj in network_obj

def convert_ip_to_binary(ip) -> str: 
    # Check type of variable passed in - might want to change this to the Pythonic duck-typing way of handling
    if isinstance(ip, ipaddress.IPv4Address): 
        ip = str(ip)
    elif isinstance(ip, str): 
        # Do nothing
        pass
    else: 
        return None
    
    # Split the string representation of the IP by the "." to acquire each octet of the IP
    octets = ip.split(".")
    binary = ""

    # Loop through the octets and transform to binary
    for octet in octets: 
        binary += f"{int(octet):08b}"

    # Return the binary representation in string format
    return binary

def get_subnet_mask(network: str) -> ipaddress.IPv4Address: 
    return ipaddress.ip_network(network).netmask
    
def convert_binary_to_ip(bits: str) -> str: 
    # Check type of variable passed in - might want to change this to the Pythonic duck-typing way of handling
    if not isinstance(bits, str): 
        return None
    
    octets = []

    # Loop through the str in chunks of 8 for each octet
    for i in range(0, len(bits), 8): 
        # Covert each binary representation to its decimal equivalent and append it to the list
        octet = str(int(bits[i:i+8], 2))
        octets.append(octet)

    # Join the list and return it
    return ".".join(octets)

def get_all_hosts(network: str) -> list: 
    # Check type of variable passed in - might want to change this to the Pythonic duck-typing way of handling
    if not isinstance(network, str): 
        return None
    
    return list(ipaddress.ip_network(network).hosts())

def get_host_mask(network: str) -> ipaddress.IPv4Address: 
    return ipaddress.ip_network(network).hostmask

def get_ip_range(network: str) -> str: 
    hosts = get_all_hosts(network)
    if hosts: 
        range = str(hosts[0]) + " - " + str(hosts[-1])
        return range
    else: 
        return None

def main(): 
    host_mask = get_host_mask("192.168.20.0/24")
    print(host_mask)

if __name__ == "__main__": 
    main()