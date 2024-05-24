story = "It was a [adjective] day in [place]. [Person's name] decided to go to the [noun]. On the way, [he/she/they] saw a [adjective] [animal] that was [verb ending in -ing] in the middle of the [noun]. [Exclamation]! [Person's name] said. 'That is the most [adjective] thing I have ever seen!' After that, [Person's name] continued to the [noun] to [verb]. It was a truly [adjective] day."
print(story)
print("Fill in the following prompts to complete the story")

for i in range(4):
  adjective = input("Adjective: ")
for i in range(3):
  noun = input("Noun: ")
#print(place = input("Place: "))
place = input("Place: ")
pronouns = input("Pronoun: ")
name = input("name")
animal = input("Animal: ")
ing = input("Verb ending in -ing: ")
exclamation = input("Word containing exclamation: ")
sameName = input("Use the same person's name again: ")
verb = input("verb: ")


print(f"It was a {adjective} day in {place}. {name} decided to go to the {noun}. On the way, {pronouns} saw a {adjective} {animal} that was {ing} in the middle of the {noun}. {exclamation}! {sameName} said. 'That is the most {adjective} thing I have ever seen!' After that, {name} continued to the {noun} to {verb}. It was a truly {adjective} day.")