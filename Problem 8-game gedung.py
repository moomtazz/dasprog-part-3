#Masukkan N (tingkatan lantai), M (Energi Gaem), dan K (kasus)
N, M, K=map(int, input().split())
A = []
X = [] #lantai awal
Y = [] #lantai yang ingin dicapai
jumlah = 0
A = list(map(int, input().split()))
for i in range(K) :
    x, y = map(int, input().split()) #terdapat x dan y disetiap kasus (K)
    X.append(x) #memasukkan nilai x ke variabel X
    Y.append(y) #memasukkan nilai y ke variabel Y
    for j in range(x,y) :
        jumlah += A[j-1] #menghitung total energi yang harus dikeluarkan Gaem
if (M>=jumlah):
    print(f"EZ banget, energiku sisa {M-jumlah}!")
else:
    print(f"NT, kurang {jumlah-M} energi sih.")