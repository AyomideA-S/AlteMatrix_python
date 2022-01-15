def to_binary(data: str):
    print("Hexadecimal value:",data)
    try:
        bnr = int(data,16)
        bnr = bin(bnr).replace('0b','')
    except ValueError:
        raise ValueError("Non-hexadecimal number entered!")
    print("Binary value:",bnr)
def to_binary_s(data: str):
    try:
        bnr = int(data,16)
        bnr = bin(bnr).replace('0b','')
    except ValueError:
        raise ValueError("Non-hexadecimal number entered!")
    return bnr


def to_octal(data: str):
    print("Hexadecimal value:",data)
    try:
        octal = int(data,16)
        octal = oct(octal).replace('0o','')
    except ValueError:
        raise ValueError("Non-hexadecimal number entered!")
    print("Octal value:",octal)
def to_octal_s(data: str):
    try:
        octal = int(data,16)
        octal = oct(octal).replace('0o','')
    except ValueError:
        raise ValueError("Non-hexadecimal number entered!")
    return octal

def to_decimal(data: str):
    print("Hexadecimal value:",data)
    try:
        decimal = int(data,16)
    except ValueError:
        raise ValueError("Non-hexadecimal number entered!")
    print("Decimal value:",decimal)
def to_decimal_s(data: str):
    try:
        decimal = int(data,16)
    except ValueError:
        raise ValueError("Non-hexadecimal number entered!")
    return decimal

def to_text(data: str):
    data = data.split()
    l = []
    for i in data:
        try:
            z = chr(int(i,16))
            l.append(z)
        except ValueError:
            raise ValueError("Non-hexadecimal value entered or limit reached!")
        except OverflowError:
            raise ValueError("Hexadecimal value limit exceeded!")
    print("ASCII value:",''.join(l))
def to_text_s(data: str):
    data = data.split()
    l = []
    for i in data:
        try:
            z = chr(int(i,16))
            l.append(z)
        except ValueError:
            raise ValueError("Non-hexadecimal value entered or limit reached!")
        except OverflowError:
            raise ValueError("Hexadecimal value limit exceeded!")
    return ''.join(l)