menu = {'espresso': {'ingredients': {'coffee': 19, 'water': 35, }, 'price': 1.99, },
        'latte': {'ingredients': {'coffee': 24, 'water': 50, 'milk': 150, }, 'price': 2.39, },
        'flat white': {'ingredients': {'coffee': 24, 'water': 60, 'milk': 50, }, 'price': 3.19}}
inventory = {'coffee': 100, 'water': 300, 'milk': 300, 'money': 0}
coins = {'dollar': 1.00, 'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}


def check_resources(user_choice):
    print(menu['user_choice'])
    for k, v in inventory:
        print(k)
        # ingmenu = menu['menu'][k]
        # print(ingmenu)

        # if k in menu['ingredients'][k] and menu['ingredients'][k] <= v:
        #     print(f'this {k} and ')
        #

    return


def make_coffee(user_choice):
    check_resources(user_choice)

    return


def process_coins(price):
    user_coin = ''
    user_change = 0.00
    need_to_pay = price
    while need_to_pay > 0:
        print(f'You need to pay: {need_to_pay}')
        user_coin = input('your coin: (dollar/quarters/dimes/nickles/pennies)') or 'dollar'
        if user_coin in coins:
            if user_coin == 'dollar':
                need_to_pay -= coins['dollar']
            if user_coin == 'quarters':
                need_to_pay -= coins['quarters']
            if user_coin == 'dimes':
                need_to_pay -= coins['dimes']
            if user_coin == 'nickles':
                need_to_pay -= coins['nickles']
            if user_coin == 'pennies':
                need_to_pay -= coins['pennies']
        else:
            print('invalid input')
        need_to_pay = round(need_to_pay, 2)

    if need_to_pay <= 0:
        user_change = abs(need_to_pay)
        print('Your return is: ', user_change)

    return True


def print_report():
    return


cmd = ''
while cmd != 'off':

    user_choice = input('What would you like? (espresso/latte/cappuccino): ') or 'latte'
    if user_choice in menu:
        print('you need to pay: ', menu[user_choice]['price'])
        paid = process_coins(menu[user_choice]['price'])
        canmakeorder = make_coffee(menu[user_choice])
        if paid:
            make_coffee(user_choice)

    else:
        print('invalid input')
