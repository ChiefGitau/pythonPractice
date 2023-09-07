coffee_menu = { "espresso": {
    "ingredients" : {
        'water' : 100,
        'milk' : 50,
        'coffee': 1.8
    },
    'price': 10},
"latte": {
    "ingredients" : {
        'water' : 200,
        'milk' : 150,
        'coffee' : 24
    },
    'price': 2.5},
"cappuccino": {
    "ingredients" : {
        'water' : 250,
        'milk' : 100,
        'coffee' : 24
    },
    'price': 2.6
}}
resource = {
    'water':1000,
    'coffee':1000,
    'milk':500,
    'money':10.00
}
def apology(lack):
    print('Sorry there is not enough ' + lack)
def resource_check(choice):
    element= coffee_menu[choice]

    if element['ingredients']['water'] > resource['water']:
        apology('water')

    elif element['ingredients']['coffee'] > resource['coffee']:
        apology('coffee')

    elif element['ingredients']['milk'] > resource['milk']:
        apology('milk')
def coffe_option(choice):

    resource_check(choice)
    euro_coin2 = input('Please insert the 2 euro coins')
    euro_coin1 = input('Please insert the 1 euro coins')
    euro_coin050 = input('Please insert the 50 cent coins')
    euro_coin020 = input('Please insert the 20 cent coins')
    euro_coin010 = input('Please insert the 10 cent coins')
    euro_coin005 = input('Please insert the  5 cent coins')

    total  = (float(euro_coin2) * 2 + float(euro_coin1) + float(euro_coin050) * 0.50 +
              float(euro_coin020) * 0.20 + float(euro_coin010) *0.10 +
              float(euro_coin005) * 0.05)
    if total < coffee_menu[choice]['price']:
        print('Sorry thats not enough money. Money refunded.')
        return

    else:
        resource['money'] = resource['money'] + total
        resource['water'] = resource['water']  - coffee_menu[choice]['ingredients']['water']
        resource['milk'] = resource['milk'] - coffee_menu[choice]['ingredients']['milk']
        resource['coffee'] = resource['coffee'] - coffee_menu[choice]['ingredients']['coffee']

        print('Here is your' + choice + '. Enjoy!')

power = True

while power:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'off':
        power = False

    elif choice == 'report':
        print(resource)

    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        coffe_option(choice)



