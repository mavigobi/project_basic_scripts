# autora: mavigobi

def multiplicate(a,b):
    return a*b

def main():
    x = float(input('Inserte un número tipo float:')) #inicialmente los inputs se leen como string
    y = float(input('Inserte otro número tipo float:'))
    result = multiplicate(x,y)
    print(f'La solución a la multiplicación es: {result}') 
    #print('La solución a la multiplicación es:', result) || otra forma de exponerlo por pantalla
if __name__ == '__main__':
    main()