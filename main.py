
t = str(input("Type a text: "))

def str_to_bin(letter: str) -> bin:
    return bin(ord(str(letter)))

def encrypt() -> int:

    hash_return = ''

    for letter in t:
        
        hash_return += str(str_to_bin(letter)).replace('0b','').ljust(8, '0')

    return int(f'0b{hash_return}', 2)

print(encrypt())
