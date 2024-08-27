
def printingDict(my_dist):
    for key in my_dist:
        print(key , my_dist[key])
        
        
my_dist = {"name":"John","age":25,"city":"newYork"}

printingDict(my_dist)
print(my_dist["name"])  #accessing value


#modifying value
my_dist['age']=26
my_dist['occupation']="Engineer"
print("printingn dictionary after modifying")
printingDict(my_dist)

del my_dist['city']

print("Deleted city")
printingDict(my_dist)

if 'age' in my_dist:
    print("Age is present in the dictionary")


    
print(my_dist.items())  #return list of tuple [(key, value), (key,value),...]

