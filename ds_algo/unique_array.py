array=[int(i) for i in input().split(" ")]
l=len(array)
dic={}
for i in range(len(array)):
	while True:
		dic[array[i]]=dic.get(array[i],0)
		if dic[array[i]]>0:
			array[i]+=1
		dic[array[i]]=dic.get(array[i],0)
		if dic[array[i]]==0:
			dic[array[i]]=1
			break
print(array)

# here this can modify an array into array with unique natural numbers by incrementing min

# ex : [2 2 1 1 3] ---> [2 3 1 4 5]
