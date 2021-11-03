weight = float(input ("Enter your weight in kg:"))
Height = float(input("Enter your height in cm:"))

height_meters =(weight/100)

BMI = round(weight/ (height_meters **2),2)

print("your body mass index is:", end='')

if BMI < 18.5 :
 print("Under_weight")

elif   (BMI == 18.5)  or (BMI <= 24.5):

   print("Normal")  

elif    BMI == 25 or (BMI >= 29.9):

  print("Over_weight")

else : print("Obesity")

