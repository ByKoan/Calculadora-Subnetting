# IP y Mascara de RED
def Int2Bin(integer):
    binary = '.'.join([bin(int(x)+256)[3:] for x in integer.split('.')])
    return binary

print('\nCalculadora SUBNETTING made by Koan')
IP = input('Introduce una direccion IP valida: ')
Subnet = input('Introduce una mascara de red Valida: ')
IP_binary = Int2Bin(IP)
Subnet_binary = Int2Bin(Subnet)

print('\nIP:', IP, "->", IP_binary)
print('Subnet:', Subnet, "->", Subnet_binary)

# AND (Broadcast)
def complement(number):
    if number == '0':
        number = '1'
    elif number == '.':
        pass
    else:
        number = '0'
    return number

def find_and_broadcast(binary_subnet):
    binary_list = list(binary_subnet)
    and_broadcast = ''.join(complement(binary_list[y]) for y in range(len(binary_list)))
    return and_broadcast

def convert_decimal(and_broadcast_Binary):
    binary = {}
    for x in range(4):
        binary[x] = int(and_broadcast_Binary.split(".")[x], 2)
    dec = ".".join(str(binary[x]) for x in range(4))
    return dec

and_broadcast_binary = find_and_broadcast(Int2Bin(Subnet))
and_broadcast = convert_decimal(and_broadcast_binary)
print('AND (Broadcast):', and_broadcast, '->', and_broadcast_binary)

# Identificador de RED
def andOP(IP1, IP2):
    ID_list = {}
    for y in range(4):
        ID_list[y] = int(IP1.split(".")[y]) & int(IP2.split(".")[y])
    ID = ".".join(str(ID_list[z]) for z in range(4))
    return ID

Identificadorred = andOP(IP, Subnet)
network_Binary = Int2Bin(Identificadorred)
print('Identificador de RED:', Identificadorred, "->", network_Binary)

# IP de Broadcast
def orOP(IP1, IP2):
    Broadcast_list = {}
    for z in range(4):
        Broadcast_list[z] = int(IP1.split(".")[z]) | int(IP2.split(".")[z])
    broadcast = ".".join(str(Broadcast_list[c]) for c in range(4))
    return broadcast

broadcastIP = orOP(Identificadorred, and_broadcast)
broadcastIP_binary = Int2Bin(broadcastIP)
print('IP De Broadcast:', broadcastIP, "->", broadcastIP_binary)

# Max IP
def maxiIP(brdcstIP):
    maxIPs = brdcstIP.split(".")
    if int(brdcstIP.split(".")[3]) - 1 == 0:
        if int(brdcstIP.split(".")[2]) - 1 == 0:
            if int(brdcstIP.split(".")[1]) - 1 == 0:
                maxIPs[0] = int(brdcstIP.split(".")[0]) - 1
            else:
                maxIPs[1] = int(brdcstIP.split(".")[1]) - 1
        else:
            maxIPs[2] = int(brdcstIP.split(".")[2]) - 1
    else:
        maxIPs[3] = int(brdcstIP.split(".")[3]) - 1
    return ".".join(str(maxIPs[x]) for x in range(4))

maxIP = maxiIP(broadcastIP)
maxIP_binary = Int2Bin(maxIP)
print('Rango maximo de IP:', maxIP, "->", maxIP_binary)

# Min IP
def miniIP(ntwrkID):
    miniIPs = ntwrkID.split(".")
    if int(ntwrkID.split(".")[3]) + 1 == 256:
        if int(ntwrkID.split(".")[2]) + 1 == 256:
            if int(ntwrkID.split(".")[1]) + 1 == 256:
                miniIPs[0] = int(ntwrkID.split(".")[0]) + 1
                miniIPs[1] = 0
                miniIPs[2] = 0
                miniIPs[3] = 0
            else:
                miniIPs[1] = int(ntwrkID.split(".")[1]) + 1
                miniIPs[2] = 0
                miniIPs[3] = 0
        else:
            miniIPs[2] = int(ntwrkID.split(".")[2]) + 1
            miniIPs[3] = 0
    else:
        miniIPs[3] = int(ntwrkID.split(".")[3]) + 1
    return ".".join(str(miniIPs[x]) for x in range(4))

minIP = miniIP(Identificadorred)
minIP_binary = Int2Bin(Identificadorred)
print('Rango minimo de IP:', minIP, "->", minIP_binary)
