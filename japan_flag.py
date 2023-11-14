import sys
ROW1_L = 8
ROW2_L = 10
ROW3_L = 12
STEP_BW_ROWS = 1
WIDTH = 11
LENGTH = 41


def line_in_circle(row, scaleup=True):
    sys.stdout.write('\u001b[1A')
    if scaleup:
        sys.stdout.write(f'\u001b[{str(row - STEP_BW_ROWS)}D')
    else:
        sys.stdout.write(f'\u001b[{str(row + STEP_BW_ROWS)}D')
    sys.stdout.write('\u001b[41;1m ' * row)


def japan_flag():

    #creates white rectangle
    for i in range(WIDTH):
        print('\u001b[47;1m ' * LENGTH, '\u001b[0m')

    #creates first(bottom) row of the red circle
    sys.stdout.write(f'\u001b[{str(WIDTH//2 - 1)}A')
    sys.stdout.write(f'\u001b[{str(LENGTH//2 - (ROW1_L//2 - 1))}C')
    sys.stdout.write('\u001b[41;1m ' * ROW1_L)

    #creates second row of the red circle
    line_in_circle(ROW2_L)

    #creates third row of the red circle
    line_in_circle(ROW3_L)

    #creates fourth row of the red circle
    line_in_circle(ROW2_L, scaleup=False)

    #creates fifth row of the red circle
    line_in_circle(ROW1_L, scaleup=False)

    #resets terminal settings
    sys.stdout.write(f'\u001b[{str(WIDTH)}B')
    sys.stdout.write('\u001b[0m')

japan_flag()
