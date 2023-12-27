#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)



#loop your data to allow each instance to be your test set
total = 0
wrong = 0
for data in db:
    X = []
    Y = []

    for row in db:
        if(int(row[0]) != int(data[0])):
            X.append([int(row[0]), int(row[1])])
        elif (int(row[1]) != int(data[1])):
            X.append([int(row[0]), int(row[1])])

    string_to_int_mapping = {
        '-': 0,
        '+': 1,
    }
    for row in db:
        if(int(row[0]) != int(data[0])):
            Y.append(int(string_to_int_mapping[row[2]]))
        elif (int(row[1]) != int(data[1])):
            Y.append(int(string_to_int_mapping[row[2]]))


    testSample = [int(data[0]), int(data[1])]

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

 
    class_predicted = clf.predict([testSample])[0]
    total = total + 1


    result = string_to_int_mapping[(data[2])]

    print(f"class_predict: {class_predicted} and result = {result}")
    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if(class_predicted != result):
       wrong = wrong + 1


#print the error rate
#--> add your Python code here
proportion = wrong / total

print(f"The error rate = {proportion:.2f}")