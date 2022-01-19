# NOTE: All functions are in pairs of the main function and an optional "silent" function 
# which would simply return a value instead of printing

# decimal to binary function
def to_binary(data: str):
    print("Decimal value:",data)
    try:
        dec = int(data)
        bnr = bin(dec).replace('0b','')
    except ValueError:
        raise ValueError("Non-decimal value entered!")
    print("Binary value:",bnr)
def to_binary_s(data: str):
    try:
        dec = int(data)
        bnr = bin(dec).replace('0b','')
    except ValueError:
        raise ValueError("Non-decimal value entered!")
    return bnr

# decimal to octal function
def to_octal(data: str):
    print("Decimal value:",data)
    try:
        dec = int(data)
        octal = oct(dec).replace('0o','')
    except ValueError:
        raise ValueError("Non-decimal value entered!")
    print("Octal value:",octal)
def to_octal_s(data: str):
    try:
        dec = int(data)
        octal = oct(dec).replace('0o','')
    except ValueError:
        raise ValueError("Non-decimal value entered!")
    return octal

# decimal to hexadecimal
def to_hexadecimal(data: str):
    print("Decimal value:",data)
    try:
        dec = int(data)
        hxd = hex(dec).replace('0x','')
    except ValueError:
        raise ValueError("Non-decimal value entered!")
    print("Hexadecimal value:",hxd)
def to_hexas(data: str):
    try:
        dec = int(data)
        hxd = hex(dec).replace('0x','')
    except ValueError:
        raise ValueError("Non-decimal value entered!")
    return hxd

# decimal to text function
def to_text(data: str):
    data = data.split()
    l = []
    for i in data:
        try:
            z = int(i)
            l.append(chr(z))
        except ValueError:
            raise ValueError("Non-decimal value entered!")
    print("ASCII value:",''.join(l))
def to_text_s(data: str):
    data = data.split()
    l = []
    for i in data:
        try:
            z = int(i)
            l.append(chr(z))
        except ValueError:
            raise ValueError("Non-decimal value entered!")
    return ''.join(l)