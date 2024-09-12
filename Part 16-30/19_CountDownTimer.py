import time

Mytime = int(input("Enter your time in Seconds: "))

for x in range(Mytime,0,-1):
    second = x%60
    minute = int(x/60) % 60
    hour = int(x/3600) % 3600
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)
    

print("Good Morning!!")