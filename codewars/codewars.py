#The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    word = word.lower()
    string = ''
    result = {}
    for letter in word:
        result[letter] = result.get(letter, 0) + 1
    for letter in word: 
        if result[letter] > 1:
            string += ")"
        else:
            string += "("
    print(string)
  
duplicate_encode('OGUF@hPwIZ(gf)Y(ULz pSy@bUseWhJRAsuD)ikc')