#Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
def get_grade(s1, s2, s3):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    F = 'F'
    avg = (s1+s2+s3)/3
    if 90 <= avg <= 100:
        print(A)
    elif 80 <= avg < 90:
        print(B)
    elif 70 <= avg < 80:
        print(C)
    elif 60 <= avg < 70:
        print(D)
    elif 0 <= avg < 60:
        print(F)

get_grade(100,100,100)

