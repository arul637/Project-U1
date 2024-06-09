import random

def getBits(length):
        bits = ''
        for i in range(length):
            bits += str(round(random.random()))
        return bits

def merge8bits(password_biniary):
        merged_binary = ''
        for i in range(0, len(password_biniary), 8):
            merged_binary += password_biniary[i:i+8] + getBits(8)
        return merged_binary

def encryption(password):
    # 1. split into binary
    password_binary = ''
    for i in password:
        password_binary += bin(ord(i))[2:].rjust(8, '0')

    # 2. placing 8 bits random between every 8 bits of intervel
    password_binary = merge8bits(password_binary)

    # 3. splitting into 14 bits and add padding
    padding_length = 14 - len(password_binary)%14
    padding_bits = getBits(padding_length)
    password_binary = password_binary + padding_bits

        # splitting by 14 and make it hex values
    temp_password_binary = ''
    for i in range(0, len(password_binary), 14):
        temp_password_binary += getBits(2) + password_binary[i:i+14]

    password_binary = temp_password_binary

        # converting into hex
    hex_password = ''
    for i in range(0, len(password_binary), 8):
        hex_password += hex(int(password_binary[i:i+8], 2))[2:].rjust(2, '0')

    hex_password = hex_password + hex(int(padding_length))[2:].rjust(2, '0')

    return hex_password

def strong_password_generator(violation=None, password_length=None):
        if violation is None:
            violation = [34, 39, 42, 43, 44, 45, 46]
        if password_length is None:
            password_length = 15
        strong_password = ''
        for i in range(password_length):
            ordinal_number = random.randint(33, 126)
            if ordinal_number not in violation:
                strong_password += str(chr(ordinal_number))

        return strong_password

def decryption(hash):

        # 1. getting padding bits and hex values
        padding_length_hex = hash[len(hash)-2:]
        hash_hex = hash[:len(hash)-2]

            # decoding the hex values
        padding_length = int(padding_length_hex, 16)

        # 2. converting into binary
        hash_binary = ''
        for i in range(0, len(hash_hex), 2):
            hash_binary += bin(int(hash_hex[i:i+2], 16))[2:].rjust(8, '0')

        # 3. splitting 16 bits and getting password binary by last 14 bits
        temp_hash_binary = ''
        for i in range(0, len(hash_binary), 16):
            temp_hash_binary += hash_binary[i+2:i+16]
        hash_binary = temp_hash_binary

        # 4. removing padding bits
        hash_binary = hash_binary[:(len(hash_binary))-padding_length]

        # 5. splitting each binary into 8 bits and removing extra 8 bits and find the character
        temp_hash_binary = ''
        for i in range(0, len(hash_binary), 16):
            temp_hash_binary += hash_binary[i:i+8]
        hash_binary = temp_hash_binary

        # 6. finding password
        password = ''
        for i in range(0, len(hash_binary), 8):
            password += chr(int(hash_binary[i:i+8], 2))

        return password