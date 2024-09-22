cmd,K = map(int, input().split())

kata = (input())
A = list(ord(B) for B in kata) #mengubah alphabet menjadi format ASCII
Limit = K % 26 #batas alphabet hanya 26 huruf

kalimat = ""
for c in range(len(A)): 
    if(kata[c].isalpha() or kata[c] == ""): #untuk elemen berupa alphabet
        if cmd == 1 :
            kalimat+=chr(A[c]+K) #menerjemahkan ke bahasa panda
        else:
            kalimat+=chr(A[c]-K) #menerjemahkan ke bahasa Indonesia
    else:
        kalimat+=kata[c] #elemen non alphabet diprint seadanya
print(kalimat)