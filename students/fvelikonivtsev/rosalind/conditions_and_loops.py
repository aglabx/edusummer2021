with open(r'D:\Downloads\rosalind_ini4.txt', 'r') as fr, open('cond_loops.txt', 'w') as fw:
    a, b = map(int, fr.read().strip().split())
    fw.write(f'{sum(integer for integer in range(a, b + 1) if integer % 2)}')
