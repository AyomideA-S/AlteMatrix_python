# IPv6 Address Analyzer by Ir0n-c0d3X

import sys, atexit, io
buffer = io.BytesIO()
sys.stdout.buffer
@atexit.register

def write():
    sys.__stdout__.write(buffer.getvalue().decode("utf-8"))

import re
def ipv6(IP: str, Mask: str | None = ..., file: str | None = None):
    if file != None:
        sys.stdout = open(file, 'w')

    if IP == None:
        return ValueError("The address argument cannot be empty!")
        
    IP = re.split(':|%|/', IP)

    if IP[-1] == '' and IP[-2] == '':
        IP.pop(-1)

    try:
        l = len(IP)
        if l != 8:
            x = 8 - l
            y = IP.index('')
            IP.pop(y)
            for i in range(x+1):
                IP.insert(y, '0000')
        for i in IP:
            x = len(i)
            if x != 4:
                h = IP.index(i)
                l = 4 - x
                i = str(('0'*l) + i)
                IP.pop(h)
                IP.insert(h, i)
    except ValueError:
        raise ValueError("Invalid IPv6 address entered!")

    print("Network Portion:", ':'.join(IP[:4]))
    print("Host Portion:", ':'.join(IP[4:]))
    print("Global Internet:", IP[0])
    print("Regional Internet:", IP[1])
    print("Local Internet:", IP[2])
    print("Personal subnet space:", IP[3])
    print("Subnet mask:", Mask)

    if file != None:
        sys.stdout.close()

def ipv6_s(IP: str, file: str | None = None):
    if file != None:
        sys.stdout = open(file, 'w')

    if IP == None:return ValueError("The address argument cannot be empty!")
    IP = re.split(':|%|/', IP)
    if IP[-1] == '' and IP[-2] == '':IP.pop(-1)
    l = len(IP)
    try:
        if l != 8:
            x = 8 - l
            y = IP.index('')
            IP.pop(y)
            for i in range(x+1):IP.insert(y, '0000')
        for i in IP:
            x = len(i)
            if x != 4:
                h = IP.index(i)
                l = 4 - x
                i = str(('0'*l) + i)
                IP.pop(h)
                IP.insert(h, i)
    except ValueError:raise ValueError("Invalid IPv6 address entered!")
    print("Network:", ':'.join(IP[:4]))
    print("Host:", ':'.join(IP[4:]))

    if file != None:
        sys.stdout.close()

def expand(IP: str, Mask: str | None = ...):
    if IP == None:
        return ValueError("The address argument cannot be empty!")

    IP = re.split(':|%|/', IP)

    if IP[-1] == '' and IP[-2] == '':
        IP.pop(-1)
    
    try:
        l = len(IP)
        if l != 8:
            x = 8 - l
            y = IP.index('')
            IP.pop(y)
            for i in range(x+1):
                IP.insert(y, '0000')
        for i in IP:
            x = len(i)
            if x != 4:
                h = IP.index(i)
                l = 4 - x
                i = str(('0'*l) + i)
                IP.pop(h)
                IP.insert(h, i)
    except ValueError:
        raise ValueError("Invalid IPv6 address entered!")

    if Mask == '':
        print("Expanded Notation:", ':'.join(IP))
    else:
        print("Expanded Notation:", ':'.join(IP), '/'+Mask)
def expand_s(IP: str, Mask: str | None = ...):
    if IP == None:return ValueError("The address argument cannot be empty!")
    IP = re.split(':|%|/', IP)
    if IP[-1] == '' and IP[-2] == '':IP.pop(-1)
    l = len(IP)
    try:
        if l != 8:
            x = 8 - l
            y = IP.index('')
            IP.pop(y)
            for i in range(x+1):IP.insert(y, '0000')
        for i in IP:
            x = len(i)
            if x != 4:
                h = IP.index(i)
                l = 4 - x
                i = str(('0'*l) + i)
                IP.pop(h)
                IP.insert(h, i)
    except ValueError:raise ValueError("Invalid IPv6 address entered!")
    if Mask == '':return ':'.join(IP)
    else:return (':'.join(IP), '/'+Mask)

