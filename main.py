PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as letters:
    formal_letter =letters.read()

with open("./Input/Names/invited_names.txt") as guest_list:
    guest_lists = guest_list.readlines()
    for names in guest_lists:
        name = names.strip()
        new_letter = formal_letter.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as dispatch:
            dispatch.write(new_letter)
