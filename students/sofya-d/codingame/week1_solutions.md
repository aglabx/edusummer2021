#Task1
var = input()
ans = ""
for i in range(len(var)):
    if var[i] == "_":
        ans = var[:i] + var[i + 1].upper() + var[(i + 2):len(var)]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(ans)

#Task2
h = int(input())

answer = h * 2 ** 6
print(answer)
