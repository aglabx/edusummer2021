with open(r'D:\Downloads\rosalind_ini6(1).txt', 'r') as fr, open(f'{__file__[:-3]}.txt', 'w') as fw:
    words = {}
    for line in fr:
        for word in line.strip().split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    to_write = (f'{word} {words[word]}\n' for word in words)

    fw.writelines(to_write)
