menu = {'espresso': {'ingredients': {'coffee': 19, 'water': 35, }, 'price': 1.99, },
        'latte': {'ingredients': {'coffee': 24, 'water': 50, 'milk': 150, }, 'price': 2.39, },
        'flat white': {'ingredients': {'coffee': 24, 'water': 60, 'milk': 50, }, 'price': 3.19}}
inventory = {'coffee': 100, 'water': 100, 'milk': 300, 'money': 0}
coins = {'dollar': 1.00, 'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}


def check_resources(user_choice):  # latte
    user_choice = menu[user_choice]['ingredients']
    count = 0
    for key in user_choice:
        if inventory[key] and user_choice[key]:
            if inventory[key] >= user_choice[key]:
                count += 1
                # inventory[key] -= user_choice[key]
        else:
            print(f'Sorry there is not enough {key} ')
            # return False
    # return True
    if count < len(user_choice):
        return False
    else:
        return True


def make_coffee(user_choice):
    dict_user_choice = menu[user_choice]['ingredients']
    for key in inventory:
        if inventory[key] and dict_user_choice[key]:
            if key == 'money':
                print(inventory['money'])
                print(menu[user_choice]['price'])
                inventory[key] += menu[user_choice]['price']
            else:
                inventory[key] -= dict_user_choice[key]


    # inventory['money'] += menu[user_choice]['price']
    print(f'Here is your {user_choice}. Enjoy')
    return


def process_coins(price):
    user_coin = ''
    user_change = 0.00
    need_to_pay = price
    while need_to_pay > 0:
        print(f'You need to pay: {need_to_pay}')
        user_coin = input('your coin: (dollar/quarters/dimes/nickles/pennies)') or 'dollar'
        print(f'you paid {user_coin}')
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
    for k, v in inventory.items():
        print(f'{k}: {v}')


def take_order():
    user_choice = input('May I take your order, please? (espresso/latte/cappuccino): ') or 'latte'
    return user_choice


cmd = ''
while cmd != 'off':
    user_choice = take_order()
    # user_choice = input('May I take your order, please? (espresso/latte/cappuccino): ') or 'latte'
    print(f'Yes. Could I have {user_choice}, please?')
    if user_choice in menu:
        print('wait a moment please..')
        avalible = check_resources(user_choice)
        if not avalible:
            order = input(f'we run out of ingredients for {user_choice}, would you like to order something else? Y/N ')
            if order == 'Y':
                user_choice = take_order()
                avalible = check_resources(user_choice)
            else:
                print('Bye!')

        else:
            print(f"That'll be: {menu[user_choice]['price']}, please.")
            paid = process_coins(menu[user_choice]['price'])

            if paid and avalible:
                make_coffee(user_choice)
                print_report()

    elif user_choice == 'report':
        print_report()

    elif user_choice == 'off':
        cmd = 'off'
        print('Machine is shutting down, BYE!')
        break
    else:
        print('invalid input')
