
HANGMAN_PHOTOS = {0:"""x-------x""",
                  1: """x-------x
|
|
|
|
|""",
      2: """x-------x
|       |
|       0
|
|
|"""
      ,3:""" x-------x
 |       |
 |       0
 |       |
 |
 |""",
      4:""" x-------x
|       |
|       0
|      /|\\
|
|""",
      5:"""x-------x
|       |
|       0
|      /|\\
|      /
|
""",
      6:"""x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}





def print_home_page():
    """print home page"""
    HANGMAN_ASCII_ART = """ 
    Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                          |___/"""

    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART + '\n' + str(MAX_TRIES))




def check_valid_input(letter_guessed, old_letters_guessed):
    """check letter: if english letter and length = 1 -> return true
    else -> return false"""
    if letter_guessed in old_letters_guessed:
        return False
    elif len(letter_guessed) != 1:
        return False
    elif not letter_guessed.isalpha():
        return False
    else:
        print(str(letter_guessed).lower())
        return True



def check_good_guess(letter_guessed,word):
    """returns true if the letter that guessed is in the secret word,
    returns false if not"""
    if letter_guessed.lower() in word:
        return True
    return False



def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """using validation check to check the letter: if its ok -> return true,
     else -> print old letters guessed by order and return false"""
    if check_valid_input(letter_guessed.lower(),old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        old_letters_guessed.sort()
        print(" -> ".join(old_letters_guessed))
        return False



def show_hidden_word(secret_word, old_letters_guessed):
    """printing the secret word with "_" where the letters didn't guessed"""
    string_to_return = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            string_to_return += letter
            string_to_return += " "
        else:
            string_to_return += "_ "
    return string_to_return



def check_win(secret_word, old_letters_guessed):
    """check if all letters guessed - win"""
    output_string = show_hidden_word(secret_word,old_letters_guessed)
    if "_" in output_string:
        return False
    return True



def check_if_end(secret_word, old_letters_guessed, num_of_trys):
    """check if player out of trys"""
    if check_win(secret_word,old_letters_guessed) or num_of_trys == 6:
        return True
    return False


def print_hangman(num_of_tires):
    print(HANGMAN_PHOTOS.get(num_of_tires))




def choose_word(file_path, index):
    """get the file path and the index of the number,
     returns the word in index place in the file"""
    selected_word = ""
    file = open(file_path, "r")
    for line in file:
        words = line.split()
        if 0 <= index < len(words):
            selected_word = words[index]
            break
    return selected_word


def handle_end_game(num_of_miss):
    if num_of_miss == 6:
        print("LOSS!")
    else:
        print("WIN!")

def main():
    print_home_page()
    path = input("Enter file path: ")
    index = input("Enter index: ")
    try:
        word = choose_word(path,int(index))
        old_letters_guessed = []
        num_of_miss = 0
        print("Let's start!")
        print_hangman(num_of_miss)
        while not check_if_end(word,old_letters_guessed,num_of_miss):

            print(show_hidden_word(word,old_letters_guessed))
            letter = input("\nguess a letter: ")
            if try_update_letter_guessed(letter,old_letters_guessed):
                if check_good_guess(letter,word):
                    print("Good Job!")
                else:
                    print("):")
                    num_of_miss += 1
                    print_hangman(num_of_miss)
        handle_end_game(num_of_miss)
    except FileNotFoundError:
        print("there's been an error while opening the file, try again")







if __name__ == "__main__":
    main()

