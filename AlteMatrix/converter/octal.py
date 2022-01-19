# NOTE: All functions are in pairs of the main function and an optional "silent" function 
# which would simply return a value instead of printing

# list of invalid octal figures
inv = ['8','9']
# octal to binary function
def octal_to_binary(data: str):
    print("Octal value:",data)
    for digit in data:
        if digit in inv:
            raise ValueError("Non-octal number entered!")
        try:
            bnr = int(data,8)
            bnr = bin(bnr).replace('0b', '')
        except ValueError:
            raise ValueError("Non-octal number entered!")
    print("Binary value: ",bnr)
def octal_to_binary_s(data: str):
    for digit in data:
        if digit in inv:
            raise ValueError("Non-octal number entered!")
        try:
            bnr = int(data,8)
            bnr = bin(bnr).replace('0b', '')
        except ValueError:
            raise ValueError("Non-octal number entered!")
    return bnr

# octal to decimal function
def octal_to_decimal(data: str):
    print("Octal value:",data)
    decimal = 0
    for i in data:
        if i in inv:
            raise ValueError("Non-octal number entered!")
        try:
            decimal = decimal*8 + int(i)
        except ValueError:
            raise ValueError("Non-octal number entered!")
    print("Decimal value:",decimal)
def octal_to_decimal_s(data: str):
    decimal = 0
    for i in data:
        if i in inv:
            raise ValueError("Non-octal number entered!")
        try:
            decimal = decimal*8 + int(i)
        except ValueError:
            raise ValueError("Non-octal number entered!")
    return decimal

# octal to hexadecimal function
def octal_to_hexadecimal(data: str):
    print("Octal value:",data)
    for digit in data:
        if digit in inv:
            raise ValueError("Non-octal number entered!")
        try:
            hxd = int(data,8)
            hxd = hex(hxd).replace('0x', '')
        except ValueError:
            raise ValueError("Non-octal number entered!")
    print("Hexadecimal value: ",hxd)
def octal_to_hexadecimal_s(data: str):
    for digit in data:
        if digit in inv:
            raise ValueError("Non-octal number entered!")
        try:
            hxd = int(data,8)
            hxd = hex(hxd).replace('0x', '')
        except ValueError:
            raise ValueError("Non-octal number entered!")
    return hxd

# octal to text function
def octal_to_text(data: str):
    data = data.split()
    l = []
    for i in data:
        try:
            z = int(i, 8)
            l.append(chr(z))
        except ValueError:
            raise ValueError("Non-octal number entered!")
    print("ASCII value:",''.join(l))
def octal_to_text_s(data: str):
    data = data.split()
    l = []
    for i in data:
        try:
            z = int(i, 8)
            l.append(chr(z))
        except ValueError:
            raise ValueError("Non-octal number entered!")
    return ''.join(l)