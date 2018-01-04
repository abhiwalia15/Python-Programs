ordinal_nums=[1,2,3,4,5,6,7,8,9]
print("the ordinary numbers are")
for ordinal_num in ordinal_nums:
 if ordinal_num==1:
  print(str(ordinal_num)+'st')
 elif ordinal_num==2:
  print(str(ordinal_num)+'nd')
 elif ordinal_num==3:
  print(str(ordinal_num)+'rd')
 elif ordinal_num>=4 and ordinal_num<=9:
  print(str(ordinal_num)+"th")
  
