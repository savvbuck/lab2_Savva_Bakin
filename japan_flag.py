import sys


def japan_flag():
    
    row1_l = 8
    row2_l = 10
    row3_l = 12
    step_bw_rows = 1
    width = 11
    length = 41

    #creates white rectangle
    for i in range(width):
        print(u'\u001b[47;1m ' * length, u'\u001b[0m')

    #creates first(bottom) row of the red circle
    sys.stdout.write(u'\u001b[' + str(width//2 - 1) + 'A')
    sys.stdout.write(u'\u001b[' + str(length//2 - (row1_l//2 - 1)) + 'C')
    sys.stdout.write(u'\u001b[41;1m ' * row1_l)

    #creates second row of the red circle
    sys.stdout.write(u'\u001b[1A')
    sys.stdout.write(u'\u001b[' + str(row2_l - step_bw_rows) + 'D')
    sys.stdout.write(u'\u001b[41;1m ' * row2_l)

    #creates third row of the red circle
    sys.stdout.write(u'\u001b[1A')
    sys.stdout.write(u'\u001b[' + str(row3_l - step_bw_rows) + 'D')
    sys.stdout.write(u'\u001b[41;1m ' * row3_l)

    #creates fourth row of the red circle
    sys.stdout.write(u'\u001b[1A')
    sys.stdout.write(u'\u001b[' + str(row2_l + step_bw_rows) + 'D')
    sys.stdout.write(u'\u001b[41;1m ' * row2_l)

    #creates fifth row of the red circle
    sys.stdout.write(u'\u001b[1A')
    sys.stdout.write(u'\u001b[' + str(row1_l + step_bw_rows) + 'D')
    sys.stdout.write(u'\u001b[41;1m ' * row1_l)

    #resets terminal settings
    sys.stdout.write(u'\u001b[' + str(width) + 'B')
    sys.stdout.write(u'\u001b[0m')

japan_flag()