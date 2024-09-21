print("welcome to my computer quiz")
playing=input("do you want to play")
input("enter yes or no:")
print("ok! lets play:)")
score = 0   

answer=input("what does cpu stand for?")
if answer.lower() == "central processing unit":
   print("correct")
   score += 1
else:
   print("incorrect!")   

answer=input("what does gpu stand for?")
if answer.lower() == "graphics processing unit":
   print("correct")
   score += 1
else:
   print("incorrect!")   

answer=input("what does ram stand for?")
if answer.lower() == "random access memory":
   print("correct")
   score += 1
else:
   print("incorrect!")   

answer=input("what does rom stand for?")
if answer.lower() == "read only memory":
   print("correct")
   score += 1
else:
   print("incorrect!")   

answer=input("what does cd stand for?")
if answer.lower() == "compact disk":
   print("correct")
   score += 1
else:
   print("incorrect!")   

answer=input("what does led stand for?")
if answer.lower() == "light emitting diode":
   print("correct")
   score += 1
else:
   print("incorrect!")   

answer=input("what does lcd stand for?")
if answer.lower() == "liquid crystal display":
   print("correct")
   score += 1
else:
   print("incorrect!")   

answer=input("what does rs stand for?")
if answer.lower() == "remote sensing":
   print("correct")
   score += 1
else:
   print("incorrect!")   

answer=input("what does gis stand for?")
if answer.lower() == "graphical information system":
   print("correct")
   score += 1
else:
   print("incorrect!")   

answer=input("what does www stand for?")
if answer.lower() == "world wide web":
   print("correct")
   score += 1
else:
   print("incorrect!")   


print("you got" + str(score) + "questions correct!")
print("you got" + str(score/10 * 100) + "%")



