from project.bakery import Bakery

bakery = Bakery('Random Name')
print(bakery.add_drink('Water', 'Mineral', 500, 'Bankya'))
print(bakery.add_drink('Tea', 'Ice', 500, 'Nestle'))
print(bakery.add_table('OutsideTable', 55, 15))
print(bakery.reserve_table(10))
print(bakery.order_drink(55, 'Spring', 'Mineral', 'Ice', 'Coke', 'Fanta'))
print(bakery.leave_table(55))

print('---')

print(bakery.get_total_income())