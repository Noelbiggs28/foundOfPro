class LibraryItem:
    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"

    def get_location(self):
        return self._location
    

class Book:
    def __init__(self, LibraryItem, author):
        self._author = author

    def get_check_out_length(self):
        return "21 days"
    
    def get_author(self):
        return self._author


class Album:
    def __init__(self, LibraryItem, artist):
        self._artist = artist

    def get_check_out_length(self):
        return "14 days"
    
    def get_artist(self):
        return self._artist


class Movie:
    def __init__(self, LibraryItem, director):
        self._director = director

    def get_check_out_length(self):
        return "7 days"
    
    def get_director(self):
        return self._director
    

class Patron:
    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0
    
    def get_fine_amount(self):
        return self._fine_amount
    
    def add_library_item(self, item):
        self._checked_out_items.append(item)

    def remove_library_item(self, item):
        self._checked_out_items.remove(item)

    def amend_fine(self, amount):
        self._fine_amount += amount


class Library:
    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, item):
        self._holdings.append(item)

    def add_patron(self, patron):
        self._members.append(patron)

    def lookup_library_item_from_id(self, id):
        pass
    def lookup_patron_from_id(self, id):
        pass
    def check_out_library_item(self, patron_id, item_id):
        pass




b1 = Book("345", "Phantom Tollbooth", "Juster") 
a1 = Album("456", "...And His Orchestra", "The Fastbacks") 
m1 = Movie("567", "Laputa", "Miyazaki") 
print(b1.get_author()) 
print(a1.get_artist()) 
print(m1.get_director())

p1 = Patron("abc", "Felicity") 
p2 = Patron("bcd", "Waldo")

lib = Library() 
lib.add_library_item(b1) 
lib.add_library_item(a1) 
lib.add_patron(p1) 
lib.add_patron(p2)

lib.check_out_library_item("bcd", "456") 
for _ in range(7): lib.increment_current_date() # 7 days pass 
lib.check_out_library_item("abc", "567") 
loc = a1.get_location() 
lib.request_library_item("abc", "456") 
for _ in range(57): lib.increment_current_date() # 57 days pass 
p2_fine = p2.get_fine_amount() 
lib.pay_fine("bcd", p2_fine) 
lib.return_library_item("456")