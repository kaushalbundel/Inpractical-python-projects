'''
loads a text file (dictionary) into a list
removes alphabets from the list

'''

import sys
empty_list=[]
def load_file(file):
    '''Open a text file and produces a list view with every word separated and in a lower case '''
    try:
        with open(file) as file_open:
            loaded_txt= file_open.read().strip().split('\n')
            loaded_txt=[x.lower() for x in loaded_txt]
            for i in range(len(loaded_txt)):
                if len(loaded_txt[i])>1:
                    empty_list.append(loaded_txt[i])
            return empty_list
    except IOError as e:
        print(f"{e} \n Error Opening {sys.stderr}. Terminating program")
        sys.exit(1)