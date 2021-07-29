pi = 3.14
diameter = input('Please type in  a measurment: ')
diameter = float(diameter)
mea_type = input('(D)diameter or (R)radius? ')
type = input('(m)Meters or (cm)Centimers? ')
cal = diameter * pi
if mea_type == 'D':
    if type == 'm':
        re_cal = cal * 100
        print(f"Circumference is {cal}m also {re_cal}cm.")
    elif type == 'cm':
        re_cal = cal / 100
        print(f"Circumference is {cal}cm also {re_cal}m.")
    else:
        print('''
        Something went wrong.
        Please just type m or cm.
        ''')
elif mea_type == 'R':
    if type == 'm':
        re_cal = cal * 100 * 2
        print(f"Circumference is {cal}m also {re_cal}cm.")
    elif type == 'cm':
        re_cal = cal / 100 * 2
        print(f"Circumference is {cal}cm also {re_cal}m.")
    else:
        print('''
            Something went wrong.
            Please just type m or cm in question two.
            ''')