fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
   
print("printing from 0 to 4") 
count = 0
while count < 5:
    print(count)
    count += 1
print("printing the list and when reaches to 3 loop will be stoped so it will print 1, 2 : ")
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)

print("It will skip when reaches to 3")
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)



log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
    if "ERROR" in line:
        print(line)