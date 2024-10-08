import pandas as pd 
import numpy as np 

# df = pd.read_csv("horoscope.csv")
# df = df.drop(['date_range','current_date','description','compatibility','mood','color','lucky_number','lucky_time'],axis=1)
# df.to_csv('fit_data.csv',index=False)

# df1 = pd.read_csv("employee_data.csv")
# df1 = df1.drop(['EmpID', 'FirstName', 'LastName', 'StartDate', 'ExitDate', 'Title', 'Supervisor', 'ADEmail', 'BusinessUnit', 'EmployeeStatus', 'EmployeeType', 'PayZone', 'EmployeeClassificationType', 'TerminationType', 'TerminationDescription', 'DepartmentType', 'Division', 'State', 'JobFunctionDescription', 'GenderCode', 'LocationCode', 'RaceDesc', 'MaritalDesc', 'Performance Score', 'Current Employee Rating'],axis=1)
# df1.to_csv('fit2.csv',index=False)
# df1_reduce = df1.sample(n=768,random_state=42)
# df1_reduce.to_csv('fit2_data.csv',index=False)


# df2=pd.read_csv("fit4_data.csv")
# df2_reduce = df2.sample(n=768,random_state=42)
# df2_reduce.to_csv("fi_data.csv",index=False)

# df3 = pd.read_csv("top.csv")
# df3=df3.drop(['Zone', 'State', 'City', 'Type', 'Establishment Year', 'time needed to visit in hrs', 'Google review rating', 'Entrance Fee in INR', 'Airport with 50km Radius', 'Weekly Off', 'Significance', 'DSLR Allowed', 'Number of google review in lakhs', 'Best Time to visit'],axis=1)
# df3.to_csv('fit4_data.csv',index=False)

df1=pd.read_csv("fit_data.csv")
df2=pd.read_csv("fit2_data.csv")
df3=pd.read_csv("fit3_data.csv")
df4=pd.read_csv("fi_data.csv")

main_data = pd.concat([df1,df2,df3,df4],axis=1,ignore_index=True)
main_data.to_csv('main_data.csv',index=False)



