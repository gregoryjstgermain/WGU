"""
Given a main program that searches for the ID or the name of a student from a dictionary,
complete the find_ID() and the find_name() functions that return the corresponding information
of a student. Then, insert a try/except statement in main() to catch any exceptions thrown by
find_ID() or find_name(), and output the exception message. Each entry of the dictionary
contains the name (key) and the ID (value) of a student.

Function find_ID() takes two parameters, a student's name and a dictionary.
Function find_ID() returns the ID associated with the student's name if the name is in the
dictionary. Otherwise, the function throws a custom exception type, StudentInfoError,
with the message "Student ID not found for studentName", where studentName is the name of
the student.

Function find_name() takes two parameters, a student's ID and a dictionary.
Function find_name() returns the name associated with the student's ID if the ID is in the
dictionary. Otherwise, the function throws a custom exception type, StudentInfoError, with
the message "Student name not found for studentID", where studentID is the ID of the student.

The main program takes two inputs from a user: a user choice of finding the ID or the name
of a student (int), and the ID or the name of a student (string). If the user choice is 0,
find_ID() is invoked with the student's name as one of the arguments. If the user choice is 1,
find_name() is invoked with the student's ID as one of the arguments. The main program finally
outputs the result of the search or a message if an exception is caught.

Note: StudentInfoError is defined in the program as a custom exception type.
StudentInfoError has an attribute to store an exception message.

Ex: If the input of the program is:

0
Reagan

and the contents of dictionary are:

'Reagan' : 'rebradshaw835',
'Ryley' : 'rbarber894',
'Peyton' : 'pstott885',
'Tyrese' : 'tmayo945',
'Caius' : 'ccharlton329'

the output of the program is:

rebradshaw835

Ex: If the input of the program is:

0
Mcauley

the program outputs an exception message:

Student ID not found for Mcauley

Ex: If the input of the program is:

1
rebradshaw835

the output of the program is:

Reagan

Ex: If the input of the program is:

1
mpreston272

the program outputs an exception message:

Student name not found for mpreston272


"""