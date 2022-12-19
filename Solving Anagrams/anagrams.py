from load_dictionary import load_file
#loading the word list
dict_file=load_file("2of12.txt")

#loading the word
chosen_word= input("Please enter a word (I am going to show an anagram)\n")
anagram_list=[]

#comparing the word with the words in the dictionary  
for word in dict_file:
    if sorted(chosen_word) == sorted(word):
        anagram_list.append(word)

#removing the input word from the anagram word list
anagram_list.remove(chosen_word)

#checking and displaying the anagram words
if len(anagram_list) == 0:
    print("There are no anagrams present! Try again")
else:
    print(f"The anagrams are: \n {anagram_list}")