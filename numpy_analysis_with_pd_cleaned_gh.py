# using pandas read_csv  instead of nupy.loadtxt 
import pandas as pd
import numpy as np


# here we initialize a new dataframe using pandas
df = pd.read_csv("SFO_PD.csv" ,
                       keep_default_na = True,
                       na_filter = True ,
                       verbose = False ,
                       skiprows = 0,
                       usecols=(8,9),
                       dtype={'Year': int, 'TotalPayBenefits': float}
                   )


n_by_year_tpb= df.groupby(["Year"])["TotalPayBenefits"].sum().to_frame(name ='Total_TPB')
print(n_by_year_tpb)

tpb_2018 = n_by_year_tpb.query('Year==2018')['Total_TPB']
tpb_2015 = n_by_year_tpb.query('Year==2015')['Total_TPB']


np_2018 = tpb_2018.to_numpy()
np_2015 = tpb_2015.to_numpy()


diff_np_2018_2015 = np_2018 - np_2015
print ("The cost increase from 2015 to 2018 is " , diff_np_2018_2015)


