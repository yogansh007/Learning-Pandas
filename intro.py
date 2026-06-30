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

cs=pd.read_csv('data.csv')
print(cs)

pd.options.display.max_rows=999
print(cs)
print(pd.options.display.max_rows)


# importing json

json_data=pd.read_json('data.json')
print(json_data)

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
another_json=pd.DataFrame(python_dict)
print(another_json)