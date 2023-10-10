
# working  on  time spamp
# import  datetime
# print(datetime.datetime.now())
# 2023-09-23 10:01:18.863411 we  need with no  dashed
from  datetime import datetime
unformated_date= datetime.now()
formarted_date=unformated_date.strftime('%Y%m%d%H%M%S')
print("Formated",formarted_date)#'%H:%M %d/%m/%Y'

