import re

file = open('input.txt', 'r')
input = file.readlines()

line_no = 0;
gear_line_no = 0;
total_sum = 0;
list_of_number_tuples = []

def row_is_nearby(tuple):
    if tuple[0] >= gear_line_no-1 and tuple[0] <= gear_line_no+1:
        return True
    return False

#numbers
for line in input:
    #find all numbers
    numbers = re.finditer("\d+", line);

    for number in numbers:
        # create a tuple of each number: LINE | START | END | NUMBER
        number_tuple = (line_no,number.start(),number.end(), number.group())
        # add that to a list
        list_of_number_tuples.append(number_tuple)
    line_no += 1

#gears
for line in input:
    #find gears
    gears = re.finditer("\*", line);
    for gear in gears:

        print("Gear at line " + str(gear_line_no) + " at position " + str(gear.start()))
        list_of_nearby_numbers = []

        for number_tuple in filter(row_is_nearby, list_of_number_tuples):
            #check if beginning or end of number is within 1 position of gear, then append to list of nearby numbers
            if ( (number_tuple[2]-1 >= gear.start()-1 and number_tuple[2]-1 <= gear.start()+1) or (number_tuple[1] >= gear.start()-1 and number_tuple[1] <= gear.start()+1)):
                list_of_nearby_numbers.append(number_tuple)

        #check if exactly 2 numbers nearby
        if(len(list_of_nearby_numbers) == 2):
            print("exactly 2 numbers nearby")
            total_sum += int(list_of_nearby_numbers[0][3]) * int(list_of_nearby_numbers[1][3])

    gear_line_no += 1

print(total_sum)
