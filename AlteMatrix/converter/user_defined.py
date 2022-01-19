import sys, atexit, io
buffer = io.BytesIO()
sys.stdout.buffer
@atexit.register

# write function
def write():
    sys.__stdout__.write(buffer.getvalue().decode("utf-8"))

# dictionary for interpretation of non-decimal numbers
base = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}
# "user-defined" function
def udf(source: int, destination: int | None = 10):
    # check for invalid arguments
    try:
        source = int(source)
        destination = int(destination)
        if source <= 1 or source >= 37 or destination <= 1 or destination >= 37:
            raise ValueError("Base limits exceeded!")
    except ValueError:
        raise ValueError("Invalid base entered!")
    # get value to be converted
    value = input(f"Base {source} value: ")
    # check for invalid characters in value
    try:
        con = int(value,source)
        l = []
        while con > 0:
            fetch = con % destination
            l.append(base.get(fetch,fetch))
            con //= destination
    except ValueError:
        raise ValueError("Inappropriate base or wrong value entered!")
    l = list(map(str,l))
    # print result
    print(f'Base {destination} value:',''.join(l[::-1]))
# silent "user-defined" function
def udf_s(source: int, destination: int | None = 10):
    # check for invalid arguments
    try:
        source = int(source)
        destination = int(destination)
        if source <= 1 or source >= 37 or destination <= 1 or destination >= 37:
            raise ValueError("Base limits exceeded!")
    except ValueError:
        raise ValueError("Invalid base entered!")
    # get value to be converted
    value = input()
    # check for invalid characters in value
    try:
        con = int(value,source)
        l = []
        while con > 0:
            fetch = con % destination
            l.append(base.get(fetch,fetch))
            con //= destination
    except ValueError:raise ValueError("Inappropriate base or wrong value entered!")
    l = list(map(str,l))
    # return result of conversion
    return ''.join(l[::-1])

# "user-defined text" function
def udt(value: str | None = None, source: str | None = "10", destination: str | None = "txt", readfile: str | None = None, writefile: str | None = None):
    # check for readable file as argument
    if readfile != None:
        sys.stdin = open(readfile, 'r')
        value = sys.stdin.read()
    elif value == None:
        raise ValueError("You have not supplied an input!")
    # check for writable file as argument
    if writefile != None:
        sys.stdout = open(writefile, 'w')

    # check for invalid arguments
    try:
        if source == "txt":
            pass
        else:
            try:
                source = int(source)
                if source <= 1 or source >= 37:
                    raise ValueError("Base limits exceeded!")
            except ValueError:
                raise ValueError("Invalid base entered!")
        if destination == "txt":
            pass
        else:
            try:
                destination = int(destination)
                if destination <= 1 or destination >= 37:
                    raise ValueError("Base limits exceeded!")
            except ValueError:
                raise ValueError("Invalid base entered!")
    except ValueError:raise ValueError("Invalid base entered!")
    
    # check for the "txt" argument
    if source != "txt" and destination != "txt":
        raise TypeError("You can only convert to or from text using this function!")

    # converting from text
    if source == "txt" and destination != "txt":
        z = []
        l = []
        hit = f"Base {destination} value"
        # get decimal value of each character
        for i in value:
            z.append(ord(i))
        for i in z:
            while i > 0:
                fetch = i % destination
                l.append(base.get(fetch,fetch))
                i //= destination
            l.append(" ")
        l = list(map(str,l))
        cip = ''.join(l[::-1])
        cip = cip.split()
        l = cip[::-1]
        # final conversion result
        l = " ".join(l)

    # converting to text
    if source != "txt" and destination == "txt":
        z = []
        l = []
        cry = f"Base {source}"
        hit = "Text"
        # check for invalid values in selceted number base
        try:
            for i in value.split():
                x = int(i,source)
                l.append(chr(x))
        except ValueError:
            raise ValueError(f"The value(s) provided are not in {cry}!")

    # return text value
    if source == "txt" and destination == "txt":
        hit = "Text"
        l = value.split()
    # print final conversion result
    print(f'{hit}:\n'+''.join(l))
# "user-defined text" function
def udt_s(value: str | None = None, source: str | None = "10", destination: str | None = "txt", readfile: str | None = None):
    # check for readable file as argument
    if readfile != None:
        sys.stdin = open(readfile, 'r')
        value = sys.stdin.read()
    elif value == None:
        raise ValueError("You have not supplied an input!")

    # check for invalid arguments
    try:
        if source == "txt":
            pass
        else:
            try:
                source = int(source)
                if source <= 1 or source >= 37:
                    raise ValueError("Base limits exceeded!")
            except ValueError:
                raise ValueError("Invalid base entered!")
        if destination == "txt":
            pass
        else:
            try:
                destination = int(destination)
                if destination <= 1 or destination >= 37:
                    raise ValueError("Base limits exceeded!")
            except ValueError:
                raise ValueError("Invalid base entered!")
    except ValueError:raise ValueError("Invalid base entered!")

    # check for the "txt" argument
    if source != "txt" and destination != "txt":
        raise TypeError("You can only convert to or from text using this function!")

    # converting from text
    if source == "txt" and destination != "txt":
        z = []
        l = []
        hit = f"Base {destination} value"
        # get decimal value of each character
        for i in value:
            z.append(ord(i))
        for i in z:
            while i > 0:
                fetch = i % destination
                l.append(base.get(fetch,fetch))
                i //= destination
            l.append(" ")
        l = list(map(str,l))
        cip = ''.join(l[::-1])
        cip = cip.split()
        l = cip[::-1]
        # final conversion result
        l = " ".join(l)

    # converting to text
    if source != "txt" and destination == "txt":
        z = []
        l = []
        cry = f"Base {source}"
        hit = "Text"
        # check for invalid values in selceted number base
        try:
            for i in value.split():
                x = int(i,source)
                l.append(chr(x))
        except ValueError:
            raise ValueError(f"The value(s) provided are not in {cry}!")

    # return text value
    if source == "txt" and destination == "txt":
        l = value.split()
    # return final conversion results
    return ''.join(l)
