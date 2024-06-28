file_1 = open("./Input/Names/invited_names.txt", "r")
names = file_1.readlines()
for name in names:
    name = name.strip()
    file_2 = open("./Input/Letters/starting_letter.txt", "r")
    letter_content = file_2.read()
    modified_letter = letter_content.replace("[name]", name)
    file_3 = open(f"./Output/ReadyToSend/{name}.txt", "w")
    final_letter = file_3.write(modified_letter)
    file_3.close()
    file_2.close()

file_1.close()


