# Naughty or nice - Christmas coding challenge

Given a set of conditions and a list of names, write a python programme which will tell you who is on Santa's naughty list and who is on his nice list.

## Getting started

1. Clone the repository
2. Create a python virtual environment `python3 -m venv env`
3. Activate the virtual environment `source env/bin/activate`
4. Install required packages `pip install -r requirements.txt`

## List of names

```
[
    'Ashley Carrabine',
    'Shirley Hunter',
    'Vanessa Mcintosh',
    'Adrienne Wilson',
    'Roger Varney',
    'Beverly Hudson',
    'Brett Jacks',
    'Kevin Avery',
    'Miranda Grant',
    'Linda Askew',
    'Sonya Brown'
]
```

## Conditions
Things that make a name naughty:
- A letter appears more than once in the first name
- Surname is longer than 5 letters

## Generate new names
Use the `names` library to generate random names. E.g:

```
import names

list_of_names = [names.get_full_name() for i in range(10)]
```