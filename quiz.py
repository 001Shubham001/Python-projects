#quiz.py
print("Welcome to my Quiz")
 
playing = input("Do you want to play? \n")
  
if playing.lower()!= "yes":
      quit()
      
print("Okay Let's play xD")
score = 0
answer = input ("What is the full form of CGI ?\n")
      
if answer.lower() ==("computer graphics"):
 print("Correct!")
 score += 1
 
else:
    print("Incorrect!")
    
answer = input ("What is the full form of www ?\n")

if      answer.lower()==("world wide web"):
 print("Correct!")
 score += 1
 
else:
 print("Incorrect!")
          
answer = input ("What is the capital of INDIA ?\n")
      
if answer.lower() ==("delhi"):
 print("Correct!")
 score += 1
else:
    print("Incorrect!")
          
answer = input ("What is the batman's real name ?\n")
      
if answer.lower()==("bruce wayne"):
 print("Correct!")
 score += 1
else:
    print("Incorrect!")
          
answer = input ("What is the full form of ATS ?\n")
      
if answer.lower()==("anti terrorism squad"):
 print("Correct!")
 score += 1
else:
    print("Incorrect!")
          
print("you got" + str(score) + "questions correct")
print("you got" + str((score / 5)*100) + "%")