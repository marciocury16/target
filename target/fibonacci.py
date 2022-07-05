n = int(input('Digite um valor e descubra se ele faz parte da sequência Fibonacci: '))
num=1
prox=1


if (n==1) or (n==2):
    print('O valor digitado faz parte da sequênica Fibonacci')
    
else:
    count=3
    while count <= n:
        termo = num + prox
        prox = num
        num = termo
        count += 1
    
    if (termo == n):
        print('O valor faz parte da sequênica Fibonacci')
    else:
        print('O valor não faz parte da sequênica Fibonacci')    