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
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
#--> add your Python code here
db = []
X = []
Y = []
days = 0

with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
string_to_int_mapping = {
        'Sunny': 0,
        'Rain': 1,
        'Overcast': 2,
        'Hot': 0,
        'Mild': 1,
        'Cool': 2,
        'Normal': 0,
        'High': 1,
        'No': 0,
        'Yes': 1,
        'Weak': 0,
        'Strong': 1
}
for row in db:
   X.append([string_to_int_mapping[row[1]], string_to_int_mapping[row[2]], string_to_int_mapping[row[3]],string_to_int_mapping[row[4]]])
   days = days + 1
   #print(f"X Data: {X}")

# X =

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
for row in db:
   Y.append(string_to_int_mapping[row[5]])

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
db_test = []
test_data = []
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db_test.append (row)

for row in db_test:
   test_data.append([string_to_int_mapping[row[1]], string_to_int_mapping[row[2]], string_to_int_mapping[row[3]],string_to_int_mapping[row[4]]])

for test in test_data:
    # Use your test samples to make probabilistic predictions
    # Get the probabilities for each class for the current test instance
    probabilities = clf.predict_proba([test])[0]
    print(f"Prob: {probabilities}")

    # Get the predicted class (0 or 1)
    predicted_class = clf.predict([test])[0]
    print(f"Predicted class: {predicted_class}")

#printing the header of the solution
#--> add your Python code here
print("Day\tOutlook\tTemperature\tHumidity\tWind\tPlayTennis\tConfidence")

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
for i, test_instance in enumerate(test_data):
    # Use your test samples to make probabilistic predictions
    # Get the probabilities for each class for the current test instance
    probabilities = clf.predict_proba([test_instance])[0]

    # Get the predicted class (0 or 1)
    predicted_class = clf.predict([test_instance])[0]

    # Check if the maximum probability is greater than or equal to 0.75
    if max(probabilities) >= 0.75:
        confidence = max(probabilities)
        days = days + 1
        print(f"{days}\t{db_test[i][1]}\t{db_test[i][2]}\t{db_test[i][3]}\t{db_test[i][4]}\t{predicted_class}\t{confidence}")
    else:
        days = days + 1
        confidence = -1  # Indicates low confidence
