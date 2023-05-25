import json
with open('mary.txt', 'w') as mary:
    mary.write('Mary had a little lamb \nlittle lamb \nlittle lamb \nMary had a little lamb whos fleece was white as snow')

with open('mary.txt', 'r') as mary:
    for line in mary:
        print(line.strip())

names = {
    '1':'William',
    '2':'Patrick',
    '3':'Jon',
    '4':'Tom',
    '5':'Peter',
    '6':'Colin',
    '7':'Sylvester',
    '8':'Paul',
    '9':'Chris',
    '10':'David',
    '11':'Matt',
    '12':'Peter',
    '13':'Jodie'
}

with open('names.txt', 'w') as name:
    json.dump(names, name)

with open('names.txt', 'r') as name:
    restored_names = json.load(name)
    print(restored_names)