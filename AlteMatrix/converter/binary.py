inv = ['2','3','4','5','6','7','8','9']
def to_decimal(data: str):
    print("Binary value:",data)
    decimal = 0
    for digit in data:
        if digit in inv:
            raise ValueError("Non-binary number entered!")
        try:
            decimal = decimal*2 + int(digit)
        except ValueError:
            raise ValueError("Non-binary number entered!")
    print("Decimal value: ",decimal)
def to_decimal_s(data: str):
    decimal = 0
    for digit in data:
        if digit in inv:
            raise ValueError("Non-binary number entered!")
        try:
            decimal = decimal*2 + int(digit)
        except ValueError:
            raise ValueError("Non-binary number entered!")
    return decimal

def to_octal(data: str):
    print("Binary value:",data)
    for digit in data:
        if digit in inv:
            raise ValueError("Non-binary number entered!")
        try:
            octal = int(data,2)
            octal = oct(octal).replace('0o', '')
        except ValueError:
            raise ValueError("Non-binary number entered!")
    print("Octal value: ",octal)
def to_octal_s(data: str):
    for digit in data:
        if digit in inv:
            raise ValueError("Non-binary number entered!")
        try:
            octal = int(data,2)
            octal = oct(octal).replace('0o', '')
        except ValueError:
            raise ValueError("Non-binary number entered!")
    return octal

def to_hexadecimal(data: str):
    print("Binary value:",data)
    for digit in data:
        if digit in inv:
            raise ValueError("Non-binary number entered!")
        try:
            hxd = int(data,2)
            hxd = hex(hxd).replace('0x', '')
        except ValueError:
            raise ValueError("Non-binary number entered!")
    print("Hexadecimal value: ",hxd)
def to_hexadecimal_s(data: str):
    for digit in data:
        if digit in inv:
            raise ValueError("Non-binary number entered!")
        try:
            hxd = int(data,2)
            hxd = hex(hxd).replace('0x', '')
        except ValueError:
            raise ValueError("Non-binary number entered!")
    return hxd

def to_text(data: str):
    data = data.split()
    l = []
    for i in data:
        try:
            z = int(i, 2)
            l.append(chr(z))
        except ValueError:
            raise ValueError("Non-binary value entered!")
    print("Binary Value:", ' '.join(data))
    print("ASCII value:", ''.join(l))
def to_text_s(data: str):
    data = data.split()
    l = []
    for i in data:
        try:
            z = int(i, 2)
            l.append(chr(z))
        except ValueError:
            raise ValueError("Non-binary value entered!")
    return ''.join(l)
