#program to input in seconds and convert it into hours,minutes,and
#input of time in second
second = int(input("Enter time in seconds:"))
#----------------------------------------------
#initializing no.of hours and minutes
minutes = 0
hours = 0
#calculating hours
if(second >= 3600):
   hours = second // 3600 #storing quotient as hours
   second = second % 3600 #storing quotient as hours
   #calculating minutes
   if(second >= 60):
       minutes = second // 60 #storing quotient as minutes
       second = second% 60 #storing remainder as seconds
       #printing time in hours,minutes and seconds 