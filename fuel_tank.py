while True:

    fuel = input('Fraction: ')
    
    try:
        x, y = fuel.split('/')
        fraction = int(x) / int(y)
        if fraction <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass


percent = int(fraction * 100)

if percent >= 99:
    print('F')
elif percent <= 1:
    print('E')
else:
    print(f'{percent}%')




