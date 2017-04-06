# This snippet prints out a list of multiples of 3 and 5 between 3 and x 

x = 10
y = sorted(list(set().union(range(3,x+1,3),range(5,x+1,5))))
print y
