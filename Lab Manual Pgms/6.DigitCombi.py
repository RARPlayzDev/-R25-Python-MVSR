# Import the permutations function from the itertools library.
# This function is used to generate all possible orderings of a sequence.
from itertools import permutations

def get_digit_combinations():
  """
  This program takes a three-digit number from the user
  and prints all possible combinations of those digits.
  """

  # Print a title for the program.
  print("===  Digit Combinations ===")

  # Get input from the user.
  digits_input = input("Enter digits: ")

  # Generate all permutations of the input digits.
  # The `permutations` function returns a list of tuples.
  # For example, if the input is '123', permutations('123') will produce:
  # ('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'),
  # ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')
  digit_permutations = permutations(digits_input)

  # Create an empty list to store the combinations as strings.
  combinations_list = []

  # Loop through each permutation tuple.
  for p in digit_permutations:
    # Join the digits in the tuple to form a string.
    # For example, ('1', '2', '3') becomes '123'.
    combinations_list.append("".join(p))

  # Print all the generated combinations.
  print(f"All combinations: {combinations_list}")

  # Print a blank line for better readability.
  print()

# Call the function to run the program.
get_digit_combinations()
