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
# gold plated rings have base cost 50$ and engraving 7$
#.solid gold rings have base cost of 100$ and engraving 10$ per unit.

def cost_of_project(engraving, solid_gold):
  if solid_gold == True:
    cost = solid_gold * (100 + 10 * len(engraving))
  else:
    cost = (not solid_gold) * (50 + 7 * len(engraving))
    
  return cost 

print(cost_of_project("Kalki", True))