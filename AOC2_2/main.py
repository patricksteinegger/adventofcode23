import re

sum_of_powers = 0;

file = open('input_2.txt', 'r')
input = file.readlines()

for line in input:

    max_red = 0;
    max_blue = 0;
    max_green = 0;

    split_line = line.split(":")

    #split line into components
    line_components = split_line[1].split(";")

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
                    max_blue = color_amount
            elif color.find("red") > -1:
                if color_amount > max_red:
                    max_red = color_amount
            elif color.find("green") > -1:
                if color_amount > max_green:
                    max_green = color_amount

        # if > max -> line_is_gud auf False setzen

    power = max_red*max_blue*max_green
    sum_of_powers += power


print(sum_of_powers)