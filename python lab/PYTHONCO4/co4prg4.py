class Time:
    def __init__(self):
        self.__h=int(input("enter the hour:"))
        self.__m=int(input("enter the minutes:"))
        self.__s=int(input("enter the seconds:"))
        
    def __add__(self,tobj2):
        hours=self.__h+tobj2.__h
        print("sum of hours",hours)
        minutes=self.__m+tobj2.__m
        print("sum of hours",hours)
        seconds=self.__s+tobj2.__s
        print("sum of hours",hours)
        if minutes>=60:
            hours=hours+1
            minutes=minutes-60
        if seconds>=60:
            minutes=minutes+1
            seconds=seconds-60
        return seconds,minutes,hours
print()

        
    
        
        
        