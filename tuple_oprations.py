'''create a tuple'''
t = ('joker',100,-12,'equal')
print(t)
print(type(t))
'''Now access the item inside a tuple'''
'''to access 1st value'''
print(t[0])
'''to acess last item in tuple'''
print(t[-1])

'''accessing tuple with step size'''
print(t[1::2])

'''Now reverse the tuple using slice method'''
print(t[::-1])

'''tuple cannot be modified'''
# t[2] ='jk'
# # print(t)

'''modify a tuple in simoultaneously'''
a = 'python'
b = 24
print(a,5.369,b)

'''defining a empty tuple '''
t = ()
print(type(t))
t1 = (1,'d',6)
print(type(t1))
t2 = (1,2,3,4)
print(type(t2))

'''defining tuple with singleton'''
t3 = (2)
print(type(t3))
'''it is counted as integer bcz parathensis used for oprator precedence in expressions'''
t4 = (2,)
print(type(t4))
print(t4[0])
print(t4[-1])
print(t4)


