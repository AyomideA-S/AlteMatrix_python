import sys, atexit, io
buffer = io.BytesIO()
sys.stdout.buffer
@atexit.register

def write():
    sys.__stdout__.write(buffer.getvalue().decode("utf-8"))

g = {'0':'1', '1':'0'}
z = []
a = []
def com2(value: int, multiplier: int | None = None, file: str | None = None):
    if file != None:
        sys.stdout = open(file, 'w')

    print('Value:',value)
    print('Binary Value:',bin(value).replace('0b',''))
    if multiplier != None:
        print('Multiplier:',multiplier)
        b = '{:032b}'.format(multiplier)
        print('Binary Multiplier:',b)
        for i in b:
            if i=='1':
                i = g.get(i)
                z.append(i)
            elif i=='0':
                i = g.get(i)
                z.append(i)
        x = ''.join(z)
        print('Inverse:',x)
        x = '0b'+''.join(z)
        x = int(x,2) + 1
        print('Hex Value:',hex(x))

    if file != None:
        sys.stdout.close()

    if multiplier == None:
        multiplier = 1
        mul = value*multiplier
        b = '{:032b}'.format(mul)
        print('32-bit Binary:',b)
        for i in b:
            if i=='1':
                i = g.get(i)
                a.append(i)
            elif i=='0':
                i = g.get(i)
                a.append(i)
        x = ''.join(a)
        print('32-bit Inverse:',x)
        x = '0b'+''.join(a)
        y = x
        x = int(x,2) + 1
        x = hex(x)
        print('Hex Value:',x)
    else:
        mul = value*multiplier
        print('Multiplication:',mul)
        b = '{:032b}'.format(mul)
        print('Binary Multiplication:',b)
        for i in b:
            if i=='1':
                i = g.get(i)
                a.append(i)
            elif i=='0':
                i = g.get(i)
                a.append(i)
        x = ''.join(a)
        print('Inverse Multipliaction:',x)
        x = '0b'+''.join(a)
        y = x
        x = int(x,2) + 1
        x = hex(x)
        print('Hex Multiplication:',x)

def com2_s(value: int, multiplier: int | None = None):
    if multiplier != None:
        b = '{:032b}'.format(multiplier)
        for i in b:
            if i=='1':
                i = g.get(i)
                z.append(i)
            elif i=='0':
                i = g.get(i)
                z.append(i)
        x = ''.join(z)
        x = '0b'+''.join(z)
        x = int(x,2) + 1
    if multiplier == None: multiplier = 1
    mul = value*multiplier
    b = '{:032b}'.format(mul)
    for i in b:
        if i=='1':
            i = g.get(i)
            a.append(i)
        elif i=='0':
            i = g.get(i)
            a.append(i)
    x = ''.join(a)
    x = '0b'+''.join(a)
    y = x
    x = int(x,2) + 1
    x = hex(x)
    return x
