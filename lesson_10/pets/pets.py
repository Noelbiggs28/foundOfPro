import json

class DuplicateNameError(Exception):
    pass

class NeighborhoodPets:
    def __init__(self):
        self._pets = {}
        self._pets_json_file = None

    def add_pet(self, pet_name, pet_species, pet_owner_name):
        if pet_name in self._pets:
            raise DuplicateNameError('A neighborhood pet already has that name') 
        else:
            self._pets[pet_name] = {'species': pet_species, 'owner': pet_owner_name}

    def delete_pet(self, pet_name):
        del self._pets[pet_name]

    def get_owner(self, pet_name):
        return self._pets[pet_name]['owner']

    def save_as_json(self, name_of_file):
        with open(name_of_file,'w') as outfile:
            outfile.write(str(self._pets))
    
    def read_json(self, name_of_file):
        with open(name_of_file, 'r') as infile:
            self._pets = json.load(infile)

    def get_all_species(self):
        species_set = set()
        for pet in self._pets:
            species_set.add(self._pets[pet]['species'])
            # print(pet)
        return species_set

np = NeighborhoodPets()
try:
    np.add_pet("Fluffy", "gila monster", "Oksana")
    np.add_pet("Tiny", "stegasaurus", "Rachel")
    np.add_pet("Spot", "zebra", "Farrokh")
except DuplicateNameError:
    print('You tried to enter a pet with the same name as another pet.')
np.save_as_json("pets.json")
np.delete_pet("Tiny")
spot_owner = np.get_owner("Spot")
np.read_json("other_pets.json")  # where other_pets.json is a file it saved in some previous session
species_set = np.get_all_species()
