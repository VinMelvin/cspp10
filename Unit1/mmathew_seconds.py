seconds = input("Enter Seconds: ")
sec = int(seconds) / 60
x_seconds = int(seconds) % 60
y = int(seconds) - x_seconds
minutes = y / 60 
c = int(minutes) % 60
hour= int(minutes) - c
print (int(seconds) + "seconds is" + int(hour) + "hours," + int(minutes) + "minute, and" + int(x_seconds) + "seconds")
