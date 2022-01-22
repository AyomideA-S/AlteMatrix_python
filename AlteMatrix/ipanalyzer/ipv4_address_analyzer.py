# IPv4 Address Analyzer by AyomideA-S
# NOTE: This code involves knowledge acquired from David Bombal's "Ethical Hacking for Beginners" course on Udemy!
# You can access the course at https://www.udemy.com/course/pratcical-ethical-hacking-for-beginners/?src=sac&kw=Ethical+hacking+for+beginner

import sys, atexit, io
buffer = io.BytesIO()
sys.stdout.buffer
@atexit.register

# write function
def write():
    sys.__stdout__.write(buffer.getvalue().decode("utf-8"))

import re
Masks = {32: "255.255.255.255", 31: "255.255.255.254", 30: "255.255.255.252", 29: "255.255.255.248", 28: "255.255.255.240",
        27: "255.255.255.224", 26: "255.255.255.192", 25: "255.255.255.128", 24: "255.255.255.0", 23: "255.255.254.0",
        22: "255.255.252.0", 21: "255.255.248.0", 20: "255.255.240.0", 19: "255.255.224.0", 18: "255.255.192.0",
        17: "255.255.128.0", 16: "255.255.0.0", 15: "255.254.0.0", 14: "255.252.0.0", 13: "255.248.0.0", 12: "255.240.0.0",
        11: "255.224.0.0", 10: "255.192.0.0", 9: "255.128.0.0", 8: "255.0.0.0", 7: "254.0.0.0", 6: "252.0.0.0",
        5: "248.0.0.0", 4: "240.0.0.0", 3: "224.0.0.0", 2: "192.0.0.0", 1: "128.0.0.0"}

