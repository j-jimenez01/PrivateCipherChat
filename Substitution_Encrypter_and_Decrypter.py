import random
symbols = {",":",",".":".",":":":",";":";","?":"?","!":"!","-":"-"," ":" ","'":"'"}#global variables for symbols since i am not mixing these with the letters
#this function is to encrypt the phrase passed in with the key used. This will be able to 
#hide any phrases without people knowing
def encryption(phrase,key):
    newPhrase = ""
    for x in phrase.lower():
        if x in key:
            newPhrase += key[x]
        else:
            newPhrase += symbols[x]
    return newPhrase

#this function is going to decrypt the phrase from the encryption and use the same key to
#be able to translate the encrypted message backe to the phrase.
def decryption(phrase,key):
    oldPhrase = ""
    #creating a new hash table to swap the keys and values so we can decode
    keySwap = {}
    for x in key:
        keySwap[key[x]] = x
    #checking the swap hash table so the letters go back to the correct order
    for x in phrase:
        if x in keySwap:
            oldPhrase += keySwap[x]
        else:
            oldPhrase += symbols[x]
    return oldPhrase

#main
#making a list of strings to say which option is happening
items = ["Encypt?","Decrypt?"]
while True:
    print("1. Encryption\n2. Decryption\n3. Quit")
    option = int(input("Enter the number of the option you would like to do: "))

    #assigning choice for encryption so we can use it to determine what option is going to happen
    if option == 1:
        choice = 0

    #assigning choice for decryption so we can use it to determine what option is going to happen
    elif option == 2:
        choice = 1

    else:
        #ending the program
        break

    #asking the user for a phrase and key
    phrase = input(f"What phrase would you like to {items[choice]}: ")
    letters = input("What is your key? ")
    #alphabet so we can make it set the key
    letters2 = "abcdefghijklmnopqrstuvwxyz"
    l1 = []#creating a list to randomize the letters 
    for x in letters: #making a for loop to add the letters in it
        l1.append(x)
    #making a hashtable because it will be easier to swap the letter in the functions
    key = {}
    for x in range(len(l1)):
        key[letters2[x]] = l1[x]

    #deciding if im doing encryption or decryption based off the users choice
    #passes the phrase and key into the function and then prints out what is returned
    if choice == 0:
        encrypt = encryption(phrase,key)
        print("\nEncytped Phrase is:", encrypt,"\n")
    else:
        decrypt = decryption(phrase,key)
        print("\nDecytped Phrase is:", decrypt,"\n")
