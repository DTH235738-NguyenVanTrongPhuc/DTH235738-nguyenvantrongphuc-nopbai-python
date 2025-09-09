stars = [1, 3, 7, 3, 5, 11] 

for s in stars:
    spaces = (max(stars) - s) // 2
    print(' ' * spaces + '*' * s)


trunk_spaces = (max(stars) - 3) // 2  
for _ in range(2):
    print(' ' * trunk_spaces + '*' + ' ' + '*')