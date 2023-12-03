import re
import numpy as np

file = open('input.txt', 'r')
input = file.readlines()

line_no = 0;
total_sum = 0;

# Build a matrix with the inputs because I don't know how to work them otherwise
matrix_width = len(input[0])-1 # -1 because of \n
matrix_height = len(input)
matr = [[input[y][x] for x in range(matrix_width)] for y in range(matrix_height)]

# pad matrix to ignore edge cases
# "Fuck Edge Cases. All my Homies hate Edge Cases."

pad_width = 1;
matr = np.pad(matr, pad_width, "empty");
matrix_height += 1
matrix_width += 1
print(np.matrix(matr))

def pleasehavealookifthereisasonderzeichen(number):

    is_next_to_sonderzeichen = False

    #prints all found numbers and their location in the original file
    print(str(line_no) + ": " + str(number.start()) + "-" + str(number.end()-1))

    #for every digit of the number, as well as the position to the direct left and direct right of it
    for x in range(number.start() - 1, number.end() + 1):

        # try to find a sonderzeichen in this position
        # +pad_width to offset for the padding we did
        if (len(re.findall("[^0-9.]", matr[line_no+pad_width][x+pad_width])) > 0):
            is_next_to_sonderzeichen = True;

        # or below it
        if (len(re.findall("[^0-9.]", matr[line_no - 1 +pad_width][x+pad_width])) > 0):
            is_next_to_sonderzeichen = True;

        # or above it
        if (len(re.findall("[^0-9.]", matr[line_no + 1 +pad_width][x+pad_width])) > 0):
            is_next_to_sonderzeichen = True;

    if (is_next_to_sonderzeichen):
        #return the value to add
        return int(number.group())


for line in input:

    numbers = re.finditer("\d+", line);
    for number in numbers:
        #for every found number -> run the function to check for nearby sonderzeichen
        valueofnumberifithasasonderzeichennearby = pleasehavealookifthereisasonderzeichen(number)
        if(valueofnumberifithasasonderzeichennearby):
            total_sum += valueofnumberifithasasonderzeichennearby

    line_no += 1

print(total_sum)