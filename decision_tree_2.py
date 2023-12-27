#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

num = 0
for ds in dataSets:
    num = num + 1
    total = 0
    correct = 0
    average = 0.0

    dbTraining = []
    X = []
    Y = []

    print ("---------------------------------------------------------------")
    print (f"Using Data Set {num}")
    print ("---------------------------------------------------------------")

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    #transform the original categorical training features into numbers and add to the 4D array X.
    string_to_int_mapping = {
        'Young': 0,
        'Presbyopic': 1,
        'Prepresbyopic': 2,
        'Myope': 0,
        'Hypermetrope': 1,
        'No': 0,
        'Yes': 1,
        'Reduced': 0,
        'Normal': 1
    }

    for row in dbTraining:
     X.append([string_to_int_mapping[row[0]], string_to_int_mapping[row[1]], string_to_int_mapping[row[2]],string_to_int_mapping[row[3]]])

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    for row in dbTraining:
     Y.append([string_to_int_mapping[row[4]]])

    #loop your training and test tasks 10 times here
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       # dbTest =
       db = []
       dbTest = []
       with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                    db.append (row)
                    #print(row)

            for row in db:
                dbTest.append([string_to_int_mapping[row[0]], string_to_int_mapping[row[1]], string_to_int_mapping[row[2]],string_to_int_mapping[row[3]], string_to_int_mapping[row[4]]])

       for data in dbTest:
           # Transform the features of the test instance to numbers using the same mapping as in training
            test_instance = [data[0], data[1], data[2], data[3]]

            # Use the decision tree to make a class prediction
            predicted_class = clf.predict([test_instance])[0]

            # Compare the prediction with the true label (data[4]) of the test instance
            true_label = data[4]

            #print(f"Predicted class: {predicted_class}, True label: {true_label}")
            total = total + 1
            if (predicted_class == true_label):
                correct = correct + 1

    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
    average = correct / total
    average = average * 100
    print(f"The average of correct results is {average}%")

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here




