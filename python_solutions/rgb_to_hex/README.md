# RGB to Hex Converter

This function converts a set of rgb values to a hexadecimal string

## Problem Description

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):

255, 255, 255 --> "FFFFFF"

255, 255, 300 --> "FFFFFF"

0, 0, 0 --> "000000"

148, 0, 211 --> "9400D3"

## Solution

First the function declares a dictionary to map integers between 0 and 15 to their corresponding Hex values:

    hex_values  = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

Next, the function creates an empty string called "hex". Hex values for each rgb value will be stored here and returned at the end of the function.

    hex = ""

The function then takes the input (r, g, b) and stores these values in a list:

 `values = [r, g, b]`
 
 The function then begins a for loop, iterating over each value in values:

    for value in values:

It then goes through a series of if/elif/else statements to determine how it responds to the value. First it checks if the value is less than or equal to 0, then adds "00" to "hex" if necessary:

    if  value  <=  0:
	    hex  +=  "00"

Then it checks if the value is greater than or equal to 255 and if so adds "FF" to "hex":

    elif  value  >=  255:
	    hex  +=  "FF"

If neither of these conditions are met, the following statement is triggered:

    else:
	    hex  +=  hex_values[int(value  /  16)] +  hex_values[value  %  16]
 
 The first part of the right-hand side of this operation finds the highest whole number that the value is divisible by, and returns the corresponding hex value. The second part returns the hex value of the remainder of the value divided by 16. These values are then added to "hex". Once the loop has been completed for each value in the input, "hex" is returned.