# EX 1
def manage_students():
    students = ['Aljawhra', 'sara', 'saud','Abdulaziz' ]
    fist_student = students [1]
    last_student = students [-1]
    return fist_student, last_student

print('Exercise 1:', manage_students()) 

# EX 2
def combine_foods():
    foods = ['pizza', 'burger', 'shawarma']
    meal = ''
    for food in foods:
        meal += food + ' '
        return meal.strip()
       
print('Exercise 2:', combine_foods())

# EX 3
def slice_foods():
  foods = ['pizza', 'burger', 'shawarma']
  last_two_foods = foods[-2:]
  return last_two_foods

print('Exercise 3:', slice_foods())

# EX 4
def hometown_info():
    home_town = {
        'city': 'Alain',
        'country': 'United Arab Emirates',
        'population': 7000000
    }
    home_town_message = (f"I was born in {home_town['city']},{home_town['country']} - "
        f"population of {home_town['population']}")
    return home_town_message

print('Exercise 4:', hometown_info())

# EX 5
def list_home_town_items():
    home_town = {
        'city': 'Alain',
        'country': 'United Arab Emirates',
        'population': 7000000
    }
    home_town_items = []
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    return home_town_items

print('Exercise 5:', list_home_town_items())