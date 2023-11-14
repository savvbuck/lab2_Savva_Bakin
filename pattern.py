import sys


WIDTH = 11
LENGTH = 24

def pattern():

    #creates white rectangle
    for i in range(WIDTH):
        print('\u001b[47;1m ' * LENGTH, '\u001b[0m')

    #creates bottom half of the pattern 
    for i in range(0, WIDTH//2 + 1):
        #creates left half
        sys.stdout.write(f'\u001b[{str(LENGTH//4 + i)}C')
        sys.stdout.write('\u001b[40;1m ')
        sys.stdout.write(f'\u001b[{str(LENGTH//4 + i)}D')
        sys.stdout.write(f'\u001b[{str(LENGTH//4 - i)}C')
        sys.stdout.write('\u001b[40;1m ')
        sys.stdout.write(f'\u001b[{str(LENGTH//4 - i)}D')

        #creates right half
        sys.stdout.write(f'\u001b[{str((LENGTH//4)*3 + i - 4)}C')
        sys.stdout.write('\u001b[40;1m ')
        sys.stdout.write(f'\u001b[{str((LENGTH//4)*3 + i - 4)}D')
        sys.stdout.write(f'\u001b[{str((LENGTH//4)*3 - i - 4)}C')
        sys.stdout.write('\u001b[40;1m ')

        #sets new row
        sys.stdout.write('\u001b[1A')
        sys.stdout.write('\u001b[100D')

    #move cursor up
    sys.stdout.write(f'\u001b[{str(WIDTH - 6)}A')

    #creates upper part of the pattern
    for i in range(0, WIDTH//2 + 1):
        #creates left half
        sys.stdout.write(f'\u001b[{str(LENGTH//4 + i)}C')
        sys.stdout.write('\u001b[40;1m ')
        sys.stdout.write(f'\u001b[{str(LENGTH//4 + i)}D')
        sys.stdout.write(f'\u001b[{str(LENGTH//4 - i)}C')
        sys.stdout.write('\u001b[40;1m ')
        sys.stdout.write(f'\u001b[{str(LENGTH//4 - i)}D')

        #creates right half
        sys.stdout.write(f'\u001b[{str((LENGTH//4)*3 + i - 4)}C')
        sys.stdout.write('\u001b[40;1m ')
        sys.stdout.write(f'\u001b[{str((LENGTH//4)*3 + i - 4)}D')
        sys.stdout.write(f'\u001b[{str((LENGTH//4)*3 - i - 4)}C')
        sys.stdout.write('\u001b[40;1m ')

        #sets new row
        sys.stdout.write('\u001b[1B')
        sys.stdout.write('\u001b[100D')
    #resets terminal settings
    sys.stdout.write(f'\u001b[{str(WIDTH)}B')
    sys.stdout.write('\u001b[0m')

for i in range(10):
    pattern()
