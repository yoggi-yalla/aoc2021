import math

with open('input.txt') as f:
    data = f.read()


nums = [int(x, base=16) for x in data]
bits = "".join((bin(num).replace('0b', '').zfill(4) for num in nums))


def parse_literal(bits):
    ret = ""
    pos = 0
    while 1:
        ret += bits[pos+1:pos+5]
        pos += 5
        if bits[pos-5] == "0":
            break
    return int(ret, base=2), pos


def parse_packet(bits):
    pos = 0
    packet_version = int(bits[pos:pos+3], base=2)
    pos += 3
    
    packet_type = int(bits[pos:pos+3], base=2)
    pos += 3

    if packet_type == 4:
        literal, length = parse_literal(bits[pos:])
        pos += length

    else:
        length_type_id = int(bits[pos], base=2)
        pos += 1

        if length_type_id == 0:
            sub_packet_length = int(bits[pos:pos+15], base=2)
            pos += 15
            end = pos + sub_packet_length
            
            literals = []
            while pos < end:
                literal, length, sub_version = parse_packet(bits[pos:])
                packet_version += sub_version
                literals.append(literal)
                pos += length

        else:
            nbr_of_subpackets = int(bits[pos:pos+11], base=2)
            pos += 11

            literals = []
            for _ in range(nbr_of_subpackets):
                literal, length, sub_version = parse_packet(bits[pos:])
                packet_version += sub_version
                literals.append(literal)
                pos += length
            
        if packet_type == 0:
            literal = sum(literals)
        elif packet_type == 1:
            literal = math.prod(literals)
        elif packet_type == 2:
            literal = min(literals)
        elif packet_type == 3:
            literal = max(literals)
        elif packet_type == 5:
            literal = int(literals[0] > literals[1])
        elif packet_type == 6:
            literal = int(literals[0] < literals[1])
        elif packet_type == 7:
            literal = int(literals[0] == literals[1])
    
    return literal, pos, packet_version


literal, length, packet_version = parse_packet(bits)

print("Part 1:", packet_version) # 852
print("Part 2:", literal) # 19348959966392
