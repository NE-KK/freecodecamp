# freecodecamp
# Daily Coding Challenges
# Day 26 (2025-09-05)
# IPv4 Validator

"""
Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated by dots (.). 
Each number must satisfy the following conditions:

- It is between 0 and 255 inclusive.
- It does not have leading zeros (e.g. 0 is allowed, 01 is not).
- Only numeric characters are allowed.
"""

def create_octet_list(ip_address):
    return ip_address.split(".")


def four_octets(ip_address):
    octet_list = create_octet_list(ip_address)
    
    if len(octet_list) == 4:
        return True
    else:
        return False


def valid_seperator(ip_address): 
    count_dot = ip_address.count(".")

    if count_dot == 3:
        return True
    else:
        return False


def no_leaading_zeros(ip_address):
    octet_list = create_octet_list(ip_address)

    for octet in octet_list:
        if octet == "":
            return False 
        if octet[0] == "0" and len(octet) > 1:
            return False

    return True


def octet_in_range(ip_address):
    octet_list = create_octet_list(ip_address)

    for octet in octet_list:
        if int(octet) > 255:
            return False
    
    return True


def is_valid_ipv4(ip_address):
    is_valid = True

    if is_valid:
        is_valid = valid_seperator(ip_address)
    if is_valid:
        is_valid = four_octets(ip_address)
    if is_valid:
        is_valid = no_leaading_zeros(ip_address)
    if is_valid:
        is_valid = octet_in_range(ip_address)

    return is_valid


print(is_valid_ipv4("192.168.1.1"))
print(is_valid_ipv4("192.168.01.1"))
print(is_valid_ipv4("192168.1.1"))
print(is_valid_ipv4("192.168.1."))
print(is_valid_ipv4("256.168.1."))
