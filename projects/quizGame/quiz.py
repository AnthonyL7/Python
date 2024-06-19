print("Welcome to today's pop quiz")
print("Half of the questions are written and the others are multiple choice")
q1 ="Question 1: How many days are in a year? "  
q2 = "Question 2: How many seconds are in a minute? " 
q3 = "Question 3: How many mintues in an hour? "
q4 = "Question 4: Is it cold during the winter? "
q5 = "Question 5: Is it hot during the summer? "
#Multiple Choice 
q6 = ["Question 6: What is the capital of France", "A. Berlin", "B. Madrid", "C. Paris", "D. Rome"] 
q7 = ["Question 7: Which planet is known as the Red Planet?", "A. Earth", "B. Mars", "C. Jupyter", "D. Venus"]
q8 = ["Question 8: What is the largest ocean on Earth?", "A. Atlantic Ocean", "B. Indian Ocean", "C. Artic Ocean", "D Pacific Ocean"] 
q9 = ["Question 9: Who wrote 'To Kill a Mockingbird?", "A. Harper Lee", "B Jane Austen", "C. Mark Twain", "D. J.K. Rowling"]
q10 = ["Question 10: Who painted the Mona Lisa?", "A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"]

#Answers
answer = [365, 60, 60, "yes", "yes", "c", "b", "d", "a", "c"]

def check_written_questions():
  pass
#Get multiple choice
def get_multiple_choice_answer(question):
  ##question.append(user_answer)
  for i in question:
    print(i)
  user_answer = input("Answer: ")
  check_6(user_answer)
  check_7(user_answer)
  check_8(user_answer)
  check_9(user_answer)
  check_10(user_answer)
  
#Check Number 6
def check_6 (user_answer):
  if user_answer.lower() == answer[5]:
    print("correct")
  elif user_answer.lower() != answer[5]:
    print("incorrect")

#Check Number 7
def check_7 (user_answer):
  if user_answer.lower() == answer[6]:
    print("correct")
  elif user_answer.lower() != answer[6]:
    print("incorrect")

#Check Number 8
def check_8 (user_answer):
  if user_answer.lower() == answer[7]:
    print("correct")
  elif user_answer.lower() != answer[7]:
    print("incorrect")

#Check Number 9
def check_9 (user_answer):
  if user_answer.lower() == answer[8]:
    print("correct")
  elif user_answer.lower() != answer[8]:
    print("incorrect")

#Check Number 10
def check_10 (user_answer):
  if user_answer.lower() == answer[9]:
    print("correct")
  elif user_answer.lower() != answer[9]:
    print("incorrect")

get_multiple_choice_answer(q6)
get_multiple_choice_answer(q7)
get_multiple_choice_answer(q8)
get_multiple_choice_answer(q9)
get_multiple_choice_answer(q10)



