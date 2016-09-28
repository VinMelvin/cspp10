seconds = input("Enter Seconds: ")
sec = int(seconds) / 60
x_seconds = int(seconds) % 60
y = int(seconds) - x_seconds
minutes = y / 60 
c = int(minutes) % 60
hour= int(minutes) - c
print ({} + " seconds is " + {} + " hours, " + {} + " minute, and "  + {} + " seconds".format(seconds,hour,minutes,x_seconds))
