'''tinggisegitiga = int(input())
for i in range(tinggisegitiga):
    print ("*"*(tinggisegitiga-i))'''

U = int(input())
K = int(input())
M = int(input())

SM = M//2
SK = K//2
RI = 100

G1 = U - SK*2
G2 = G1 - (SM*5)*5
G3 = G2 - RI * 10

if G3 > 0:
    print(f"Yey! Ucup Menang! HP tersisa: {G3}")

else:
    print("Yah! Ucup Meninggoy.")