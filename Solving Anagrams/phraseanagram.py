import sys
from collections import Counter
import load_dictionary

#loading the dictionary

dict_file=load_dictionary.load_file("2of12.txt")
#In the load dictionary file I had removed the single letters which have eliminated the possibility of having I and a (most common words)
#appending i and a in the dictionary
dict_file.append("a")
dict_file.append("I")
dict_file=sorted(dict_file)

#input the text for which anagram has to be created
ini_name=input("Please enter the text you want a phrase anagram!")

#function to identify the phrase anagram

def find_anagrams(name, word_list):
    """ Reads the name and displays all anagrams as per the word list"""
    name_letter_map=Counter(name)
    anagrams=[]
    for word in word_list:
        test=''
        word_letter_map=Counter(word) #in the original program the word is converted into lower but I have already made the change while creating the word list
        for letter in word:
            if word_letter_map[letter]<=name_letter_map[letter]:
                test+=letter
            if Counter(test)==word_letter_map:
                anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print(f"Remaining letters = {name}")
    print(f"The number of remaining letters {len(name)}")
    print(f"Number of remaining real world anagrams {len(anagrams)}")

def process_choice(name):
    """ Checks the user choice for validity, return choice and leftover letters """
    choice = input(" \n Please make a choice else enter to start over or # to end: ")
    while True:
        if choice==" ":
            main()
        elif choice=="#":
            sys.exit()
        else:
            candidate = "".join(choice.lower().split())
        left_over_list= list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) -  len (left_over_list) == len(candidate):
            break
        else:   
            print("won't work! Make another choice", file=sys.stderr)
    name="".join(left_over_list)
    return choice, name

def main():
    """helps the user build anagram from a phrase"""
    name = ''.join(ini_name.lower().split())
    limit = len(name)
    phrase = ''
    running = True
    while running:
        temp_phrase = phrase.replace(' ','')
        if len(temp_phrase) < limit:
            print(f"The length of angaram phrase {len(temp_phrase)}")

            find_anagrams(name, dict_file)
            print("Current anagram phrase = ", end=" ") 
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase+=choice + ' '
        elif len(temp_phrase) == limit:
            print("\n *** FINISHED **** \n")
            print("Anagram of name = ", end= " ")
            print(phrase, file =sys.stderr)
            print()
            try_again = input("\n\n Try again? (press Enter else 'n' to quit) \n ")
            if try_again.lower()=="n":
                running = False
                sys.exit()
            else:
                main()
if __name__=='__main__':
    main()

