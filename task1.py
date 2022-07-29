x = int(input('введіть рік: '))

def is_year_lead(x):
    if x % 4 == 0 and x % 100 != 0:
        print('цей рік високосний, у ньому 366 днів')
    else: 
        print('у цьому році 365 днів')

is_year_lead(x)