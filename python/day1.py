# Calculate fuel required for module based off mass
def calculate_fuel_required(mass: int) -> int:
    return (mass // 3) - 2


# Calculate fuel required for module taking into account fuel needed for fuel
def calculate_total_fuel(o_mass: int) -> int:
    total = 0
    # Get fuel required for the module itself
    temp_fuel = calculate_fuel_required(o_mass)
    while temp_fuel > 0:
        # Added the fuel needed for the fuel to the total
        total += temp_fuel
        # Calulate the fuel needed for this fuel
        temp_fuel = calculate_fuel_required(temp_fuel)

    return total


def main():
    # Open input file
    with open("inputs/puzzle1.txt", "r") as f:
        total_fuel_p1 = 0
        total_fuel_p2 = 0
        # Iterate through each line of the input file
        # and calculate fuel used for each module
        for line in f:
            mass = int(line)
            total_fuel_p1 += calculate_fuel_required(mass)
            total_fuel_p2 += calculate_total_fuel(mass)
        # Output results to terminal
        print(f"Puzzle1: {total_fuel_p1}")
        print(f"Puzzle2: {total_fuel_p2}")


if __name__ == "__main__":
    main()
