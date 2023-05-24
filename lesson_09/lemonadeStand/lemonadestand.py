class InvalidSalesItemError:
    def __init__(self, message):
        return None
class MenuItem:
    def __init__(self, item_name, item_wholesale_cost, item_selling_price):
        self._item_name = item_name
        self._item_wholesale_cost = item_wholesale_cost
        self._item_selling_price = item_selling_price

    def get_item_name(self):
        return self._item_name
    
    def get_item_wholesale_cost(self):
        return self._item_wholesale_cost
    
    def get_price(self):
        return self._item_selling_price
    
class SalesForDay:
    def __init__(self, days_stand_has_been_open, dictionary_of_items_sold):
        self._days_stand_has_been_open = days_stand_has_been_open
        self._dictionary_of_items_sold = dictionary_of_items_sold

    def get_day(self):
        return self._days_stand_has_been_open
    
    def get_sales_dict(self):
        return self._dictionary_of_items_sold

class LemonadeStand:
    def __init__(self, name):
        self._name = name
        self._current_day = 0
        self._menu_item_objects = {}
        self._sales_for_today = []

    def get_name(self):
        return self._name
    
    def add_menu_item(self, menu_item_object):
        name = menu_item_object.get_item_name()
        self._menu_item_objects[name] = menu_item_object

    def enter_sales_for_today(self, sales_for_day_dictionary):
        items_sold_today = list(sales_for_day_dictionary.keys())
        try:
            for item_name in items_sold_today:
                if item_name not in self._menu_items_objects:
                    raise Exception('the item you sold not on menu')
                sales_for_day_object = SalesForDay(self._current_day, sales_for_day_dictionary)
                self._sales_for_today.append(sales_for_day_object)
        except:
            print('item not on menu')
        
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, menu_item):
        
        for sales_object in self._sales_for_today:
            sales_object_day = sales_object.get_day()
            if sales_object_day == day:
                sales_object_dictionary = sales_object.get_sales_dict()
                sales_for_menu_item_on_this_day = sales_object_dictionary.get(menu_item, 0)
                return sales_for_menu_item_on_this_day
            return "No info found for item"
        # if menu_item in self._sales_for_today[day][0]:
        #     amount_sold_for_day = self._sales_for_today[day][0][menu_item]
        # else:
        #     return 'doesnt exist'
        # # returns number of item sold on day
        # # uses salesfordayobject
        # return amount_sold_for_day

    def total_sales_for_menu_item(self, name_of_menu_item):
        for item in self._sales_for_today:
            print (item)

    def total_profit_for_menu_item(self):
        pass

    def total_profit_for_stand(self):
        pass

hotdog = MenuItem('Hot Dog', 0.10, 1.00)
soda = MenuItem('Soda', .05, .50)
fries = MenuItem('Fries', 0.50, 1.00)
willies = LemonadeStand('Willies')
day_00 = {
    'Hot Dog': 5,
    'Soda':4}
willies.add_menu_item(hotdog)
willies.add_menu_item(soda)
willies.add_menu_item(fries)
willies.enter_sales_for_today(day_00)
print(willies.sales_of_menu_item_for_day(0,'Hot Dog'))