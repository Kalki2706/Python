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

#The above print ine will take input from user 
#score after taking input it will return grade 
#the user got.
