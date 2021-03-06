#Project Name: Course Grader
#Author: Mitesh Madaan
#Description: This project inputs data from a input file(csv format) having marks of students and assigns a grade to each of them.
#The final details with assigned grade is written in a output file in csv format.
#                                         *****************************START******************************
#imporitng necessary module for working with csv file
import csv
# loc variable stores address of input and output data file
input_file = r"G:\BITS\LECTURES\SEM 1-1\CP\CP Lab\CSF111_181_Practical_Marks.csv"
output_file = r"C:\Users\HP\.PyCharmCE2018.3\config\scratches\tut files\projects\course grader\CP grades.csv"
#declaring a data set to store all student's raw information from input file to be written in output file
data = []
#grader function that assigns a grade to each of the student's marks
def grader(mark):
    if mark == 33:
        grade = 'A'
    elif mark == 22:
        grade = 'B'
    elif mark == 11:
        grade = 'C'
    else:
        grade = 'NC'
    #returing grade assigned back to main driver function
    return grade
#extracting student's details from input file into a data set
with open(input_file,'r') as csvfile:
    #declaring a reader pointer to operate upon input file
    csvreader = csv.reader(csvfile)#assinging input file(csv) to reader pointer
    #looping through rows containing student's details(one per each row)
    for row in csvreader:
        data.append(row)#adding data to data set at one row(student) each time
#declaring a file pointer to output file to operate upon it.
Fw = open(output_file,'w')
#writing the header line in output file at first
Fw.write('Name'+','+'ID'+','+'Total'+','+'Grade'+'\n')
#loop for writing student's results in output file
for x in range(530):
    temp = data[x]# getting a particular student's details from complete set of data and storing into temporary set
    Fw.write(temp[0] + ',' + temp[1]+ ',' + temp[15]+ ',' + grader(int(temp[15]))+'\n')#writing the details and grade obtained in output file
#all students's details have been written, closing the output file pointer
Fw.close()
#                                         *****************************END******************************


