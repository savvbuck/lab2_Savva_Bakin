WIDTH = 10
LENGTH = 10 

def function_graph():

    plain = [['  .  ' for i in range(WIDTH)] for i in range(LENGTH)] #sets plain of '.'

    for i in range(WIDTH):
        for j in range(LENGTH):
            if j == 0:
                plain[i][j] = f'  {str(i)}  ' #sets vertical number line
            if i == 0:
                plain[i][j] = f'  {str(j)}  ' #sets horizontal number line
            if i == 3 * j:
                plain[i][j] = '   //'

    
    for i in range(WIDTH):
        print(''.join(plain[WIDTH - 1 - i])) #prints list's containments, but in reverse order
        print('')


function_graph()
