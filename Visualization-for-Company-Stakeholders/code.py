# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Reading the file
data=pd.read_csv(path)
#Code starts here
# Step 1 
#Reading the file
#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts().plot(kind='bar')
plt.show()
#Plotting bar plot
# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack().plot(kind='bar', stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()
#Changing the x-axis label 
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack().plot(kind='bar', stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()
#Changing the y-axis label
graduate=data[data['Education'] == 'Graduate'].plot(kind='density' ,label='Graduate')
not_graduate = data[data['Education'] == 'Not Graduate'].plot(kind='density' ,label='Not Graduate')
#Rotating the ticks of X-axis
#Plotting a stacked bar plot
fig,(ax_1, ax_2, ax_3) = plt.subplots(nrows= 3 , ncols=1)
ax_1.scatter('ApplicantIncome', 'LoanAmount')
ax_1.set_title('Applicant Income')
ax_2.scatter('CoapplicantIncome', 'LoanAmount')
ax_2.set_title('Coapplicant Income')
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.scatter('TotalIncome', 'LoanAmount')
ax_3.set_title('Total Income')


