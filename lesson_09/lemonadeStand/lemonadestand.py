class InvalidSalesItemError(Exception):
    pass
    
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
                if item_name not in self._menu_item_objects:
                    raise Exception('the item you sold not on menu')
                sales_for_day_object = SalesForDay(self._current_day, sales_for_day_dictionary)
            self._sales_for_today.append(sales_for_day_object)
        except:
            raise InvalidSalesItemError('the item isnt on the menu')
        
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, menu_item):
        
        for sales_object in self._sales_for_today:
            sales_object_day = sales_object.get_day()
            if sales_object_day == day:
                sales_object_dictionary = sales_object.get_sales_dict()
                sales_for_menu_item_on_this_day = sales_object_dictionary.get(menu_item, 0)
                return sales_for_menu_item_on_this_day
        return "No information found for that day"

    def total_sales_for_menu_item(self, menu_item):
        total = 0
        day = 0
        while day < self._current_day:
            total += self.sales_of_menu_item_for_day(day, menu_item)
            day +=1
        return total


    def total_profit_for_menu_item(self, menu_item):
        amount_sold = self.total_sales_for_menu_item(menu_item)
        cost = self._menu_item_objects[menu_item].get_item_wholesale_cost()
        price = self._menu_item_objects[menu_item].get_price()
        return (price - cost) * amount_sold

    def total_profit_for_stand(self):
        total = 0
        for item in self._menu_item_objects:
            total += self.total_profit_for_menu_item(item)
        return total

def main():
    
    stand = LemonadeStand('Lemons R Us')
    item1 = MenuItem('lemonade', 0.5, 1.5)
    stand.add_menu_item(item1)
    item2 = MenuItem('nori', 0.6, 0.8)
    stand.add_menu_item(item2)
    item3 = MenuItem('cookie', 0.2, 1) 
    stand.add_menu_item(item3)
    day_0_sales = {
        'lemonade' : 5,
        'cookie'   : 2
    }
    stand.enter_sales_for_today(day_0_sales)
    print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")
    print(stand.total_profit_for_stand())

if __name__ == '__main__':
    main()