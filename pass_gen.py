import random


array_a = list('abcdefghijklmnopqrstuvwxyz')
array_A = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
array_n = list('1234567890')
array_s = list('-_=+*[].,')


def help():
    print('')
    print('============== HELP ================')
    print('This simple script generates a word, which you can')
    print('use as an unique login or password. Inputs requied -')
    print('two words. First word is an array of atributes, that ')
    print('will rule the result's strength. Second word - is result's')
    print('length. ')
    print('Available arguments (their order does not matter:')
    print('a - include small letters, from a to z')
    print('A - include big letters, from A to Z')
    print('n - include numbers from 0 to 9')
    print('s - include special symblos, such as -_=+*[].,')
    print('For example, >> naA 14 will return result small, big letters')
    print('and numbers and will have length = 14')
    print('=============== END ================')
    print('')


def generate():
    target_array = list()
    print('Input keys and length, separate with space')
    print('Keys = a, A, n, s')
    input_text = input('>> ')
    end = False
    length = 0
    password = ''

    while end == False:
        if input_text[:1] == 'a':
            target_array = target_array + array_a
            input_text = input_text[1:]
        elif input_text[:1] == 'A':
            target_array = target_array + array_A
            input_text = input_text[1:]
        elif input_text[:1] == 'n':
            target_array = target_array + array_n
            input_text = input_text[1:]
        elif input_text[:1] == 's':
            target_array = target_array + array_s
            input_text = input_text[1:]
        elif input_text[:1] == ' ':
            length = int(input_text[1:])
            input_text = ''
            end = True
        else:
            print('Error!')
            break

    for i in range(length):
        password += random.choice(target_array)

    print('Result = ', password)
    return 1

print('Easygen v1.0 from Renderhauer')
help()


generate()

while True:
    src = input('Generate one more time? y/n (h for help): ')
    if src[:1] == 'y' or src[:1] == 'Y':
        generate()
    if src[:1] == 'h' or src[:1] == 'H':
        help()
    else:
        print('Good hunting!')
        break