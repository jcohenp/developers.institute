#1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

zip_items = zip(keys, values)

new_dict = dict(zip_items)

print(new_dict)

#2

store = {"name": "Zara",
         "creation_date": "1975", 
         "creator_name": "Amancio Ortega Gaona", 
         "type_of_clothes": ["men", "women", "children", "home"], 
         "international_competitors": ["Gap", "H&M", "Benetton"], 
         "number_stores": "7000", 
         "major_color": {"France":"blue",
                        "Spain":"red",
                        "US": ["pink", "green"]} 
    }
store["number_stores"] = 0
print(store["number_stores"])

store.update({"Origin":"Spain"})
print(store)

if "international_competitors" in store:
    key = "international_competitors"
    store[key].append("Desigual")
print(store)

del store["creation_date"]
print(store)
print(store["international_competitors"][3])

fav1 = str(store["major_color"]["US"][0])
fav2 = str(store["major_color"]["US"][1])
print("favourite colours in the us are " + fav1 + " and " + fav2)

print(len(store))

print(store.keys())

more_on_zara = {
    "creation_date": "1975", 
    "number_stores": "10 000" 
    }
store["more_on_zara"] = more_on_zara
print(store)

print(store["number_stores"]) #became 0, didn't save moreonzara info;



#3

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

dict_disn = {users[i]: i for i in range(len(users))}

print(dict_disn)

dict_disney = {i : users[i] for i in range(0, len(users))}
               
print(dict_disney)

users.sort()

dict_sort = {i : users[i] for i in range(0, len(users))}

print(dict_sort)

i_only = []

for i in users:
    name = list(i)
    for j in name:
        if j == "i" and i not in i_only:
           i_only.append(i)
        else:
            pass
print(i_only)


start_pm = []

for j in users:
    name = list(j)
    if name[0] == "P" or name[0] == "M": 
        start_pm.append(j)
print(start_pm)







