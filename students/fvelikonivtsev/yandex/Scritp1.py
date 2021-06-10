import sys

stdin = iter(sys.stdin)
current_temp, conditioner_tem = next(stdin).strip().split()
print(current_temp, conditioner_tem)
mode = next(stdin).strip()


def conditioner(temp1, temp2, mode_):
    decisions = {'auto': temp2,
                 'fan': temp1,
                 'heat': max(temp1, temp2),
                 'freeze': min(temp1, temp2)}

    return str(decisions[mode_])


sys.stdout.write(conditioner(current_temp, conditioner_tem, mode))