# ipv4 function
def ipv4(IP: str, Subnet: str | None = ..., Mask: str | None = ..., file: str | None = None):
    # checking for a writable file as argument
    if file != None:
        sys.stdout = open(file, 'w')

    if IP == None:
        raise ValueError("The address argument must not be empty!")
    IPv4 = IP.split('.')

    try:
        Mask = int(Mask)
    except (TypeError, ValueError):
        Mask = ''

    NA = '.'.join(IPv4)

    try:
        Subnet = re.split('/|\.', Subnet)
    except (TypeError, ValueError):
        Subnet = ''

    # beginning of output
    print('\n')
    print(" "*19,"IPv4")
    print('|' + '-'*43 + '|')
    print('|',"Octet 1 ","|","Octet 2 ","|","Octet 3 ","|","Octet 4 ",'|')
    IPv4 = list(map(int,IPv4))
    if len(IPv4) != 4:
        raise ValueError("Incorrect IPv4 length format!")
    A,B,C,D = IPv4[0], IPv4[1], IPv4[2], IPv4[3]
    N,E,W,S = '{:08b}'.format(A), '{:08b}'.format(B), '{:08b}'.format(C), '{:08b}'.format(D)
    print('|' + '-'*10 + '|' + '-'*10 + '|' + '-'*10 + '|' + '-'*10 + '|')
    print('|', N,'|',E,'|',W,'|',S,'|')
    print('|' + '-'*43 + '|\n')
    # identifying the class
    if A < 128:cfn = 'A'
    elif A < 192:cfn = 'B'
    elif A < 224:cfn = 'C'
    elif A < 240:cfn = 'D'
    else:cfn = 'E'
    print("Class:",cfn)

    # check if subnet was supplied
    try:
        Subnet = list(map(int,Subnet))
        if len(Subnet) != 4:
            raise ValueError("Incorrect Subnet length format!")
        F,G,H,I = Subnet[0], Subnet[1], Subnet[2], Subnet[3]
        W,X,Y,Z = '{:08b}'.format(F), '{:08b}'.format(G), '{:08b}'.format(H), '{:08b}'.format(I)
        print(" "*15,"Subnet mask")
        print('|' + '-'*43 + '|')
        print('|',"Octet 1 ","|","Octet 2 ","|","Octet 3 ","|","Octet 4 ",'|')
        print('|' + '-'*10 + '|' + '-'*10 + '|' + '-'*10 + '|' + '-'*10 + '|')
        print('|', W,'|',X,'|',Y,'|',Z,'|')
        print('|' + '-'*43 + '|')
    except:
        pass

    # check if subnet mask was supplied
    if Mask != '':
        print("This is a", str(Mask) + "-bit subnet mask.")
        h = 32 - Mask
        print("Host Bits:", h)
        J = 2**h - 2
        print("Number of supported Hosts:", J)
        print("Total IPs:", J+2)

    # analyzing ipv4 address
    try:
        if '0' in W:x,y=F,A
        elif '0' in X:x,y=G,B
        elif '0' in Y:x,y=H,C
        elif '0' in Z:x,y=I,D
        l = 256 - x
        print("Block Size:", l)
        print("Subnets:", 256//l)

        for f in range(0,257,l):
            if f > y:
                break
        z = IPv4.index(y)
        if z == 3:
            IPv4.pop(-1)
            IPv4.append(1)
            IPv4 = list(map(str,IPv4))
            alpha = ".".join(IPv4)

            IPv4.pop(z)
            IPv4.insert(z, f-1)
            IPv4 = list(map(str,IPv4))
            delta = ".".join(IPv4)

            hax = int(IPv4[z])
            IPv4.pop(z)
            IPv4.insert(z, hax-1)
            IPv4 = list(map(str,IPv4))
            gamma = ".".join(IPv4)
        else:
            IPv4.pop(z)
            IPv4.pop(-1)
            IPv4.insert(z, 0)
            IPv4.append(1)
            IPv4 = list(map(str,IPv4))
            alpha = ".".join(IPv4)

            IPv4.pop(z)
            IPv4.pop(-1)
            IPv4.insert(z, f-1)
            IPv4.append(255)
            IPv4 = list(map(str,IPv4))
            delta = ".".join(IPv4)

            hax = int(IPv4[-1])
            IPv4.pop(-1)
            IPv4.append(hax-1)
            IPv4 = list(map(str,IPv4))
            gamma = ".".join(IPv4)
    except:
        pass

    Subnet = list(map(str,Subnet))
    print("Network Address:", NA)
    print("Subnet Address:",'.'.join(Subnet))
    try:
        print("Directed Broadcast Address:", delta)
        print("IP Range:",alpha,'-',gamma)
        print("Wildcard Bits:",'0.0.0.'+str(f-1))
    except:
        pass
    print("Subnet mask:",Masks.get(Mask,Mask))
    # end of output

    # close file
    if file != None:
        sys.stdout.close()

# silent ipv4 function
def ipv4_s(IP: str, Subnet: str | None = ..., Mask: str | None = ..., file: str | None = None):
    # checking for a writable file as argument
    if file != None:
        sys.stdout = open(file, 'w')
    
    if IP == None:
        raise ValueError("The address argument must not be empty!")
    IPv4 = IP.split('.')

    try:
        Mask = int(Mask)
    except (TypeError, ValueError):
        Mask = ''

    NA = '.'.join(IPv4)

    try:
        Subnet = re.split('/|\.', Subnet)
    except (TypeError, ValueError):
        Subnet = ''

    # beginning of output
    print('\n')
    print(" "*19,"IPv4")
    print('|' + '-'*43 + '|')
    print('|',"Octet 1 ","|","Octet 2 ","|","Octet 3 ","|","Octet 4 ",'|')
    IPv4 = list(map(int,IPv4))
    if len(IPv4) != 4:raise ValueError("Incorrect IPv4 length format!")
    A,B,C,D = IPv4[0], IPv4[1], IPv4[2], IPv4[3]
    N,E,W,S = '{:08b}'.format(A), '{:08b}'.format(B), '{:08b}'.format(C), '{:08b}'.format(D)
    print('|' + '-'*10 + '|' + '-'*10 + '|' + '-'*10 + '|' + '-'*10 + '|')
    print('|', N,'|',E,'|',W,'|',S,'|')
    print('|' + '-'*43 + '|\n')

    # check if subnet was supplied
    try:
        Subnet = list(map(int,Subnet))
        if len(Subnet) != 4:raise ValueError("Incorrect Subnet length format!")
        F,G,H,I = Subnet[0], Subnet[1], Subnet[2], Subnet[3]
        W,X,Y,Z = '{:08b}'.format(F), '{:08b}'.format(G), '{:08b}'.format(H), '{:08b}'.format(I)
        print(" "*15,"Subnet mask")
        print('|' + '-'*43 + '|')
        print('|',"Octet 1 ","|","Octet 2 ","|","Octet 3 ","|","Octet 4 ",'|')
        print('|' + '-'*10 + '|' + '-'*10 + '|' + '-'*10 + '|' + '-'*10 + '|')
        print('|', W,'|',X,'|',Y,'|',Z,'|')
        print('|' + '-'*43 + '|')
    except:
        pass

    # check if subnet mask was supplied
    if Mask != '':
        h = 32 - Mask
        print("Bits:",h)
        J = 2**h - 2
        print("Hosts:", J)
        print("IPs:", J+2)
    try:
        if '0' in W:x,y=F,A
        elif '0' in X:x,y=G,B
        elif '0' in Y:x,y=H,C
        elif '0' in Z:x,y=I,D
        l = 256 - x
        print("Size:", l)
        print("Subnets:", 256//l)
    except:
        pass
    print(Masks.get(Mask,Mask))
    # end of output

    # close file
    if file != None:
        sys.stdout.close()
