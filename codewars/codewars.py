import re
def solution(s):
    
    result = re.sub(r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])',' ', s)
    print(result)


solution("helloWorld")