stars = [1, 3, 7, 3, 5, 11, 2, 2]

for s in stars:
    spaces = (max(stars) - s) // 2
    print(' ' * spaces + '*' * s)