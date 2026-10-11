average = float(input("Enter your final average grade:(0/10)\t"))
frequency = int(input("Enter you frenquency:(0/100)%\t"))

if (average < 0 or average > 10) or (frequency < 0 or frequency > 100):
 print("Invalid entrance") 


elif average >= 7 and frequency >= 75.0 :
  print("Approved")

else:

 if average < 7 and frequency >= 75.0:
   print("Reproved due to average")

 elif average > 7 and frequency < 75.0:
   print("Reproved due to frequency")

 else:
   print("Reproved")