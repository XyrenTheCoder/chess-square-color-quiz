import random

files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] #a-h

def generate_square():
    file = random.choice(files)
    rank = random.randint(1, 8)

    for i in files:
        if files.index(i) % 2 == 0:
            color = 'dark'
        else:
            color = 'light'
        if file == i:
            break

    if rank % 2 == 0:
        if color == 'dark':
            color = 'light'
        elif color == 'light':
            color = 'dark'
    else:
        pass
    return file, rank, color

def Main():
    file, rank, color = generate_square()
    ans = str(input(f'What color is {file}{rank}?\n>> ')).lower()
    if ans == 'idk':
        print(f'{file}{rank} was a {color} square :(')
    elif ans != 'dark' and ans != 'light':
        print('Dude answer with "dark" or "light", are you stupid? >:(')
    elif ans == color:
        print('Correct!!')
        return Main()
    else:
        print(f'Incorrect, {file}{rank} was a {color} square :(')

Main()
