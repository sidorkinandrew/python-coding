import pandas

data = pandas.read_csv("day_026_NATO_alphabet_data.csv")
#TODO 1. Create a dictionary in this format:
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
phonetic_dict = {letter: code for letter, code in zip(data["letter"], data['code'])}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
