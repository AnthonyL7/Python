print("Welcome to today's pop quiz")
print("Half of the questions are written and the others are multiple choice")
written = {"Question 1: How many days are in a year? ": [365, 366],   
 "Question 2: How many seconds are in a minute? ": [60, 59],
 "Question 3: How many mintues in an hour? ": [60, 59],
 "Question 4: Is it cold during the winter? ": 'yes',
 "Question 5: Is it hot during the summer?" : 'yes'}
  #Multiple Choice 

multiple_choice = {"Question 6: What is the capital of France": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], 
  "Question 7: Which planet is known as the Red Planet?": ["A. Earth", "B. Mars", "C. Jupyter", "D. Venus"],
  "Question 8: What is the largest ocean on Earth?": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Artic Ocean", "D Pacific Ocean"], 
  "Question 9: Who wrote 'To Kill a Mockingbird?": ["A. Harper Lee", "B Jane Austen", "C. Mark Twain", "D. J.K. Rowling"],
  "Question 10: Who painted the Mona Lisa?": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"]
}

#Answers

#Get user input for Number 1
def quiz(q):
  for question, answers in q.items():
    print(question)
    user_answer = input("Answer: ")

    try: 
      user_answer = int(user_answer)
    except ValueError:
      pass

    if user_answer in answers: 
      print("correct")
    else: 
      print("incorrect")

quiz(written)





