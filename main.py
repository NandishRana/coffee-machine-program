from data import MENU, resources


def coffee_maker():
    for item in recipe:
        resources.update(
            {item: resources[item] - MENU[cmd_line]['ingredients'][item]})

    resources['money'] += MENU[cmd_line]['cost']
    return user_money - MENU[cmd_line]['cost']


def gen_report():
    for key, value in resources.items():
        unit = "ml" if key != "money" else ""
        print(f"{key}: {value}{unit}")


def resource_availability(item, thingy):
    if resources[item] >= thingy:
        return "OK"
    else:
        return f"Sorry there is not enough {item}."


def coin_processor():
    da_money = 0
    for users_coins in coinpurse:
        da_money += coinpurse[users_coins] * coins[users_coins]

    return da_money


def ingredients():
    if cmd_line == "espresso":
        return ['water', 'coffee']
    elif cmd_line == "latte" or cmd_line == "cappuccino":
        return ['water', 'milk', 'coffee']


machine_status = "on"
resources.update({'money': 0})
coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
coinpurse = {}
resources_status = "OK"

while machine_status == "on":

    cmd_line = input("What would you like? (espresso/latte/cappuccino): ")

    if cmd_line == "report":
        gen_report()
    elif cmd_line == "off":
        break
    elif cmd_line == "espresso" or cmd_line == "latte" or cmd_line == "cappuccino":

        recipe = ingredients()

        for item in recipe:
            if resources_status == "OK":
                resources_status = resource_availability(item, MENU[cmd_line]['ingredients'][item])

        if resources_status == "OK":
            print("Please insert coins.")

            for coin in coins:
                coinpurse.update({coin: int(input(f"How many {coin}?: "))})
            user_money = coin_processor()

            if user_money >= MENU[cmd_line]['cost']:
                change = coffee_maker()
                print(
                    f"Here is ${round(change, 2)} in change.\nHere is your {cmd_line}, Enjoy!.")

            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print(resources_status)
            resources_status = "OK"
    else:
        print("Did u spell it correct?")
