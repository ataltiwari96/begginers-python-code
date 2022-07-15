while(True):
  dd=int(input("\nEnter date in DD:"))
  if(dd in range(1,32)):
    pass
  else:
    print("\nEnter a valid day!!!")
    continue
  mm=int(input("Enter month in MM:"))
  if(mm in range(1,13)):
   pass
  else:
   print("\nInvalid Month!!!")
   continue
  yy=int(input("Enter year in YYYY:"))
  if(yy in range(1,2023)):
    break
  else:
    print("\nInvalid Year!!!")
    continue
    
month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
leapmonth={2:29}
birth=0
yyy=yy%100
if(yy%4==0):
  month.update(leapmonth)
t=month[mm]+1
if(dd in range(1,t)):
  
  if((yy%4!=0) and (mm==2 and dd==29)):
   print("Invalid Date!!! Please Enter a valid date")
  elif(yy%4==0 and mm==2 and dd==29):
   print("------------------------")
   print ("|Year\t\t |Day\t\t")
   

   for i in range(yy,2023,4):
    yyy=i%100
    y=int(yyy)//4
    y+=int(yyy)
    if(yy==2020):
        birth+=1
    else:
        birth+=4
    m={ 1:0, 2:3,3:3, 4:6, 5:1, 6:4, 7:6, 8:2, 9:5, 10:0, 11:3, 12:5}
    y+=m[mm]
    y+=dd
    if(i>=2000):
     y=y-2
     d=y%7
     day={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    
     if (d==0):
      print("|",i,"\t\t |",day[d],"<===")
     else:
      print("|",i,"\t\t |",day[d],"\t")
    else:
     d=y%7
     day={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
     if (d==0):
      print("|",i,"\t\t |",day[d],"<===")
     else:
      print("|",i,"\t\t |",day[d]," \t")
   print("------------------------")
   print("Current age of person as of 2022 is ",birth-1)
  else:
   print("------------------------")
   print ("|Year\t\t |Day\t\t")
   for i in range(yy,2023,1):
    yyy=i%100
    y=int(yyy)//4
    y+=int(yyy)
    birth+=1
    m={ 1:0, 2:3,3:3, 4:6, 5:1, 6:4, 7:6, 8:2, 9:5, 10:0, 11:3, 12:5}
    y+=m[mm]
    y+=dd
    if(i>=2000):
     y=y-1
     d=y%7
     day={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    
     if (d==0):
      print("|",i,"\t\t |",day[d],"<===")
     else:
      print("|",i,"\t\t |",day[d],"\t")
    else:
     d=y%7
     day={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
     if (d==0):
      print("|",i,"\t\t |",day[d],"<===")
     else:
      print("|",i,"\t\t |",day[d]," \t")
   print("------------------------")
   print("Current age of person as of 2022 is ",birth-1)

else:
 print("\n\nInvalid Date")
