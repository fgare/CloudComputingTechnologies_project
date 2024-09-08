from Generator import Generator

if __name__ == '__main__':
    for i in range(1): # indice customer
        for j in range(1): # indice machine
            Generator(f'customer{i}', f'machine{j}').start()
