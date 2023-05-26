import json

class NobelData:
    def __init__(self, name_of_file):
        self._name_of_file = name_of_file
        self._noble_json_data = ''
        
        with open(name_of_file, 'r') as infile:
            self._noble_json_data = json.load(infile)

    def search_nobel(self, winning_year, catagory):
        winners = []
        for prize in self._noble_json_data['prizes']:
            if winning_year in prize.values() and catagory in prize.values():
                for winner in prize['laureates']:
                    winners.append(winner['surname'])
        winners.append('Biggs')
        print(sorted(winners))

nobel_json_data = NobelData('nobels.json')
nobel_json_data.search_nobel('2001','economics')
nobel_json_data.search_nobel('1911',"chemistry")