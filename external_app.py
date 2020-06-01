import requests
from datetime import datetime
from datetime import timedelta
from dateutil import relativedelta
import pandas as pd
import json

url = "http://127.0.0.1:8000/data/Employee/"


def update_salary(emp_id, new_salary):
    url = "http://127.0.0.1:8000/data/Employee/"+ str(emp_id) +"/"
    payload = {'salary': str(update_salary)}
    files = []
    headers= {}
    response = requests.request("PUT", url, headers=headers, data = payload, files = files)
    print(response.text.encode('utf8'))


payload = {}
headers= {}
data ={}
sum_Sal=0
response = requests.request("GET", url, headers=headers, data = payload)
emps = response.json()
print(emps)
for emp in emps:
    sum_Sal += emp['salary']
    print(str(sum_Sal))
average_salary = int(sum_Sal/len(emps))
print("average salary is ", average_salary)

emp_list=[]

for emp in emps:
    date_time_obj = datetime.strptime(emp['hire_date'], '%Y-%m-%d')
    diff = relativedelta.relativedelta(datetime.now(),date_time_obj)
    if diff.years > 1 and emp['salary'] < average_salary:
        emp_list.append(emp)
print(emp_list)

emp_df = pd.DataFrame(emp_list)
emp_df.to_csv('emp.csv',index=False)








