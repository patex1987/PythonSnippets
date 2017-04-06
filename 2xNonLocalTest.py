# These are workarounds for python 3.X nonlocal 

# Solution nr.1
def outer(start):
    d = {'y' : start}
    def inner():
        d['y'] += 1
        return d['y']
    return inner

f = outer(6)
g = outer(10)
print(f(),g(),g(), f(), f())

# Solution nr.2, ugly solution. Every function is an object. So every function can have attributes
def outer2(start):
    def inner():
        inner.y += 1
        return inner.y
    inner.y = start
    return inner

f = outer2(6)
g = outer2(10)
print(f(),g(),g(), f(), f())
print f.y

# Solution nr.3, using classes. 
class outer3:
	def __init__(self,start):
		self.state = start
	def inner(self):
		self.state += 1
		return self.state
		
f = outer3(6)
g = outer3(10)
print (f.inner(),g.inner(),g.inner(),f.inner(),f.inner())

# Solution nr.4, classes __call__ overloading
class outer4:
	def __init__(self,start):
		self.state = start
	def __call__(self):
		self.state += 1
		return self.state

f = outer4(6)
g = outer4(10)
print (f(),g(),g(), f(), f())