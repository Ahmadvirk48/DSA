spicy_foods = [
 {
 "name": "Green Curry",
 "cuisine": "Thai",
 "heat_level": 9,
 },
 {
 "name": "Buffalo Wings",
 "cuisine": "American",
 "heat_level": 3,
 },
 {
 "name": "Mapo Tofu",
 "cuisine": "Sichuan",
 "heat_level": 6,
 },
]

#1.
my_list=[]
def get_names(spicy_foods):
    for i in spicy_foods:
        my_list.append((i["name"]))
            
get_names(spicy_foods)
print(my_list)

#2.
my_list1=[]
def get_spiciest_foods(spicy_foods):
    for i in spicy_foods:
        if i["heat_level"] > 5:
            my_list1.append(i)
#3.            
get_spiciest_foods(spicy_foods)
print(my_list1)

#4.
def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        print(i["name"],"(",i["cuisine"],")","| Heat Level:",i["heat_level"]* "🌶")
    
#5.
print_spicy_foods(spicy_foods)


#6. hello world



    
    
    

