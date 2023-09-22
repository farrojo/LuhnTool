import tkinter as tk
import random
import pyperclip

def make_random_number(number_of_element):
    random_numbers = []
    for i in range(number_of_element):
        random_numbers.append(random.randint(0, 9))
    return random_numbers

def luhn_algorithm(bin_input):
    # Ensure that bin_input is at least 6 digits long
    if len(bin_input) < 6:
        return "Invalid BIN (Minimum 6 digits)"

    # Convert bin_input to a list of integers
    bin_digits = [int(digit) for digit in bin_input]

    # Calculate the number of random digits needed to reach a total of 16 digits
    num_random_digits = 16 - len(bin_digits)

    random_master_int = bin_digits + make_random_number(num_random_digits)

    sum_even = []
    sum_odd = []
    for index, element in enumerate(random_master_int):
        if index % 2 != 0:
            r = random_master_int[index] * 2
            character_string = list(str(r))
            character_int = map(int, character_string)
            sum_even.append(sum(character_int))
        if index % 2 == 0:
            sum_odd.append(element)

    total_sum = sum(sum_even) + sum(sum_odd) * 9
    random_master_int.append((10 - (total_sum % 10)) % 10)  # last digit makes it a multiple of 10

    credit_card_number = ''.join(map(str, random_master_int))
    return credit_card_number.zfill(16)  

def generate_card_number():
    bin_input = bin_entry.get()
    if bin_input.isdigit() and len(bin_input) >= 6:
        card_number = luhn_algorithm(bin_input)
        card_number_display.config(text="Generated Card Number:\n" + card_number)
        pyperclip.copy(card_number)
        copy_button.config(state=tk.NORMAL)
    else:
        card_number_display.config(text="Invalid BIN (Minimum 6 digits)")

def copy_to_clipboard():
    card_number = card_number_display.cget("text").split("\n")[1]
    pyperclip.copy(card_number)

# main window
root = tk.Tk()
root.title("Credit Card Number Generator")

# input BIN
bin_label = tk.Label(root, text="Enter BIN (Bank Identification Number):")
bin_label.pack(pady=5)
bin_entry = tk.Entry(root)
bin_entry.pack(pady=5)

# generate Number
generate_button = tk.Button(root, text="Generate", command=generate_card_number)
generate_button.pack(pady=5)

# generated number
card_number_display = tk.Label(root, text="", wraplength=300)
card_number_display.pack(pady=5)

# Copy to clipboard
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=5)

root.mainloop()
