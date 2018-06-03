# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 00:34:46 2017

Arrow testing out

@author: Mark
"""

import arrow

end_time = arrow.get("1230", "HHmm")
start_time = arrow.get("10:30", "HH:mm")
time_span = end_time - start_time
x = str(time_span)
print(x)


#end_datetime = datetime.datetime