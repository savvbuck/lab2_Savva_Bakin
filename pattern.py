import sys


def pattern():

    width = 11
    length = 24

    #creates white rectangle
    for i in range(width):
        print(u'\u001b[47;1m ' * length, u'\u001b[0m')

    #creates bottom half of the pattern 
    for i in range(0, width//2 + 1):
        #creates left half
        sys.stdout.write(u'\u001b[' + str(length//4 + i) + 'C')
        sys.stdout.write(u'\u001b[40;1m ')
        sys.stdout.write(u'\u001b[' + str(length//4 + i) + 'D')
        sys.stdout.write(u'\u001b[' + str(length//4 - i) + 'C')
        sys.stdout.write(u'\u001b[40;1m ')
        sys.stdout.write(u'\u001b[' + str(length//4 - i) + 'D')

        #creates right half
        sys.stdout.write(u'\u001b[' + str((length//4)*3 + i - 4) + 'C')
        sys.stdout.write(u'\u001b[40;1m ')
        sys.stdout.write(u'\u001b[' + str((length//4)*3 + i - 4) + 'D')
        sys.stdout.write(u'\u001b[' + str((length//4)*3 - i - 4) + 'C')
        sys.stdout.write(u'\u001b[40;1m ')

        #sets new row
        sys.stdout.write(u'\u001b[1A')
        sys.stdout.write(u'\u001b[100D')

    #move cursor up
    sys.stdout.write(u'\u001b[' + str(width - 6) + 'A')

    #creates upper part of the pattern
    for i in range(0, width//2 + 1):
        #creates left half
        sys.stdout.write(u'\u001b[' + str(length//4 + i) + 'C')
        sys.stdout.write(u'\u001b[40;1m ')
        sys.stdout.write(u'\u001b[' + str(length//4 + i) + 'D')
        sys.stdout.write(u'\u001b[' + str(length//4 - i) + 'C')
        sys.stdout.write(u'\u001b[40;1m ')
        sys.stdout.write(u'\u001b[' + str(length//4 - i) + 'D')

        #creates right half
        sys.stdout.write(u'\u001b[' + str((length//4)*3 + i - 4) + 'C')
        sys.stdout.write(u'\u001b[40;1m ')
        sys.stdout.write(u'\u001b[' + str((length//4)*3 + i - 4) + 'D')
        sys.stdout.write(u'\u001b[' + str((length//4)*3 - i - 4) + 'C')
        sys.stdout.write(u'\u001b[40;1m ')

        #sets new row
        sys.stdout.write(u'\u001b[1B')
        sys.stdout.write(u'\u001b[100D')
    #resets terminal settings
    sys.stdout.write(u'\u001b[' + str(width) + 'B')
    sys.stdout.write(u'\u001b[0m')

for i in range(10):
    pattern()
