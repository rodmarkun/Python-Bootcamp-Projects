#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def main():
    file_letter = open("./Input/Letters/starting_letter.txt", "r")
    file_names = open("./Input/Names/invited_names.txt", "r")
    names = file_names.readlines()
    file_names.close()
    letter_string = file_letter.read()
    for name in names:
        name = name.strip()
        letter = letter_string.replace("[name]", name)
        filename = "./Output/ReadyToSend/letter_for_" + name + ".txt"
        file_letter_to_send = open(filename, "w+")
        file_letter_to_send.write(letter)
        file_letter_to_send.close()
    file_letter.close()

main()