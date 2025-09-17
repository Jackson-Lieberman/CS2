import random


def reverse_string(word):
    '''
    reverses a string 
    Args:
        word(str): the string being reversed
    Returns:
        str: the string reversed
    '''
    return word [:: -1] 

def count_vowels(word):
    '''
    counts the amount of vowels in a word
    Args:
        wiord(str): the string we are checking for vowels
    Returns:
        int: the amt of vowels in the word
    '''
    total_vowels = 0
#converts the word to lowercase for every letter in the word it will check if its in the list of vowels
#if it is, it will add one to the vowel score
    word = conv_lower(word)
    for char in word:                                        
        if char in ['a', 'e', 'i', 'o', 'u']:
            total_vowels += 1
    return total_vowels

def count_consonants(word):
    '''
    counts the amount of consonants in a word
    Args:
        word(str): the string we are checking for consonants
    Returns:
        int: the amt of consonants in the word
    '''
    total_consonants = 0
    #converts the word to lower case and for every letter in the word it will check if its in the list of vowels
    #if it is, it will add one to the consonants score
    word= conv_lower(word)
    for char in word:
         if char in ['b', 'c', 'd', 'f', 'g', 'h', 'j','k','l','m','n','p','q','r','s', 't', 'v', 'w', 'x', 'y', 'z']:
             total_consonants += 1
    return total_consonants


def return_last(name):
    '''
    returns last name
    Args:
        name(str): the name that the function takes in
    Returns:
        str: the last name
    '''
    last_name = ""

#for the length of the name, moving backwards, check if there is a space
#if there is a space, set the last space to index i
    for i in range(len(name), 0, -1):
        if name[i-1] == " ":
            last_space = i
            break
#from the last space to the end of the name add each letter
    for i in range(last_space, len(name)):
        last_name += name[i]

    return last_name
  


def return_first(name):
    '''
    returns first name
    Args:
        name(str): the name that the funciton takes in
    Returns:
        str: the first name
    '''
    title, new_name =check_title(name)#this will remove a title from the name if there is one
    first_space = len(new_name)  #fall back if there is only a first name
    #for the length of the name, check if there is a space. If there is a space set it to index i
    for i in range(len(new_name)):
        if new_name[i] == " ":
            first_space = i
            break 
    #add each letter to the first name variable until you reach the first space
    first_name = ""
    for i in range(first_space):
        first_name += new_name[i]
    return first_name

def return_middle(name):
    '''
    returns middle name
    Args:
        name(str): the name that the funciton takes in
    Returns:
        str: the middle name
    '''
    has_title, name =check_title(name)#this will remove a title from the name if there is one

    space = 0 
    # for the length of the name, check if there is a space. if there is a space, add one the space variable
    for char in name:
        if char == " ":
            space += 1

    #if there are les than 2spaces tell the user there is no middle name
    if space < 2:
        return "No middle name"
    #if not, set the the first and spaces by checking for spaces through the name
    else:
        first_space = 0
        last_space = 0
        for i in range(len(name)):
            if name[i] == " ":
                first_space = i+1
                break
        else:
            first_space+=1
        for i in range(len(name), 0, -1):
            if name[i-1] == " ":
                last_space = i
                break
        
        #from the first space to the last space return each character
        middle_name = ""
        for i in range(first_space, last_space-1):
            middle_name += name[i]
        return middle_name

def find_hyphen (name):
    '''
    checks if last name has a hyphen
    Args:
        name(str): the name that the funciton takes in
    Returns:
        bool: if the last name is hyphenated
    '''
    last_space = -1
    #goes backwards through the name until there is a space and when there is a space, set it to the variable last space
    for i in range(len(name) - 1, -1):
        if name[i] == " ":
            last_space = i
            break
    #from the last space to the end of the name check every character to see if its a hyphen and return a boolian on wether or not one is present
    for i in range(last_space + 1, len(name)):
        if name[i] == "-":
            return True
    return False

def conv_lower(word):
    '''
    converts a word to lower case
    Args:
        word(str): the word that the funciton takes in
    Returns:
        str: the lower case word
    '''
    new_word= []
    #for every letter in the given word set it to its ordinal value
    for letter in word:
        int_value= ord(letter)
    #if the ordinal value if less than 90 and greater than 65(diserning that the word is upper case), add 32 to the ordinal value(changing the letter from uppercase to lower case)
        if int_value>=65 and int_value<=90:
            int_value= int_value+32
    #adds the character associated with the new ordinal value to the new word
        new_word+= chr(int_value)
    final_word = ""
    #add the characters from the new word into a string which is the final word
    for char in new_word:
        final_word += char
    return final_word

