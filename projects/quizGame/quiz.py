print("Welcome to today's pop quiz")
print("Half of the questions are written and the others are multiple choice")
questions = {"Question 1: How many days are in a year? ": 365,   
 "Question 2: How many seconds are in a minute? ": 60,
 "Question 3: How many mintues in an hour? ": 60,
 "Question 4: Is it cold during the winter? ": 'yes',
 "Question 5: Is it hot during the summer?" : 'yes',
  #Multiple Choice 
  "Question 6: What is the capital of France": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], 
  "Question 7: Which planet is known as the Red Planet?": ["A. Earth", "B. Mars", "C. Jupyter", "D. Venus"],
  "Question 8: What is the largest ocean on Earth?": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Artic Ocean", "D Pacific Ocean"], 
  "Question 9: Who wrote 'To Kill a Mockingbird?": ["A. Harper Lee", "B Jane Austen", "C. Mark Twain", "D. J.K. Rowling"],
  "Question 10: Who painted the Mona Lisa?": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"]
}

#Answers

#Get user input for Number 1
def get_1(written):
  print(written)
  user_answer = int(input("Answer: "))
  check_1(user_answer)

#Get user input for Number 2
def get_2(written):
  print(written)
  user_answer = int(input("Answer: "))
  check_2(user_answer)

#Get user input for Number 3
def get_3(written):
  print(written)
  user_answer = int(input("Answer: "))
  check_3(user_answer)

#Get user input for Number 4
def get_4(written):
  print(written)
  user_answer = input("Answer: ")
  check_4(user_answer)

#Get user input for Number 5
def get_5(written):
  print(written)
  user_answer = input("Answer: ")
  check_5(user_answer)


#Get multiple choice for number 6
def get_multiple_choice_6(question):
  for i in question:
    print(i)
  
  user_answer = input("Answer: ")
  check_6(user_answer)

#Get multiple choice for number 7
def get_multiple_choice_7(question):
  for i in question:
    print(i)
  
  user_answer = input("Answer: ")
  check_7(user_answer)

#Get multiple choice for number 8
def get_multiple_choice_8(question):
  for i in question:
    print(i)
  
  user_answer = input("Answer: ")
  check_8(user_answer)

#Get multiple choice for number 9
def get_multiple_choice_9(question):
  for i in question:
    print(i)
  
  user_answer = input("Answer: ")
  check_9(user_answer)

#Get multiple choice for number 10
def get_multiple_choice_10(question):
  for i in question:
    print(i)
  
  user_answer = input("Answer: ")
  check_10(user_answer)


#Check the answer by passing get_ into check_
#Check Number 1
def check_1(user_answer):
  if user_answer != answer[0]:
    print("incorrect")
  else:
    print("correct")

#Check Number 2
def check_2(user_answer):
  if user_answer != answer[1]:
    print("incorrect")
  else:
    print("correct")

#Check Number 3
def check_3(user_answer):
  if user_answer != answer[2]:
    print("incorrect")
  else:
    print("correct")

#Check Number 4
def check_4(user_answer):
  if user_answer.lower() == answer[3]:
    print("correct")
  else:
    print("incorrect")

#Check Number 5
def check_5(user_answer):
  if user_answer.lower() == answer[4]:
    print("correct")
  else:
    print("incorrect")

#Check Number 6
def check_6 (user_answer):
  if user_answer.lower() == answer[5]:
    print("correct")
  else:
    print("incorrect")

#Check Number 7
def check_7 (user_answer):
  if user_answer.lower() == answer[6]:
    print("correct")
  else:
    print("incorrect")

#Check Number 8
def check_8 (user_answer):
  if user_answer.lower() == answer[7]:
    print("correct")
  else:
    print("incorrect")

#Check Number 9
def check_9 (user_answer):
  if user_answer.lower() == answer[8]:
    print("correct")
  else:
    print("incorrect")

#Check Number 10
def check_10 (user_answer):
  if user_answer.lower() == answer[9]:
    print("correct")
  else:
    print("incorrect")


get_1(q1)
get_2(q2)
get_3(q3)
get_4(q4)
get_5(q5)
get_multiple_choice_6(q6)
get_multiple_choice_7(q7)
get_multiple_choice_8(q8)
get_multiple_choice_9(q9)
get_multiple_choice_10(q10)



