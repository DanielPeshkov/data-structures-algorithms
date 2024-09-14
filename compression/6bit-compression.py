# Encode string to (binary) int representation
def encode(s):
    if len(s) == 0:
        raise ValueError("Cannot encode empty string")
    encoded = 0
    for character in s:
        utf = ord(character)
        # Unsupported
        if utf > 122:
            raise ValueError("Invalid Character")
        # Lowercase Letters
        elif utf > 96:
            encoded |= (utf - 87)
        # Unsupported
        elif utf > 90:
            raise ValueError("Invalid Character")
        # Uppercase Letters
        elif utf > 64:
            encoded |= (utf - 55)
        # Numbers
        elif utf >= 48 and utf <= 57:
            encoded |= (utf - 48)
        # Hyphen (minus)
        elif utf == 47:
            encoded |= 36
        # Forward Slash
        elif utf == 45:
            encoded |= 37
        else:
            raise ValueError("Invalid Character")
        encoded <<= 6
    return encoded >> 6

# Compress string using 6-bit encoding
def compress(s):
    encoded = encode(s)
    compressed = ''
    while encoded > 0:
        compressed += chr(encoded & 255)
        encoded >>= 8
    
    return compressed

# Decode 6-bit binary back to utf-8 character
def decode(c):
    # Numbers
    if c < 10:
        return chr(c + 48)
    # Lowercase Letters
    if c < 36:
        return chr(c + 87)
    if c == 36:
        return '/'
    return '-'

# Decompress string using 6-bit decoding
def decompress(s):
    encoded = 0
    for character in s[::-1]:
        encoded |= ord(character)
        encoded <<= 8
    encoded >>= 8

    decompressed = ''
    while encoded > 0:
        decompressed += decode(encoded & 63)
        encoded >>= 6
    
    return decompressed[::-1]

def test_6bit_compression():
    test_cases = ['secret-message', 'msg-with-dashes', 'msg/with/slashes', 'msgw17hnumb3rs']
    failed = False
    for i, case in enumerate(test_cases):
        compressed = compress(case)
        decompressed = decompress(compressed)
        if (len(compressed) > len(case)) or (decompressed != case):
            failed = True
            print(f"'\033[91m' + 'Failed Test Case ' + '\x1b[0m'{i+1}")
    if not failed:
        print('\033[92m' + 'All Tests Pass' + '\x1b[0m')

test_6bit_compression()