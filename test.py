msg = input('enter your meaasage: ')
shift_value = int(input('enter value to shift alphabets: '))

cipher = '' 
for char in msg:
    if char.isalpha():
        code = ord(char) + shift_value
        if code > ord('z'):
            if shift_value > 1:
                code = ord('a') + (shift_value - 1)
        else:
            code = ord('a')
    elif char.isalnum():
        code += 'char'   
    #code = ord(char) + shift_value
    # if code > ord('z'):
    #     if shift_value > 1:
    #         code = ord('a') + (shift_value - 1)
    #     else:
    #         code = ord('a')
    cipher += code
print(cipher) 
