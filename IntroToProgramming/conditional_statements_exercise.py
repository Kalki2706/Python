#Question 1
# "A" grade: 90-100, "B" grade: 80-89, "C" grade: 70-79, "D" grade: 60-69, "F" grade: less than 60

def get_grade(score):
  if score >= 90:
    grade = "A"
  elif score >= 80:
    grade = "B"
  elif score >= 70:
    grade = "C"
  elif score >= 60:
    grade = "D"
  else:
    grade = "F"
    
  return grade 

print(get_grade(score))

#The above print line will take input from user 
#after taking input of score it will print the grade 
#the user got.


#Question 2

#cost of project
