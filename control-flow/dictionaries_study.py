
# dictionaries
from pprint import pprint
print({})
print(type({}))
d = dict()

person = {
    'first_name': 'nmaju',
    'last_name': 'terence',
    'is_married': True,
    'address': {
        'street_name': 'antenne orange logbessou',
        'zipcode': '00237',
        'city': 'douala',
        'country': 'cameroon',
        },
    'education': 'alx africa',
    'child': 'kiara',
    'company': 'bigtee llc',
    'website': 'www.bigtee.io',
    'profession': 'web developer and seo expert',
    'age': 32,
    'skills': ['python', 'html5', 'css3', 'javascript', 'wordpress', 'seo'],
    }
pprint(person)
print(person['education'])
person['hobbies'] = ['video gamming', 'reading', 'running']

# add an item to a dictionary
person['hobbies'].append('clubbing')

# get() method
print(person.get('education'))

# using conditions to display value of a key in a dictionary
if 'hobbies'in person:
    print(person['hobbies'])

# len() method
print(len(person))

print(person.keys())
print(person.values())
print(person.items())

for item in person.items():
    print(item, item[0], item[1])

# extract and display the key and value of dictionaries
for item in person:
    print(item, person[item])

# checking if a key is in a dictionary
print('child' in person)

# removing key and value pairs from a dictionary pop(key), popitem(), del:

person.pop('child')
pprint(person)

person.popitem()
pprint(person)