
import numpy as np
import pandas as pd

def ConvertString(cell):
    try :
        return  str(cell)
    except:
        return 'NA'
def ConvertFloat(cell):
    try:
        return float(cell)
    except:
        return 0.0

# data read without converters, set low memory otherwise interpreter complains
#  df  = pd. read_csv('datasets/Salaries.csv', low_memory=False)


#using converter option to change columns to proper type:
df  = pd. read_csv('datasets/Salaries.csv', 

converters={
    'Id' :  ConvertString,
    'Year' :  ConvertString,
    'EmployeeName' :  ConvertString,
    'JobTitle' :  ConvertString,
    'Benefits' :  ConvertString,
    'Status' :  ConvertString,
    'Notes' :  ConvertString,
    'Agency' :  ConvertString,
    'BasePay' :  ConvertFloat,
    'OvertimePay' :  ConvertFloat,
    'OtherPay' :  ConvertFloat,
    'TotalPay' :  ConvertFloat,
    'TotalPayBenefitsPay' :  ConvertFloat
    
    

})
#1-2
print("\n\nLooking at initial data:\n")
print(df.head())   
print(df.info)

#3
print("\nPrinting average values of Base Pay for first 10000:")
print(f'Average: {(df["BasePay"][0:10000].mean())}')

#4
print("\nPrinting max value of Total Pay Benefits for first 10000:")
print(f'Max TPB: {df["TotalPayBenefits"].max()}')

#5-6

print("\n\nPrinting JOSEPH DRISCOLL's job title:")
jd = df.loc[ df['EmployeeName'] == "JOSEPH DRISCOLL" ]
print(f''' JD's job title:  {jd["JobTitle"].values} \n JD's Total Pay Benefits: {jd.TotalPayBenefits.values}''')

#7-8
print("\n\nPrinting Details on highest paid person:")
baller = df.loc[ df['TotalPay']==df['TotalPay'].max() ]
print(f''' Baller Name:  {baller["EmployeeName"].values} \nBaller Pay: {baller["TotalPay"].values}\n Baller Benefits: {baller["TotalPayBenefits"].values}   ''')
print("\n\nPrinting Details on lowest paid person:")
notballer = df.loc[ df['TotalPay']==df['TotalPay'].min() ]
print(f''' Baller Name:  {notballer["EmployeeName"].values} \nBaller Pay: {notballer["TotalPay"].values}\n Baller Benefits: {notballer["TotalPayBenefits"].values}   ''')

print("The lowest paid person seems to have a really low pay! They're basically paying to work! We should go over records and fix this mistake.")

#9
print("\n\nAverage Total Pay by years: ")
print(df.groupby('Year').mean()["TotalPay"])



#10
print("\n\nUnique Job Title Count: ")
print(len(pd.unique(df.JobTitle)))


#11
print("\n\nGetting top 7 popular jobs")
print(df.JobTitle.value_counts().nlargest(7))


#12
print("\n\nGet jobs held by one person in 2013:")
print (  sum(filter ( lambda u: u==1 ,df.loc[df['Year']=='2013']['JobTitle'].value_counts().tolist())))




#13
print("Get count of people with  'Chief' in their names" )
print(df.JobTitle.str.count("Chief").sum())

 #14
print("Correlation Length of (Job Title) v Base Pay")
lengthOfJobTitle = df.JobTitle.str.len()
print(lengthOfJobTitle.corr(df.BasePay))
