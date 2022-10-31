import math
num = int
smPar = int
smPri = int
ctPri = int

vlPri = 0
smPar = 0
smPri = 0
for n in range(1, 4):
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        smPar += num

    for m in range(1, int(math.sqrt(num)+1)):
        if num % m == 0:
            vlPri += 1

    if vlPri == 0:
        smPri += num
print(f"Soma dos números pares: {smPar}")
print(f"Soma dos números primos: {smPri}")