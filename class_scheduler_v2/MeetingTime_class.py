# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 01:07:25 2017

@author: Mark
"""


class MeetingTime:
    
    def __init__(self, day = "Mon", start_time = 800, end_time = 1000):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.duration = self._duration() #tuple of hours and minutes
    
    def _duration(self):
        hrs = (self.end_time // 100) - (self.start_time // 100)
        mins = (self.end_time % 100) - (self.start_time % 100)
        if (self.end_time % 100) < (self.start_time % 100):
            hrs -= 1
            mins += 60
        return (hrs, mins)
            
    
    def get_day(self): #only so class method can be passable, w/ instance param
        return self.day
    
    def get_start_time(self): #only so class method can be passable, w/ instance param
        return self.start_time
    
    def get_end_time(self): #only so class method can be passable, w/ instance param
        return self.end_time
    
    def get_duration(self): #returns tuple with (hrs, mins)
        return self.duration
        
    def get_duration_minutes(self): #returns number of minutes
        minutes_duration = self.duration[0] * 60 + self.duration[1]
        return minutes_duration
    
    def get_duration_hours(self): #returns float, number of hours (with decimal)
        hours_duration = self.get_duration_minutes() / 60
        return hours_duration
    
    def day_str(self):
        return self.get_day()
        
    def start_time_str(self):
        return self._str_format_time(self.start_time)
    
    def end_time_str(self):
        return self._str_format_time(self.end_time)
    
    def duration_str(self):
        hrs = str(self.duration[0])
        mins = str(self.duration[1])
        if len(mins) == 1:
            mins = "0" + mins
        return hrs + ":" + mins
        
    def __str__(self):
        start_str = self.start_time_str()
        end_str = self.end_time_str()
        return (self.day + (" " * (7-len(self.day)))  + start_str  \
        + (" " * (11-len(start_str))) + "-" + (" " * 4) + end_str)
    
    def _str_format_time(self, time):
        
        ampm = "AM" if (time - 1200 < 0) else "PM" #determines am / pm
        
        if time // 1300 == 1: #determintes 12hr format
            hour_str = str((time - 1200) // 100)
        else:
            hour_str = str(time // 100)
        
        if hour_str == "0":
            hour_str = "12"
        
        minute_str = str(time % 100)
        
        if len(minute_str) == 1:
            minute_str = "0" + minute_str
        
        time_str = "{}:{} {}".format(hour_str, minute_str, ampm)
        
        return time_str
        
        
    def __repr__(self):
        return str(self)




"""
def call_method(class_method, obj):
    return class_method(obj)

x = MeetingTime()

day = call_method(MeetingTime.get_day, x)
start = call_method(MeetingTime.get_start_time, x)
end = call_method(MeetingTime.get_end_time, x)
print(day, start, end)

z = [day, start, end]
for i in z:
    print(type(i))
"""

