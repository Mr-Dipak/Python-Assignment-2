fsl = int(input("Please Enter your fasting sugar level: "))
if (fsl >= 80 and fsl <=100):
    print("your fasting sugar level is normal")

elif fsl < 80:
    print("your fasting sugar level is low")

else:
    print ("your fasting sugar level is high")