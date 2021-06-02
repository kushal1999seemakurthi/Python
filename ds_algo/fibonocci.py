def fib(n,f):
	if(n==1): return 1
	elif(n==2): return 2
	elif(n==3): return 3
	elif(n==4): return 5
	elif(n==5): return 8
	try:
		return f[n]

	except:
		if(n%2==0):
			a=fib(int(n/2),f)**2 + fib(int(n/2)-1,f)**2
			# print(a,"----ineven---")

		elif(n%2==1):
			a=fib(int((n+1)/2),f)*fib(int((n-1)/2),f)+fib(int((n-1)/2),f)*fib(int((n-3)/2),f)
			# print(a,"----inodd---")
		f[n]=a
		return a



f={1:1 , 2:2 , 3:3 , 4:5 , 5:8}
i=48-6
# print(fib(i,f),i+1)
for i in range(3,52):
    print("  i== ",i,"  and the fib == ",fib(i,f))

# class solu:

# 	def fib(self,n,f):
# 		if(n==1): return 1
# 		elif(n==2): return 2
# 		elif(n==3): return 3
# 		elif(n==4): return 5
# 		elif(n==5): return 8
# 		try:
# 			return f[n]

# 		except:
# 			if(n%2==0):
# 				a=fib(int(n/2),f)**2 + fib(int(n/2)-1,f)**2
# 				# print(a,"----ineven---")

# 			elif(n%2==1):
# 				a=fib(int((n+1)/2),f)*fib(int((n-1)/2),f)+fib(int((n-1)/2),f)*fib(int((n-3)/2),f)
# 				# print(a,"----inodd---")
# 			f[n]=a
# 			return a

# 	def solve(self,n):
# 		f={1:1 , 2:2 , 3:3 , 4:5 , 5:8}
# 		return self.fib(n,f)

# a=solu()
# print(a.solve(i)-fib(i,f))
