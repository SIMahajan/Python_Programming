#update dictionary
Sample1={0:10,1:20}
print(Sample1) 
Sample1.update({2:30,3:40})
print(Sample1)

dic1={1:10,2:20}
dic2={3:10,4:20}
dic3={5:10,6:20}
dic4={}
for i in (dic1,dic2,dic3):
    dic4.update(i)
print(dic4)


