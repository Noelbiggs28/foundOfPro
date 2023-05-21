class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

def std_dev(person_list):
    # list_of_ages = [person.get_age() for person in person_list]
    list_of_ages = []
    for person in person_list:
        list_of_ages.append(person.get_age())
    
    mean1 = sum(list_of_ages) / len(list_of_ages) 
    
    # small_list = [(num-mean1) ** 2 for num in list_of_ages]
    small_list = []
    for num in list_of_ages:
        small_list.append((num-mean1) ** 2 )
    
    mean3 = sum(small_list) / len(small_list)
    answer = mean3 ** 0.5
    
    return answer

mike = Person('Mike', 73)
sarah = Person('Sarah', 24)
steve = Person('Steve', 48)
list_of_peeps = [mike, sarah, steve]

print(std_dev(list_of_peeps))
