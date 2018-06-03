# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:09:53 2017

@author: Mark
"""

from MeetingTime_class import MeetingTime
import math

class Schedule:
    
    def __init__(self, course_dict, schedule_lst):
        
        self.day_times_dict = {} # holds MeetingTime objects for each day of week
        self.schedule_list = schedule_lst
        self.num_credits = 0 # num of credits this schedule represents
        self.priority_score = 0  # create priority score for Schedule
        
        # initialized; going to be assigned to MeetingTime objects later
        self.earliest_times = None
        self.latest_times = None
        self.avg_times = None
        
        for course, section in self.schedule_list:
            self.num_credits += course_dict[course].no_credits() # adds credits
            self.priority_score += course_dict[course].priority # adds priority scores of classes
        
        # creates MeetingTime objects for each day of the week
        
        for course, section in self.schedule_list: # for eac c-s (course-section)
            curr_section_obj = course_dict[course][section]
            
            for meeting_time in curr_section_obj: # for each meeting time in c-s object
                day = meeting_time.day 
                start_time = meeting_time.start_time
                end_time = meeting_time.end_time
                
                if day in self.day_times_dict: # if day of week already in day_time_dict
                    if self.day_times_dict[day].start_time > start_time: # update value
                        self.day_times_dict[day].start_time = start_time
                    
                    if self.day_times_dict[day].end_time < end_time: # update value
                        self.day_times_dict[day].end_time = end_time
                else: # day of week not in day_time_dict yet, so initialize
                    self.day_times_dict[day] = MeetingTime(day, start_time, end_time)
        
        
        #methods for getting MeetingTime start & end times
        # either of these is going to be passed as parameter, to be called on MeetingTime object
        start_method = MeetingTime.get_start_time # method to get start time of MeetingTime instance
        end_method  = MeetingTime.get_end_time # method to get end time of MeetingTime instance
        
        # get earliest start & end, latest start & end, and avg start & end
        
        earliest_start = self._earliest_time(start_method)
        earliest_end = self._earliest_time(end_method)
        
        latest_start = self._latest_time(start_method)
        latest_end = self._latest_time(end_method)
        
        avg_start = self._avg_time(start_method)
        avg_end = self._avg_time(end_method)
        
        
        
        self.earliest_times = MeetingTime(start_time= earliest_start, end_time= earliest_end)
        self.latest_times = MeetingTime(start_time= latest_start, end_time= latest_end)
        self.avg_times = MeetingTime(start_time= avg_start, end_time= avg_end)
        
        
        #for the garbage collector        
        earliest_start = None
        earliest_end = None
        
        latest_start = None
        latest_end = None
        
        avg_start = None
        avg_end = None
        
        
    def _earliest_time(self, attribute_method): #attribute method is either start time or end time
        earliest_time = 2399 #initialize
        for day in self.day_times_dict:
            time = self.day_times_dict[day] # MeetingTime object
            curr_time = attribute_method(time) # either start time or end time
            if  curr_time < earliest_time:
                earliest_time = curr_time
        return earliest_time
    
    def _latest_time(self, attribute_method):
        latest_time = 0 # initialize
        for day in self.day_times_dict:
            time = self.day_times_dict[day] # MeetingTime object
            curr_time = attribute_method(time) # either start time or end time
            if curr_time > latest_time:
                latest_time = curr_time
        return latest_time
    
    def _avg_time(self, attribute_method):
        no_days = len(self.day_times_dict) # no. days to divide total time into
        hrs = 0
        mins = 0
        for day in self.day_times_dict:
            time = self.day_times_dict[day]
            curr_time = attribute_method(time)
            hrs += curr_time // 100 # the total number of hours
            mins += curr_time % 100 # the total number of minutes
        
        hrs /= no_days # avg hours
        mins /= no_days # avg minutes
        
        hrs, mins = self._fix_round_hrs_and_mins(hrs, mins) # fix figures
        time = hrs * 100 + mins
        return time
    
    
    def _fix_round_hrs_and_mins(self, hrs, mins): 
        #fixes carry of hrs to mins, and rounds down
        #mins to nearest 5
        
        hrs_carry = hrs - math.floor(hrs) # decimal part of hours
        mins += hrs_carry * 60 # decimal part of hrs converted to minutes and added to mins
        hrs = math.floor(hrs) # whole number, not decimal
        hrs += mins // 60 # if mins now has a carry, add it to hrs
        mins = mins % 60 # after carry, remianing mins is mins
        mins = 5 * math.floor(mins/5) #rounds down to nearest multiple of 5: 0 5 10 15 20 25 etc
        return int(hrs), int(mins)
   
    #return ints
    def no_credits(self):
        return self.num_credits
    
    def priority_score(self):
        return self.priority_score
    
    def earliest_start(self):
        return self.earliest_times.start_time
        
    def earliest_end(self):
        return self.earliest_times.end_time
    
    def latest_start(self):
        return self.latest_times.start_time
    
    def latest_end(self):
        return self.latest_times.end_time
    
    def avg_start(self):
        return self.avg_times.start_time
    
    def avg_end(self):
        return self.avg_times.end_time
    
    def avg_duration(self):
        return self.avg_times.duration
    
    #iterator for strings of MeetingTimes days of week
    def iter_days_of_week_str(self):
        days_of_week = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
        for day in days_of_week:
            if day in self.day_times_dict:
                yield str(self.day_times_dict[day])
  
        
    #return string represenation of times
    def earliest_start_str(self):
        return self.earliest_times.start_time_str()
        
    def earliest_end_str(self):
        return self.earliest_times.end_time_str()
    
    def latest_start_str(self):
        return self.latest_times.start_time_str()
    
    def latest_end_str(self):
        return self.latest_times.end_time_str()
    
    def avg_start_str(self):
        return self.avg_times.start_time_str()
    
    def avg_end_str(self):
        return self.avg_times.end_time_str()
    
    def avg_duration_str(self):
        return self.avg_times.duration_str()