with open(r'D:\Downloads\rosalind_ini5.txt', 'r') as fr, open(f'{__file__[:-3]}.txt', 'w') as fw:
    for index, string in enumerate(fr):
        if index % 2:
            fw.write(string)