# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 02:22:58 2017

@author: Mark
"""

import arrow

class MeetingTime:
    
    def __init__(self, day = "Mon", start_time = 800, end_time = 1000):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
    
    def get_day(self):
        return self.day
    
    def get_start_time(self):
        return self.start_time
    
    def get_end_time(self):
        return self.end_time
        
    def __str__(self):
        start_str = self._str_format_time(self.start_time)
        end_str = self._str_format_time(self.end_time)
        return (self.day+ " " + start_str + " - " + end_str)
    
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
x =  MeetingTime()
print("\n" + str(x))

x.start_time = 0
x.end_time = 1403
print(x)
"""