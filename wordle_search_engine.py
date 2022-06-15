import re

def read_data(filename):
    wordlelist = []
    with open(filename) as wordlist:
        for word in wordlist:
            wordlelist.append(word[:-1])
    return wordlelist

def wordle_search(wordlelist) -> None:
    
    excluded_set = set()
    excluded_letters_string = ''
    
    while True:

        matches = []

        while len(matches) == 0:
            
            search_term = input('Enter your search term: ')
            
            if search_term == '':
                exit()

            if len(search_term) > 5:
                print('Your search term MUST be 5 characters or less!')

            else:
                excluded_letters = input('Enter excluded letters: ')

                if excluded_letters:
                    for letter in excluded_letters:
                        excluded_set.add(letter)
                    
                    excluded_letters_string = ''
                    for letter in excluded_set:
                        if letter.isalpha():
                            excluded_letters_string += letter + '|'

                if excluded_letters_string:
                    search_term = '^(?!.*(' + excluded_letters_string[:-1] + ')).*' + search_term
                
                matches = [i for i in wordlelist if re.match(search_term, i, flags=re.IGNORECASE)]
                if len(matches) == 0 and len(search_term.split('*')[0]) <= 5:
                    print('There are no matches for your search term.')

        print('\nResults:')
        for match in matches:
            print(match)
        
        print('\nContinue searching for the same Wordle?')
        continue_search = input("If yes, hit Enter. To search for a new wordle enter 'w'. To exit enter q:\n")

        if continue_search == 'w':
            excluded_set.clear()
            excluded_letters_string = ''

        if continue_search == 'q':
            exit()

if __name__ == '__main__':
    print('\nWordle Search Engine\n')
    print('Instructions:\nType in a five letter word using a combination of letters (abcd) and periods (.),') 
    print('the search engine will show you all the matching words. Enter nothing to exit.\n')
    print("'.' = any letter")
    print('Example: a.b.c\n')

    wordle_search(read_data('words.txt'))