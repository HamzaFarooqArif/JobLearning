person = {'name': 'Hamza', 'age': 23}

sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)

sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
print(sentence)

sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(name=person['name'], age=person['age'])
print(sentence)

personB = ['Hamza', 23]
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(personB)
print(sentence)