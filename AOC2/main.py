import re

sum_of_ids = 0;
max_red = 12;
max_green = 13;
max_blue = 14;

file = open('input_01.txt', 'r')
input = file.readlines()

for line in input:

    line_is_gud = True

    split_line = line.split(":")

    #find ID of current line ☑️
    line_id = "".join(re.findall("\d",split_line[0]))

    #split line into components
    line_components = split_line[1].split(";")
    amount_of_components = len(line_components)

    # iterate list of components for r/g/b
    for component in line_components:

        # split into color components
        color_components = component.split(",")

        for color in color_components:
            #find number
            color_amount = int("".join(re.findall("\d", color)))

            # check against max of r/g/b
            if color.find("blue") > -1:
                if color_amount > max_blue:
                    line_is_gud = False
            elif color.find("red") > -1:
                if color_amount > max_red:
                    line_is_gud = False
            elif color.find("green") > -1:
                if color_amount > max_green:
                    line_is_gud = False

        # if > max -> line_is_gud auf False setzen

    # if line_is_gud -> add id to sum_of_ids
    if line_is_gud:
        sum_of_ids += int(line_id)




print(sum_of_ids)




"""numbersbutactuallytext = ['zero','one','two','three','four','five','six','seven','eight','nine']

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

print (total)"""




