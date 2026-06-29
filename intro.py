import pandas as pd

data={
    'mobile': ["apple","oppo","vivo"],
    'price': [50000,27000,20000]

}

pd_data=pd.DataFrame(data)
print(pd_data)


li=['a','b','c']
series=pd.Series(li,index=[1,2,3])
print(series)

dict={'a':110,'b':120,'c':130}
series_from_dict=pd.Series(dict,index=['a','b'])
print(series_from_dict)