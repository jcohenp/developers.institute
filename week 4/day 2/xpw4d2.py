#1
fav_nums = {"9","10", "12"}
fav_nums.add("11")
fav_nums.remove("12")
print(fav_nums)
f_fav_nums = {"7","5"}
fav_nums.update(f_fav_nums)
print(fav_nums)

#2 - No. Tuples are immutible

#3 - Int take full numbers and float takes desimals.

list_float = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(list_float)

#4
for i in range(1,21):
    print(i)

#5
toppings = input("what topplings do you want? when u finish enter quit!\n")
while toppings != "quit":
    toppings = input("what topplings do you want? when u finish enter quit!\n")
print("order excepted")

#6
price = []
age = input('age or press quit to end \n')
while age != "quit":
    age = int(age)
    if age < 3:
        pass
    elif age > 2 or age < 13:
        kid = 10
        price.append(kid)
    elif age > 12:
        adult = 15
        price.append(adult)
    age = input('age or press quit to end \n')    
print(sum(price))

#7
users = ["Jasper","Horace","Maurice","Gloria"]
new_users = []
for i in users:
    age = input("How old are you?")
    if int(age) > 16:
         new_users.append(i)
   
print(new_users)

#8
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

#9 While doesn't make sense to use. Used for loop instead. 
mylist = [1,2,3,4,5,6,7,8]
for i in range (len(mylist),0,-1):
    print(i)
    
#10 While doesn't make sense to use. Used for loop instead.   
mylist = [1,2,3,4,5,6,7,8]
for i in mylist:
    if i % 2== 0:
        print(i)

#11
mult = []
i=0
for i in range(0,31,3):
    mult.append(i)
print(mult)

#12
for num in range (1500, 2700):
    if num % 7 == 0 and num % 5 == 0:
        print(num)