def conv_upper(word):
    '''
    converts a word to upper case
    Args:
        word(str): the word that the funciton takes in
    Returns:
        str: the upper case word
    '''
    new_word= []
    #for every letter in the given word set it to its ordinal value
    for letter in word:
        int_value= ord(letter)
    #if the ordinal value if less than 122 and greater than 97(diserning that the word is lower case), subtract 32 to the ordinal value(changing the letter from lower case to upper case)
        if int_value<=122 and int_value>=97:
            int_value= int_value-32
    #adds the character associated with the new ordinal value to the new word
        new_word+=chr(int_value)
    final_word = ""
    #add the characters from the new word into a string which is the final word
    for char in new_word:
        final_word += char
    return final_word


def rand_name(name):
    '''
    modifies a name to mix up the letters
    Args:
        name(str): the name being randomized
    Returns:
        str: the randomized letters of the name
    '''
    #makes a list of the characters in your name
    name_array = list(name) 
    #shuffles the characters in the list
    random.shuffle(name_array)
    randomized_name = ""
    #adds each letter in the scrambled array to a string
    for char in name_array:
        randomized_name += char
    
    return randomized_name


def is_palindrome(name):
    '''
    checks if a name is a palendrome
    Args:
        name(str): the string being checked if its a palindrome
    Returns:
        bool: if the string is a palendrome
    '''
    #reverses the name and checks if its equal to the the first name
    reverse = name[:: -1]
    return reverse == name

def sort_name(name): 
    '''
    Takes a name and returns it as a sorted array of characters in alphabetical order
    Args:
        name(str): persons name that is being sorted
    Returns:
        array: the array of the sorted name
    '''
    #sorts the name alphabetically and by capitols and special characters
    return sorted(name)

def get_initials(name): 
    '''
    Takes a name and returns the initials
    Args:
        name(str): persons name for the initals
    Returns:
        str: the persons initals
    '''
    #defines first, middle, and last names from inputted information
    middle = return_middle(name)
    first = return_first(name)
    last = return_last(name)

    #checks if there is a middle name or not and assigns the initals as the first element in each name accordingly
    if middle == "No middle name":
        initials = f'{first[0]} {last[0]}'
    else:
        initials = f'{first[0]} {middle[0]} {last[0]}'

    return initials

#REMOVE . SPLIT
def check_title(name): 
    '''
    checks if a name contains a title/distinction
    Args:
        name(str): persons name thats being checked
    Returns:
        bool: if the name has a title
        str: either the name without the distiction or the name
    '''
    first_space = len(name)  #fall back if there is only a first name
    #for the length of the name, check if there is a space. If there is a space set it to index i
    for i in range(len(name)):
        if name[i] == " ":
            first_space = i
            break 
    #add each letter to the first name variable until you reach the first space
    first_name = ""
    for i in range(first_space):
        first_name += name[i]

    titles = ['Dr.', 'Sir', 'Esq', 'Ph.d']
    #checks if the first piece of the name is in the list of titles
    
    if first_name in titles:
        #Removes the title from the name
        new_name = ""
        for i in range(first_space, len(name)):
            new_name += name[i]
        return True, new_name.strip(' ')
    else:
        new_name = name
        return False, new_name.strip(' ')
        
    

def menu():
    '''
    Runs all funtions
    Args:
        none
    '''
    word = input("what is your word")
    name = input('what is your full name')
    while True:
        option = input('''
                       What would you like to do? 
                       1.Reverse a string
                       2.Count constanants, 
                       3.Count vowels, 
                       4.Return first name, 
                       5.Return last name, 
                       6.Return middle name(s), 
                       7.Check if your last name has a hyphen, 
                       8.Convert a word to lowercase, 
                       9.Convert a word to uppercase, 
                       10.Mix up a name, 
                       11.Check if your first name is a palendrome
                       12.Sort your name
                       13.Make intials from your name
                       14.Check for distinction
                       ''')
   
        if option == '1':
            print('Lets reverse your word')
            print(reverse_string(word))
        elif option == '2':
            print('Lets count the constanants in your word')
            print(count_consonants(word))
        elif option == '3':
            print('Lets count the vowels in your word')
            print(count_vowels(word))
        elif option == '4':
            print('Lets get your first name')
            print(return_first(name))
        elif option == '5':
            print('Lets get your last name')
            print(return_last(name))
        elif option == '6':
            print('Lets get your middle name(s)')
            print(return_middle(name))
        elif option == '7':
            print('Lets check if your name contains a hyphen')
            print(find_hyphen(name))
        elif option == '8':
            print('Lets make your word lowercase')
            print(conv_lower(word))
        elif option =='9':
            print('Lets make your word uppercase')
            print(conv_upper(word))
        elif option == '10':
            print('Lets mix up your name')
            print(rand_name(name))
        elif option == '11':
            print('Lets check if your name is a palendrome')
            print(is_palindrome(name))
        elif option == '12':
            print('Sort your name by letter')
            print(sort_name(name))
        elif option == '13':
            print('Lets make intials for your name')
            print(get_initials(name))
        elif option == '14':
            print('Lets check if your name has a distiction')
            has_title, name = check_title(name)
            print(has_title)
    
menu()

