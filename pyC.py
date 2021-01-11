def cube(n):
    return n**3

lam1 = lambda n1:n1**3

print(cube(3))
print(lam1(3))
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
  
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list) 
ages = [13, 90, 17, 59, 21, 60, 5] 
  
adults = list(filter(lambda age: age>18, ages))
print(adults)

final_list1 = list(map(lambda x: x**2 , li))
print(final_list1)

animals = ['dog', 'cat', 'parrot', 'rabbit'] 
  
# here we intend to change all animal names 
# to upper case and return the same 
uppered_animals = list(map(lambda animal: str.upper(animal), animals)) 
print(uppered_animals)
from functools import reduce

reduced = reduce((lambda x,y: x+y),li)
print(reduced)

print("List is ",li)
print ("The maximum element of the list is : ",end="")  
print (reduce(lambda a,b : a if a > b else b,li))  

if __name__ == "__main__":
    pass