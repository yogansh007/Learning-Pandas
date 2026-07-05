import pandas as pd

data={
    'mobile': ["apple","oppo","vivo"],
    'price': [50000,27000,20000]

}

pd_data=pd.DataFrame(data,index=['a','b','c'])
print(pd_data)


li=['a','b','c']
series=pd.Series(li,index=[1,2,3])
print(series)

dict={'a':110,'b':120,'c':130}
series_from_dict=pd.Series(dict,index=['a','b'])
print(series_from_dict)



print(pd_data.loc[['a','b']])



pd.options.display.max_rows=999

print(pd.options.display.max_rows)


# importing json



python_dict= {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5
  }
}

# json format and python dict are same so read can 
# be done from both json file and python dict


#tail ==> prints last 5 rows by defualt if no is not given




csv=pd.read_csv('data.csv')
print(csv)



#new_csv=csv.dropna()
#print(new_csv)


#by default the dropna method will return new dataframe 
# to get original dataframe changed use inplace= true

#csv.dropna(inplace=True)
#print(csv)


# fill required data in empty cells instead of deleting full rows

#csv.fillna({
   # "Calories":69,
    #"Pulse":69,
    #"Maxpulse":69,
    #"Duration":69,
#},inplace=True)
#print(csv)

# calculating mean and putting value on required column
#x=csv["Calories"].mean()
#csv.fillna({"Calories":x},inplace=True)
#print(csv)
#print(x)


csv["Date"]=pd.to_datetime(csv['Date'],format='mixed')
#print(csv)


#csv.dropna(subset=['Date'],inplace=True)
#print(csv)

#csv.loc[7,'Duration']=45
#print(csv)

# loop through csv and repalce wrong data out of range

#for x in csv.index:
   # if csv.loc[x,"Duration"]>120:
      #  csv.loc[x,"Duration"]=120

#for x in csv.index:
 #   if csv.loc[x,"Duration"]>120:
  #      csv.drop(x,inplace=True)

#print(csv)


# look dor dublicate rows

#print(csv.duplicated())
#csv.drop_duplicates(inplace=True)
#print(csv)


#finding correlation between rows





print(csv.corr())