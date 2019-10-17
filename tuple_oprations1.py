'''''packing and unpacking in tuple'''
'''tuple packing'''
t = ('python','java','Aws')
print(t[0])
print(t[-1])
'''this is packed tuple'''
''''''''''now unpck the tuple'''

a,b,c=t
print(a)
print(b)
print(c)

''''Another way of unpacking'''
(s1,s2,s3) = t
print(s1)
print(s2)
print(s3)

#Note
'''need to pass number required value as presestn in items of tuple'''
# (v1,v2)= t
# print(v1)
# #Cannot pass less value
# (g1,g2,g3,g4)=t
# #can not pass more values
# print(g1)

''''packing and unpacking compound assign ment '''
(g1,g2,g3)=('dev',10,'aws')
print(g1)
print(type(g1))
#Now its string as op

'''creating tuple without using ()'''
tup = 1,2,'mk'
print(tup)
print(type(tup))
(l1,l2,l3) = tup
print(l1,l2,l3)
# print(type(l1,l2,l3))
(l1,l2,l3)= 456,4,5
'''creating singleton Tuple'''
h1 = 2
print(type(h1))
h2 = 2,
print(h2)
print(type(h2))

'''unpacking tuple without pass require numb of values'''
(f1,f2,f3,*_,f5)=(1,2,3,4,5,6,7,8,9)
# *_ is a list we can create any name as same
print(f1)
print(_)

(d1,d2,*d3)=7,8,9,5,6,1,2,3
print(d1)
print(d3)
print(type(d3))

'''swaping two variables'''
a = 'mk'
b = 'Joker'
print(a)
print(b)
temp = a
print(temp)
a = b
print(a)
print(b)
print(temp)
b = temp
print(a,b,temp)
'''execute with temp variable'''
d1 = 'jk'
d2 = 'kk'
tempp = d1
d1 = d2
d2 = tempp
print(d1,d2)

'''in Python swaping can be done by tuple assignment'''
e1 = 'Fobbs'
f1 = 'hobbs'
print(e1,f1)
'''Magic Time'''
e1,f1 = f1,e1
print(e1,f1)


