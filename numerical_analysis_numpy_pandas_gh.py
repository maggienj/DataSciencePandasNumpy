# using pandas read_csv  instead of numpy.loadtxt 
import pandas as pd
import numpy as np
import os

# dtype="str" ,
# nrows=10000 ,
# First read into csv with pandas
# here we initialize a new dataframe using pandas
df = pd.read_csv("SFO_PD.csv" ,
                       keep_default_na = True,
                       na_filter = True ,
                       verbose = True ,
                       skiprows = 0,
                       usecols=(8,9),
                       dtype={'Year': int, 'TotalPayBenefits': float}
                   )


n_by_year_tpb= df.groupby(["Year"])["TotalPayBenefits"].sum().to_frame(name ='Total_TPB')
print(n_by_year_tpb)

tpb_2018 = n_by_year_tpb.query('Year==2018')['Total_TPB']
tpb_2015 = n_by_year_tpb.query('Year==2015')['Total_TPB']
print( tpb_2018)
print(tpb_2015)

np_2018 = tpb_2018.to_numpy()
np_2015 = tpb_2015.to_numpy()
print("np_2018 = " , np_2018)
print("np_2015 = " , np_2015)

diff_np_2018_2015 = np_2018 - np_2015
print ("diff = " , diff_np_2018_2015)

print (tpb_2018.shape)
print (tpb_2015.shape)

#diff_Val = tpb_2018[1,1]
# - tpb_2015[1:1]
#print("diff_Val = " ,diff_Val)

#diff_val = np.n_by_year_tpb[4,1] - np.n_by_year_tpb[1,1]

print (n_by_year_tpb.shape)

#print( diff_val)
