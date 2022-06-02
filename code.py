msg = input('enter your meaasage: ')
shift_value = int(input('enter value to shift alphabets: '))

cipher = ''
for char in msg:
    if not char.isalpha():
        continue
    code = ord(char) + shift_value
    #if shift_value > 1:
    if code > ord('z'):
        if shift_value > 1:
            code = ord('a') + (shift_value - 1)
        else:
            code = ord('a')
    cipher += chr(code) 
print(cipher) 
