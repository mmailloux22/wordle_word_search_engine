import re

def read_data(filename):
    wordlelist = []
    with open(filename) as wordlist:
        for word in wordlist:
            wordlelist.append(word[:-1])
    return wordlelist

def wordle_search(wordlelist) -> None:
    while True:
        
        matches = []

        while len(matches) == 0:
            
            search_term = input("Enter your search term: ")
            
            if search_term == '':
                exit()
            if len(search_term) > 5:
                print("Your search term MUST be 5 characters or less!")
            
            matches = [i for i in wordlelist if re.match(search_term, i, flags=re.IGNORECASE)]
            if len(matches) == 0 and len(search_term) <= 5:
                print('There are no matches for your search term.')


        print('\nResults:')
        for match in matches:
            print(match)

if __name__ == '__main__':
    print('\nWordle Search Engine\n')
    print('Instructions:\nType in a five letter word using a combination of letters (abcd) and periods (.),') 
    print('the search engine will show you all the matching words. Enter nothing to exit.\n')
    print("'.' = any letter")
    print('Example: a.b.c\n')

    wordle_search(read_data('words.txt'))