numeral_input = input("Enter the roman numerals you want to convert: ")

def roman_to_int(numeral):
    final_answer = 0

    # Handle special cases where subtraction is used
    if "CM" in numeral:  # 900
        final_answer += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:  # 400
        final_answer += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:  # 90
        final_answer += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:  # 40
        final_answer += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:  # 9
        final_answer += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:  # 4
        final_answer += 4
        numeral = numeral.replace("IV", "")

    # Process remaining characters
    for i in numeral:
        if i == "M":
            final_answer += 1000
        elif i == "D":
            final_answer += 500
        elif i == "C":
            final_answer += 100
        elif i == "L":
            final_answer += 50
        elif i == "X":
            final_answer += 10
        elif i == "V":
            final_answer += 5
        elif i == "I":
            final_answer += 1

    print("The roman numerals you entered translate to: " + str(final_answer) + "!")

# Call the function
roman_to_int(numeral_input)