with open(r'D:\Downloads\rosalind_ini2.txt', 'r') as fr, open('hypoth_square.txt', 'w') as fw:
    for line in fr:
        print(line)
        fw.write(f'{sum(map(lambda x: int(x) ** 2, line.strip().split()))}')
