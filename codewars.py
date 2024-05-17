def generate_hashtag(s):
    words = s.split()
    if not s or len(s.strip()) == 0:
        return False

    capitals = '#' + ''.join(word.capitalize() for word in words)
    
    if len(capitals) > 140:
        return False
    else:
        return capitals

# Test case
print(generate_hashtag("Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat"))