def abbreviate(IP: str, Mask: str | None = ...):
    if IP == None:
        return ValueError("The address argument cannot be empty!")

    IP = re.split(':|%|/', IP)

    if IP[-1] == '' and IP[-2] == '':
        IP.pop(-1)

    try:
        l = len(IP)
        if l != 8:
            x = 8 - l
            y = IP.index('')
            IP.pop(y)
            for i in range(x+1):
                IP.insert(y, '0000')
        for i in IP:
            x = len(i)
            if x != 4:
                h = IP.index(i)
                l = 4 - x
                i = str(('0'*l) + i)
                IP.pop(h)
                IP.insert(h, i)
    except ValueError:
        raise ValueError("Invalid IPv6 address entered!")

    j = []
    s = []
    x = 0
    for i in IP:
        if i == '0000':
            h = IP.index(i)
            j.append(h)
            i = '0'
            IP.pop(h)
            IP.insert(h, i)
        elif re.match("^000", i):
            h = IP.index(i)
            IP.pop(h)
            i = i[3]
            IP.insert(h, i)
        elif re.match("^00", i):
            h = IP.index(i)
            IP.pop(h)
            i = i[2:]
            IP.insert(h, i)
        elif re.match("^0", i):
            h = IP.index(i)
            IP.pop(h)
            i = i[1:]
            IP.insert(h, i)
    j.sort(reverse=True)
    for n in range(len(j)-1):
        if j[n]-1 == j[n+1]:
            s.append(j[n])
            x += 1
        else:
            s.append(j[n])
            continue
    try:
        if j[n+1]+1 == s[-1]:
            s.append(j[-1])
            x += 1
        s = set(s)
        k = len(s) - 1
        for a in range(k):
            sh = len(s) - 1
            p = max(s)
            q = min(s)
            if q == p - sh:
                pass
            else:
                s.remove(p)
                continue
    except IndexError:
        s = set(s)
        
    if x > 0:
        col = '::'
        if Mask == '':print("Compressed Notation:", ":".join(IP[:q]) + col + ":".join(IP[p+1:]))
        else:print("Compressed Notation:", ":".join(IP[:q]) + col + ":".join(IP[p+1:]), "/"+Mask)
    else:
        if Mask == '':print("Compressed Notation:", ":".join(IP))
        else:print("Compressed Notation:", ":".join(IP), "/"+Mask)
def abbreviate_s(IP: str, Mask: str | None = ...):
    if IP == None:return ValueError("The address argument cannot be empty!")
    IP = re.split(':|%|/', IP)
    if IP[-1] == '' and IP[-2] == '':IP.pop(-1)
    l = len(IP)
    try:
        if l != 8:
            x = 8 - l
            y = IP.index('')
            IP.pop(y)
            for i in range(x+1):IP.insert(y, '0000')
        for i in IP:
            x = len(i)
            if x != 4:
                h = IP.index(i)
                l = 4 - x
                i = str(('0'*l) + i)
                IP.pop(h)
                IP.insert(h, i)
    except ValueError:raise ValueError("Invalid IPv6 address entered!")
    j = []
    s = []
    x = 0
    for i in IP:
        if i == '0000':
            h = IP.index(i)
            j.append(h)
            i = '0'
            IP.pop(h)
            IP.insert(h, i)
        elif re.match("^000", i):
            h = IP.index(i)
            IP.pop(h)
            i = i[3]
            IP.insert(h, i)
        elif re.match("^00", i):
            h = IP.index(i)
            IP.pop(h)
            i = i[2:]
            IP.insert(h, i)
        elif re.match("^0", i):
            h = IP.index(i)
            IP.pop(h)
            i = i[1:]
            IP.insert(h, i)
    j.sort(reverse=True)
    for n in range(len(j)-1):
        if j[n]-1 == j[n+1]:
            s.append(j[n])
            x += 1
        else:
            s.append(j[n])
            continue
    try:
        if j[n+1]+1 == s[-1]:
            s.append(j[-1])
            x += 1
        s = set(s)
        k = len(s) - 1
        for a in range(k):
            sh = len(s) - 1
            p = max(s)
            q = min(s)
            if q == p - sh:
                pass
            else:
                s.remove(p)
                continue
    except IndexError:s = set(s)
    if x > 0:
        col = '::'
        if Mask == '':return (":".join(IP[:q]) + col + ":".join(IP[p+1:]))
        else:return (":".join(IP[:q]) + col + ":".join(IP[p+1:]), "/"+Mask)
    else:
        if Mask == '':return (":".join(IP))
        else:return (":".join(IP), "/"+Mask)
