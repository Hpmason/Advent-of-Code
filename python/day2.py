'''
opcodes are 1, 2, 99
1 - add(+) values in position(index) of next two numbers
        and set the value of the position of the third number
2 - multiply(*) values in position(index) of next two numbers
        and set the value of the position of the third number
99 - exit intcode program

Blocks of int code:
(0,1,2,3)
(opcode, input index, input index, output index)
'''


def run_intcode(intcode: list, noun: int, verb: int) -> int:
    '''
    Process intcode program and return value of intcode at position 0
        intcode_cp: list intcode program
        noun: int value to set position 1 to
        verb: int value to set position 2 to
    Returns:
        int: intcode at position 0 after the intcode program has exited
    '''
    intcode_cp = intcode[:]
    # Set values for the noun and verb values
    intcode_cp[1] = noun
    intcode_cp[2] = verb
    # Start the indicator at the beginning of the int code
    indicator = 0
    # Loop until we get the opcode to exit the program (99)
    while intcode_cp[indicator] != 99:
        # Just a few variable references for neater code
        in_ind1 = intcode_cp[indicator + 1]
        in_ind2 = intcode_cp[indicator + 2]
        out_ind = intcode_cp[indicator + 3]
        # If opcode is value 1 add
        if intcode_cp[indicator] == 1:
            intcode_cp[out_ind] = intcode_cp[in_ind1] + intcode_cp[in_ind2]
        # If opcode is value 2 multiply
        elif intcode_cp[indicator] == 2:
            intcode_cp[out_ind] = intcode_cp[in_ind1] * intcode_cp[in_ind2]
        # If opcode is anything other than 1, 2, or 99, print error
        else:
            print(f"Unexpected opcode. \
                intcode_cp pos:{indicator}, value:{intcode_cp[indicator]}")
        # Move indicator 4 positions to next set of instructions
        indicator += 4
    # Return value of intcode at position 0
    return intcode_cp[0]


def find_result(intcode: list, desired_output: int) -> tuple:
    '''
    Return the noun and verb that corresponds with the desired output
        intcode: list of intcodes
        desired_output: int of desired final value in position one of intcode
    Returns:
        tuple: (noun, verb)
        If not found, will return (-1, -1)
    '''
    # Iterate over all combinations of noun and verb from 0-99
    for noun in range(0, 99):
        for verb in range(0, 99):
            # Run intcode program with noun and ver values
            result = run_intcode(intcode[:], noun, verb)
            # If the result is the desired output, 
            # return function with noun and verb values
            if result == desired_output:
                return noun, verb
    # If the desired output is not found, return the tuple (-1,-1)
    return -1, -1


def main():
    # Open input file
    with open("inputs/day2.txt", "r") as f:
        # Split comma seperated values into a list of ints
        intcode = [int(num) for num in f.read().split(",")]
        # Puzzle 1 requires running provided intcode with
        # positions 1 and 2 are replaced by 12 and 2 respectively
        puzzle1_result = run_intcode(intcode[:], 12, 2)
        # Result of the intcode at position one is the answer to puzzle 1
        print(f"Puzzle 1 Result: {puzzle1_result}")

        # Find the noun and verb that result in the value 19690720
        noun, verb = find_result(intcode, 19690720)
        # Answer = 100 * noun + verb
        print(f"Puzzle 2 Result: {100 * noun + verb}")


if __name__ == "__main__":
    main()
