def function_graph():

    width = 10
    length = 10

    plain = [['  .  ' for i in range(width)] for i in range(length)] #sets plain of '.'

    for i in range(width):
        for j in range(length):
            if j == 0:
                plain[i][j] = f'  {str(i)}  ' #sets vertical number line
            if i == 0:
                plain[i][j] = f'  {str(j)}  ' #sets horizontal number line
            if i == 3 * j:
                plain[i][j] = '   //'

    
    for i in range(width):
        print(''.join(plain[width - 1 - i])) #prints list's containments, but in reverse order
        print('')


function_graph()
