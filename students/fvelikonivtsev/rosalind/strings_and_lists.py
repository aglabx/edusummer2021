with open(r'D:\Downloads\rosalind_ini3.txt', 'r') as fr, open('str_list.txt', 'w') as fw:
    string = fr.readline().strip()
    a, b, c, d = map(int, fr.readline().strip().split())
    fw.write(f'{string[a:b + 1]} {string[c:d + 1]}')