import time

from Generator import Generator

if __name__ == '__main__':
    for i in range(5): # indice customer
        for j in range(10): # indice machine
            Generator(f'customer{i}', f'machine{j}').start()
            time.sleep(0.1)
