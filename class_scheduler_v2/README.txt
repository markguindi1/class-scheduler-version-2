READ ME

DOCUMENTATION FOR class_scheduler_v2

----------------------------------------------------------------------

The file from which the courses information comes from should be a raw text file (".txt"), such as this file.

The course file must be created exactly as instructed. The program is not yet ready to handle errors.

The course file should be created as follows:


1) Begin the entry of the first course with the word "Course" (this word, as well as everything else in your file, should NOT be in quotation marks).
Then, on the same line, type the course name. This can be many words; they do not have to be connected. Best practice is to type the name in CAPS.

2) On the next line, type the word "Credits", followed by the number of credits (for courses following the NYU Tandon SoE course naming conventions, this 
is unnecessary, as the number of credits is derived from the course name. To override the number of credits found in the course name, use this "Credits" 
field to enter the number of credits as above. So the "Credits" field must be entered for courses in schools other than NYU Tandon SoE).

Steps 3-5 ("Coreq", "Exclude", and "Priority") are optional. They can be entered in any order, and they can be partially included 
(meaning, you can enter only one field or two fields if you like).

3) On the next line, type the word "Coreq" or "Coreqs", followed by any corequisite courses names. Each coreq name should be separated by a comma.

4) On the next line, type the word "Exclude", followed any excluded courses (courses that you do not want to take together with this course; 
they should be "excluded" from the schedule). Again, each course name should be separated by a comma.


5) On the next line, type the word "Priority", followed by the priority score of the course. 
If you would like to sort the schedules by preferred classes, you can give the course a priority score. 
The lower the number, the higher the priority. For the classes you would prefer the most, type 0. For the next-most desirable classes, type 1, and so on.
Courses without a priority score are given a default priority score of 3. 

Again, the "Coreq", "Exclude", and "Priority" fields are completely optional, and can be completely or partially skipped if preferred.

6) On the next line, indent the line and type the word "Section", indication the first section of the current course.
On the next line, indent the line and type the first meeting time of the section that week. Type the day of the week in exactly the following format:
Mon Tues Wed Thurs Fri
Then type the start and end times of the meeting time as two simple numbers in 24-hour format, separated by nothing. 
Ex: for Monday, 11:00 am to 1:00 pm, type the following: Mon 1100 1300
If the same meeting time occurs on multiple days of the week, you can just type all days before the start & end times. Ex: Tues Thurs 1100 1300
Repeat these steps for each meeting time of the section.

Repeat the "Section" steps for each section of the course.

Repeat all of the above steps for each course.

The extra empty lines, as well as the indentations of the sections, are just added for clarity and readability, but they are not strictly necessary.
The key words, such as Course, Priority, Coreq, Coreqs, Exclude, and Section, can be in any letter case, capitalized, all caps, or all lowercase.
They do not have to be consistently cased throughout the file. In the example, they are just added for clarity and readability.
HOWEVER, THE COURSE NAMES AND SECTION NUMBERS MUST BE CONSISTENTLY NAMED AND CASED.

An example of all of the above:


Course CS 2124 LEC
Credits 4
Priority 0
Coreq CS 2124 LAB

	Section ALEC
	Mon Wed 1030 1200

	Section BLEC
	Mon Wed 1200 1330

	Section CLEC
	Mon Wed 1500 1630


Course MG 2004
Priority 3
Exclude MG 2104, MG 2304

	Section A
	Mon Wed 1030 1230

Course MG 2104
Priority 2
Exclude MG 2004, MG 2304

	Section A
	Tues Thurs 1600 1800


Course BMS-A 1004 LAB
Credits 4
Priority 0
Coreq BMS-A 1004 LEC
Exclude PH 2033, PH 2131, BMS-B 1004 LEC, BMS-B 1004 LAB

	Section 1
	Mon 800 1100

	Section 2
	Fri 1100 1400

	Section 3
	Wed 800 1100



The extra empty lines, as well as the indentations of the sections, are just added for clarity and readability, but they are not strictly necessary.
The key words, such as Course, Priority, Coreq, Coreqs, Exclude, and Section, can be in any letter case, capitalized, all caps, or all lowercase.
They do not have to be consistently cased throughout the file. In the example, they are just added for clarity and readability.
However, the course names and section numbers MUST BE CONSISTENTLY NAMED AND CASED.

----------------------------------------------------------------------

If using the user input main function, everything must be entered exactly as it was entered in the file, as per the instructions.

If using the non-user-input main function, everything must also be entered exactly as specified.


















