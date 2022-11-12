import glob
from os import path

PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()

for a_letter in glob.glob('./input/letters/*.txt'):
    fname = path.basename(a_letter)
    fname = path.splitext(fname)[0]
    with open(a_letter) as letter_file:
        letter_contents = letter_file.read()
        for name in names:
            stripped_name = name.strip()
            new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
            with open(f"./output/ready_to_send/{fname}_letter_for_{stripped_name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)

