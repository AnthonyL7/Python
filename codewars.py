#Complete the solution so that the function will break up camel casing, using a space between words.
import re
def solution(s):
    
    if " " in s:
        new = s.replace(" ", "")
        print(new)
    elif s:
        space = re.findall(r'[A-Z][a-z]*|[a-z]+', s)
        new_word = ' '.join([word + ' ' for word in space])
        print(new_word)
    else: 
        print(s)

solution("want Say")