import re

file = open('input.txt', 'r')
input = file.readlines()

total_sum = 0;

#new list LINE_NO | WINS | COUNT_X_TIMES
magic_list = []

#build list
for card in input:
    winning_amount = 0
    card_lineNumber = int(re.findall("\d+", card.split(":")[0])[0])
    card_input = card.split(":")[1]
    card_winningNumbers = card_input.split("|")[0]
    card_ourNumbers = card_input.split("|")[1]
    winning_numbers = re.findall("\d+",card_winningNumbers)
    our_numbers = re.findall("\d+",card_ourNumbers)

    for winner in winning_numbers:
        if winner in our_numbers:
            winning_amount += 1

    magic_list_item = {
        "line_number": card_lineNumber,
        "winning_amount": winning_amount,
        "count": 1
    }
    magic_list.append(magic_list_item)

#count scratchcards
for card in magic_list:

    for l in range(card["count"]):
        for i in range(card["winning_amount"]):
            magic_list[card["line_number"] + i]["count"] += 1

    total_sum += card["count"]

print(total_sum)