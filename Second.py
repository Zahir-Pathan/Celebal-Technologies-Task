
var="Zahir"
print(hex(id(var)))
x="Pathan"
print(hex(id(x)))
var=var + x
print(hex(id(var)))
print(var)
print(var.upper())
print(var.title())

############################


var_list = ['Zahir',30,2j]
print(dir(var_list)) #to check methods 
# print(var_list[0])
# print(var_list.pop())#will remove the last element
# print(var_list.remove(0))
print(var_list.remove(30))#only removes the first occurance of value mentioned 
print(var_list)