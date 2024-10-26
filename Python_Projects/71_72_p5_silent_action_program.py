import os
print("****** Welcome to the Silent Action Program ******")

def find_max_bitter(bitters_data):
    max_price = 0
    winner_name = ""
    for bitter in bitters_data:
        bitter_price = bitters_data[bitter]
        bitter_name = bitter
        if bitter_price > max_price:
            max_price = bitter_price
            winner_name = bitter_name
    print(bitters_data)
    print(f"The Winner is {winner_name} with the bid of Rs.{max_price}")


other_bitters = True
bitters = {}
while other_bitters:
    name = input("What is your name: ")
    price = int(input("What is your bit price(Rs.): "))
    bitters[name] = price
    input_bitter = input("Are there any bitters? Type 'yes' or 'no': ")
    if input_bitter == 'no':
        find_max_bitter(bitters)
        other_bitters = False
    else:
        other_bitters = True
        os.system('cls')


