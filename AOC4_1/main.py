import re

file = open('input.txt', 'r')
input = file.readlines()

line_no = 0;
total_sum = 0;

for card in input:
    winning_amount = 0
    card_input = card.split(":")[1]
    card_winningNumbers = card_input.split("|")[0]
    card_ourNumbers = card_input.split("|")[1]
    winning_numbers = re.findall("\d+",card_winningNumbers)
    our_numbers = re.findall("\d+",card_ourNumbers)

    for winner in winning_numbers:
        if winner in our_numbers:
            if winning_amount == 0:
                winning_amount = 1
            else:
                winning_amount *= 2

    total_sum += winning_amount

print(total_sum)