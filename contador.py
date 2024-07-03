from time import sleep

def contador(i, f, p):
    cont = i
    while cont <= f:
        print(f'{cont} ', end='', flush=True)
        sleep(0.05)
        cont += p 

contador(0, 1500, 100)
print('FIM')