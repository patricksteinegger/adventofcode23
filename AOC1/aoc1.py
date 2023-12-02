import regex as re

total = 0;

file1 = open('in.txt', 'r')
input = file1.readlines()

numbersbutactuallytext = ['zero','one','two','three','four','five','six','seven','eight','nine']

for i in input:
    match = re.findall("\d|one|two|three|four|five|six|seven|eight|nine", i, overlapped=True)
    first = match[0]
    last = match[len(match)-1]

    if not first.isnumeric():
        first = numbersbutactuallytext.index(first)

    if not last.isnumeric():
        last = numbersbutactuallytext.index(last)

    result = int(first) * 10 + int(last)
    total += result

print (total)




