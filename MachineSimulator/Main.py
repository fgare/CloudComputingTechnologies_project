from MachineSimulator.Generator import Generator

if __name__ == '__main__':
    for i in range(1):
        for j in range(1):
            Generator(f'customer{i}', f'machine{j}').start()
