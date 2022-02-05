sound = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
'''
def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')

def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
'''
def decode_bits(bits):
    bits = bits.strip('0')
    if '0' not in bits:
        return '.'
    intervel_code = set()
    msg = []
    tmp = ''
    mode = 1
    index = 0
    while index < len(bits):
        if bits[index] == '1':
            if mode == 0:
                intervel_code.add(tmp)
                msg.append(tmp)
                tmp = ''
            tmp += bits[index]
            mode = 1
            if index == len(bits) - 1:
                intervel_code.add(tmp)
                msg.append(tmp)
        else:
            if mode == 1:
                intervel_code.add(tmp)
                msg.append(tmp)
                tmp = ''
            tmp += bits[index]
            mode = 0
        index += 1
    
    len_sorting = lambda st : len(st)

    interval_dict = dict.fromkeys(intervel_code)
    unit = len(sorted(intervel_code, key=len_sorting)[0])
    for code in sorted(intervel_code):
        if code[0] == '0' and len(code) == unit:
            interval_dict[code] = ''
        elif code[0] == '0':
            interval_dict[code] = ' ' * (len(code) // unit)
        elif code[0] == '1' and len(code) == unit:
            interval_dict[code] = '.'
        elif code[0] == '1':
            interval_dict[code] = '-'
    #return interval_dict
    return ''.join(interval_dict[msg[i]] for i in range(len(msg)))


def decode_morse(morsecode):
    words = morsecode.split('       ')
    word = [wo.split('   ') for wo in words]
    msg = ''
    for wor in word:
        for letter in wor:
            msg += letter
        msg += ' '
    return msg.strip()

#print(decode_bits(sound))

def new_decode_bits(bits):
    bits = bits.strip('0')
    code = dict()
    msg = []
    tmp = ''
    
    for i, bit in enumerate(bits):
        if i == 0:
            tmp += bit
            continue
        else:
            if bits[i - 1] != bit:
                msg.append(tmp)
                code[tmp] = ''
                tmp = ''
                tmp += bit
            else:
                tmp += bit 
        if i == len(bits) - 1:
            msg.append(tmp)
            code[tmp] = ''

    len_sorting = lambda bit : len(bit)
    unit = len(sorted(msg, key=len_sorting)[0])
    for key in code:
        if key[0] == '0' and len(key) == unit:
            code[key] = ''
        elif key[0] == '0':
            code[key] = ' ' * (len(key) // unit)
        elif key[0] == '1' and len(key) == unit:
            code[key] = '.'
        elif key[0] == '1':
            code[key] = '-'
            
    return ''.join(code[msg[i]] for i in range(len(msg)))

print(new_decode_bits(sound))