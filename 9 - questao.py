
import os

ida: int
smIda: int
pesmai90altmen150: int
ida10e30Alt190: int
pes: float
alt: float
med: float

pesoSuperior90alturaInferior150 = 0
somIda = 0
ida10e30Alt190 = 0

for n in range(0, 10):
    print(f"Dados para {n+1}ª pessoa:")
    
    ida = int(input("Informe a idade: "))
    pes = float(input("Informe o peso: "))
    alt = float(input("Informe a altura: "))

    os.system("cls")
    smIda = smIda + ida
   
    if (pes > 90) and (alt < 1.50):
        pesmai90altmen150 += 1
    if (ida >= 10 and ida <= 30) and alt > 1.90:
        ida10e30Alt190 += 1

medIda = somIda / 10

print(f"Média das idades das dez pessoas: {medIda:.2f}")
print(
    f"Quantidade de pessoas com peso superior a 90 kg e altura inferior a 1,50 metro: {pesmai90altmen150}m.")
print(
    f"Porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90 m: {ida10e30Alt190/10*100:.1f}%.")