cmd,K = map(int, input().split())
kata = []
while True:
    baris=input()
    if baris.lower() == "exit":
        break
    kata.append(baris)
A = list(ord(B) for B in kata) #mengubah alphabet menjadi format ASCII
Limit = K % 90 #batas alphabet hanya 26 huruf

kalimat = ""
for c in range(len(A)): 
    if(kata[c].isalpha()): #untuk elemen berupa alphabet
        if cmd == 1 :
            kalimat+=chr(A[c]+K) #menerjemahkan ke bahasa panda
        else:
            kalimat+=chr(A[c]-K) #menerjemahkan ke bahasa Indonesia
    else:
        kalimat+=kata[c] #elemen non alphabet diprint seadanya
print(kalimat)