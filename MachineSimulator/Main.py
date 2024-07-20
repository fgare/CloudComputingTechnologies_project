from MachineSimulator.Generator import Generator

if __name__ == '__main__':
    for i in range(5):
        for j in range(10):
            Generator(f'customer{i}', f'machine{j}').start()
