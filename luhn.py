import tkinter as tk
import random
import pyperclip

def make_random_number(number_of_element):
    random_numbers = []
    for i in range(number_of_element):
        random_numbers.append(random.randint(0, 9))
    return random_numbers

def luhn_algorithm(bin_input):
    bin_digits = [int(digit) for digit in bin_input]
    random_master_int = bin_digits + make_random_number(10 - len(bin_digits))
    
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
    random_master_int.append(total_sum % 10)
    credit_card_number = ''.join(map(str, random_master_int))
    return credit_card_number

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

# Create the main window
root = tk.Tk()
root.title("Credit Card Number Generator")

# label and input field for the BIN
bin_label = tk.Label(root, text="Enter BIN (Bank Identification Number):")
bin_label.pack(pady=5)
bin_entry = tk.Entry(root)
bin_entry.pack(pady=5)

# button to generate a credit card number
generate_button = tk.Button(root, text="Generate", command=generate_card_number)
generate_button.pack(pady=5)

# label to display the generated card number
card_number_display = tk.Label(root, text="", wraplength=300)
card_number_display.pack(pady=5)

# "Copy" button to copy the card number to the clipboard
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=5)

root.mainloop()
