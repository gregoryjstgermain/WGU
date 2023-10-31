"""
Write a program that reads the student information from a tab separated values (tsv) file.
The program then creates a text file that records the course grades of the students.
Each row of the tsv file contains the Last Name, First Name, Midterm1 score, Midterm2 score,
and the Final score of a student. A sample of the student information is provided in StudentInfo.tsv.
Assume the number of students is at least 1 and at most 20. Assume also the last names and first names
do not contain whitespaces.

The program performs the following tasks:

    Read the file name of the tsv file from the user.
    Open the tsv file and read the student information.
    Compute the average exam score of each student.
    Assign a letter grade to each student based on the average exam score in the following scale:
        A: 90 =< x
        B: 80 =< x < 90
        C: 70 =< x < 80
        D: 60 =< x < 70
        F: x < 60
    Compute the average of each exam.
    Output the last names, first names, exam scores, and letter grades of the students into a text file
    named report.txt. Output one student per row and separate the values with a tab character.
    Output the average of each exam, with two digits after the decimal point, at the end of report.txt.
    Hint: Use the format specification to set the precision of the output.

Ex: If the input of the program is:

StudentInfo.tsv

and the contents of StudentInfo.tsv are:

Barrett    Edan    70  45  59
Bradshaw    Reagan  96  97  88
Charlton    Caius   73  94  80
Mayo    Tyrese  88  61  36
Stern    Brenda  90  86  45

the file report.txt should contain:

Barrett    Edan    70  45  59  F
Bradshaw    Reagan  96  97  88  A
Charlton    Caius   73  94  80  B
Mayo    Tyrese  88  61  36  D
Stern    Brenda  90  86  45  C

Averages: midterm1 83.40, midterm2 76.60, final 61.60


"""

# TODO: Declare any necessary variables.
# TODO: Read a file name from the user and read the tsv file.
# TODO: Compute student grades and exam averages, then output results to a text file.

file = input() #user file input
grade_map = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
exams = {'midterm1': [], 'midterm2': [], 'final': []}


with open(file, 'r') as f, open('report.txt', 'w') as OUT: #open file
    #data = f.readlines()
    for row in f:
        ln, fn, *scores = row.strip().split('\t')
        scores = list(map(int, scores))
        exams['midterm1'] += [scores[0]]
        exams['midterm2'] += [scores[1]]
        exams['final'] += [scores[2]]
        average = sum(scores) / len(scores)
        for letter in grade_map:
            if grade_map[letter] <= average:
                break
        row = '\t'.join((ln, fn, *map(str, scores), letter))
        print(row, file=OUT)

    print('', file=OUT)

    average1 = sum(exams['midterm1']) / len(exams['midterm1'])
    average2 = sum(exams['midterm2']) / len(exams['midterm2'])
    average_f = sum(exams['final']) / len(exams['final'])

    print(f'Averages: midterm1 {average1:.2f}, midterm2 {average2:.2f}, final {average_f:.2f}', file=OUT)



