import csv
import math

#opening and reading the file
with open("class 105/data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

#removing 1 list form data
data=file_data[0]
#print(data)

#Calculating mean
total_data=0
data_len=len(data)

for i in data:
    total_data+=int(i)

mean=total_data/data_len
#print(mean)
#taking the sqare of indivusal value -mean
sq_list=[]

for x in data:
    minus=int(x)-mean
    minus=minus**2
    sq_list.append(minus)

#print(sq_list)
#Suming the suared list
sum=0
for y in sq_list:
    sum+=y

#print(sum)
#Dividing the number by number of values-1
result=sum/(data_len-1)

#print(result)
#squareroot to get the standart deviation
std_dev=math.sqrt(result)
print(std_dev)