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


#Ask the user questions
q1_input = input(q1)
q2_input = input(q2)
q3_input = input(q3)
q4_input = input(q4)
q5_input = input(q5)

#Check written questions
def check_written_questions():
  
#Get multiple choice
def get_multiple_choice(question):
  for i in question:
    print(i)
  user_answer = input("Answer: ")
  question.append(user_answer)

  #Check if multiple choice inputs are correct
  if question == "Question 6: What is the capital of France" and user_answer == "C" or user_answer == "c":
    print("correct") 
  elif question == "Question 7: Which planet is known as the Red Planet?" and user_answer == "B" or user_answer == "b":
    print("correct")
  elif question == "Question 8: What is the largest ocean on Earth?" and user_answer == "D" or user_answer == "d":
    print("correct")
  elif question == "Question 9: Who wrote 'To Kill a Mockingbird?" and user_answer == "A" or user_answer == "a":
    print("correct")
  elif question == "Question 10: Who painted the Mona Lisa?" and user_answer == "C" or user_answer == "c":
    print("correct")
  else:
    print("incorrect")

get_multiple_choice(q6)
get_multiple_choice(q7)
get_multiple_choice(q8)
get_multiple_choice(q9)
get_multiple_choice(q10)


