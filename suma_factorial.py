#11/02/22
def suma_factorial(n):
    s = ""

    for i in range(1, n+1):
        s += " "+str(i)+"+ "
 
    
    if n >= 1:
        print(s)
        suma_factorial(n-1)
   
    

if __name__ == "__main__":
    n = int(input('Introduce un número para calcular la suma factorial: '))
    suma_factorial(n)
