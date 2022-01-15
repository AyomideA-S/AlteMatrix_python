import sys, atexit, io
buffer = io.BytesIO()
sys.stdout.buffer
@atexit.register

def write():
    sys.__stdout__.write(buffer.getvalue().decode("utf-8"))

base = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}
def udf(source: int, destination: int | None = 10):
    try:
        source = int(source)
        destination = int(destination)
        if source <= 1 or source >= 37 or destination <= 1 or destination >= 37:
            raise ValueError("Base limits exceeded!")
    except ValueError:raise ValueError("Invalid base entered!")
    value = input(f"Base {source} value: ")
    try:
        con = int(value,source)
        l = []
        while con > 0:
            fetch = con % destination
            l.append(base.get(fetch,fetch))
            con //= destination
    except ValueError:raise ValueError("Inappropriate base or wrong value entered!")
    l = list(map(str,l))
    print(f'Base {destination} value:',''.join(l[::-1]))
def udf_s(source: int, destination: int | None = 10):
    try:
        source = int(source)
        destination = int(destination)
        if source <= 1 or source >= 37 or destination <= 1 or destination >= 37:
            raise ValueError("Base limits exceeded!")
    except ValueError:raise ValueError("Invalid base entered!")
    value = input()
    try:
        con = int(value,source)
        l = []
        while con > 0:
            fetch = con % destination
            l.append(base.get(fetch,fetch))
            con //= destination
    except ValueError:raise ValueError("Inappropriate base or wrong value entered!")
    l = list(map(str,l))
    return ''.join(l[::-1])

def udt(value: str | None = None, source: str | None = "10", destination: str | None = "txt", readfile: str | None = None, writefile: str | None = None):
    if readfile != None:
        sys.stdin = open(readfile, 'r')
        value = sys.stdin.read()
    elif value == None:raise ValueError("You have not supplied an input!")
    if writefile != None:sys.stdout = open(writefile, 'w')

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

    if source != "txt" and destination != "txt":
        raise TypeError("You can only convert to or from text using this function!")

    if source == "txt" and destination != "txt":
        z = []
        l = []
        hit = f"Base {destination} value"
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
        l = " ".join(l)

    if source != "txt" and destination == "txt":
        z = []
        l = []
        cry = f"Base {source}"
        hit = "Text"
        try:
            for i in value.split():
                x = int(i,source)
                l.append(chr(x))
        except ValueError:
            raise ValueError(f"The value(s) provided are not in {cry}!")

    if source == "txt" and destination == "txt":
        hit = "Text"
        l = value.split()
    
    print(f'{hit}:\n'+''.join(l))
def udt_s(value: str | None = None, source: str | None = "10", destination: str | None = "txt", readfile: str | None = None):
    if readfile != None:
        sys.stdin = open(readfile, 'r')
        value = sys.stdin.read()
    elif value == None:raise ValueError("You have not supplied an input!")

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

    if source != "txt" and destination != "txt":
        raise TypeError("You can only convert to or from text using this function!")

    if source == "txt" and destination != "txt":
        z = []
        l = []
        hit = f"Base {destination} value"
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
        l = " ".join(l)

    if source != "txt" and destination == "txt":
        z = []
        l = []
        cry = f"Base {source}"
        hit = "Text"
        try:
            for i in value.split():
                x = int(i,source)
                l.append(chr(x))
        except ValueError:
            raise ValueError(f"The value(s) provided are not in {cry}!")

    if source == "txt" and destination == "txt":
        hit = "Text"
        l = value.split()
    
    return ''.join(l)
