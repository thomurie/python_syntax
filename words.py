def print_upper_words(words):
    """Converts strings from array into all uppercase words
    prints each word on its own line


    Args:
        words (Array): accepts array of strings

    Returns:
        prints each word from the array in all uppercase
    """
    for word in words:
        print(word.upper());

my_words = ["yes", "no", "maybe", "so"];

print_upper_words(my_words);

def only_es(words):
    """Only prints words that start with the letter "e"

    Args:
        Words (array): An array of strings
    
    Returns:
        Only prints words from the array that begin with the letter "E"
    """

    for word in words:
        if word[0].lower() == 'e':
            print(word)

some_e_words = ["tim", "Ein", "andre", "ed"]

only_es(some_e_words);

def words_by_letter(words, letters):
    """[summary]

    Args:
        words (array): [description]
        letters (array): [description]

    Returns:
        words that begin with any of the letters from the letters array
    """
    for word in words:
        for letter in letters:
            if word[0].lower() == letter:
                print(word)

words_by_letter(some_e_words, ["a", "e"])