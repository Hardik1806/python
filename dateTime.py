from datetime import date,datetime #importing the datetime module
d1=input("please eneter the date")#taking input of the initial date
da1=datetime.strptime(d1,"%d%m%Y")#formatting the date
print("the date you entered is : ",da1.strftime("%d-%m-%Y"))
print("only the day part: ",da1.strftime("%d"))#printing only the date part
a=da1.strftime("%d")#day part of date 1
c=da1.strftime("%m")#month of date 1
w1=da1.strftime("%W")#findind week of date 1
print("week no. of date 1 is:",w1)
d2=input("please enter the upcoming date")#taking input of the upcoming date
da2=datetime.strptime(d2,"%d%m%Y")#formatting rhe date
print("the upcoming date you entered is: ",da2.strftime("%d-%m-%Y"))
print("only the day part: ",da2.strftime("%d"))#printng only the date part
b=da2.strftime("%d")#day part of date 2
d=da2.strftime("%m")#month of date 2
w2=da2.strftime("%W")#finding week of date 2
print("week no. of date 2 is: ",w2)
def calcmonth(e):
    month=""
    match e:
        case "01" :
            month="january"
        case "02" :
            month="february"
        case "03" :
            month="march"
        case "04" :
            month="april"
        case "05" :
            month="may"   
        case "06" :
            month="june"
        case "07" :
            month="july"
        case "08" :
            month="august"
        case "09" :
            month="september"
        case "10" :
            month="october"
        case "11" :
            month="november"
        case "12" :
            month="december"
    return month
if (da1>da2): #finding the difference b/w the dates 
    difference=da1-da2
else:
    difference=da2-da1

month1=calcmonth(c)#storing name of month1
month2=calcmonth(d)#storing name of month2
year1=da1.strftime("%Y")# getting the year part of date 1
year2=da2.strftime("%Y")#getting the year part of date 2
y1=""
y2=""
if int(year1)%4==0 and int(year1)%100!=0: # checking for leap year
    y1="year 1 is leap year"
elif int(year1)%100==0 and int(year1)%4==0:
    y1="year 1 is leap year"
else:
    y1="year 1 is not a leap year"
if int(year2)%4==0 and int(year2)%100!=0:
    y2="year 2 is leap year"
elif int(year2)%100==0 and int(year2)%4==0:
    y2="year 2 is leap year"
else:
    y2="year 2 is not a leap year"
print("month of date 1 is: ",month1)
print("month of date 2 is: ",month2)
print("todays date is",date.today())
print("difference b/w the dates in days is",difference.days)
print("difference b/w dates in terms of hours is",difference.days*24)
print("difference b/w the date in terms of minutes is",difference.days*24*60)
print(y1)
print(y2)
