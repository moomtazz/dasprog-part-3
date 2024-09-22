size_kue = int(input())
spasi = ((size_kue-8)*6)-(2*2)

if size_kue<8:
    print("Too Small")
    
#layer 1
sepasiii = (spasi//2)*" "
print(f"{sepasiii} *")
for i in range(3):
    print(f"{sepasiii}|-|")
print(sepasiii, (((size_kue-8)*2)-1)*"-")

#layer 2
seeepasi = (spasi//4)*" "
bawah2 = ((((size_kue-8)*3)+3)-3)//2
samping2 = ((size_kue-8)*2)-1

for i in range(bawah2):
    layerke2 = "|" + samping2*"=" +"|"
    print(seeepasi,layerke2)
print((((size_kue-8)*6)-(2*2))*"-")

#layer 3
bawah3 = ((((size_kue-8)*3)+3)-3)//2
samping3 = ((size_kue-8)*6)-(2*2)

for j in range(bawah3):
    layerke3 = "|" + samping3*"=" +"|"
    print(layerke3)