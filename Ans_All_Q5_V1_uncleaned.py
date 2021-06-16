# using pandas read_csv  instead of numpy.loadtxt 
import pandas as pd
import numpy as np
import os


df = pd.read_csv("C:/windows/datasets/SFO_PD.csv" ,
                       keep_default_na = True,
                       na_filter = True ,
                       verbose = False ,
                       skiprows = 0,
                       usecols=(0,1,2,4,8,9),
                       # nrows=100 ,
                       dtype={'Id':int,'EmployeeName':str,'JobTitle':str, 'Year': int, 'TotalPayBenefits': float , 'OvertimePay': float}
                   )


n_by_year_tpb= df.groupby(["Year"])["TotalPayBenefits"].sum().to_frame(name ='Total_TPB')
print(n_by_year_tpb)

tpb_2018 = n_by_year_tpb.query('Year==2018')['Total_TPB']
tpb_2015 = n_by_year_tpb.query('Year==2015')['Total_TPB']


np_2018 = tpb_2018.to_numpy()
np_2015 = tpb_2015.to_numpy()


diff_np_2018_2015 = np_2018 - np_2015

print ("----- ----- ------ ")
print ("----- ----- ------ ")
print ("----- ----- ------ ")
print ("Q1 --- The cost increase from 2015 to 2018 is " , diff_np_2018_2015)
print ("----- ----- ------ ")
print ("----- ----- ------ ")
print ("----- ----- ------ ")

#Q2 -- no recs for 2014 
n_mean_by_year_tpb= df.groupby(["JobTitle"])["TotalPayBenefits"].mean().to_frame(name ='mean_TPB')
#print(n_mean_by_year_tpb)
print ("Q2 --- No recs for 2014 ... so, using 2015 for sampling data " )
tpb_2014 = df.query('Year==2015')

np_2014 = tpb_2014.to_numpy()
tpb_2014.shape
#print ( np_2014 )

# df.pivot_table(index='year',columns='JobTitle',values='TotalPayBenefits',aggfunc='mean',sort)
tpb_2014 = df.groupby(['JobTitle']).agg({'TotalPayBenefits':['mean','max']})
tpb_2014.columns = ['max', 'mean_max'] # change column names

tpb_2014_sorted = tpb_2014.sort_values(by='mean_max',ascending=False).head(1)

print ("Q2 = " , tpb_2014_sorted )
print ("Q2 --- there are no recs for 2014 , so using 2015 data for sampling.")
print ("----- ----- ------ ")
print ("----- ----- ------ ")
print ("----- ----- ------ ")


#Q3 --- For 2018, how much could have been saved in 2018 by stopping OverTimePay
df_2018 = df.query('Year==2018')
n_by_year_otp= df_2018.groupby(["Year"])["OvertimePay"].sum().to_frame(name ='Total_OTP')

print ("----- ----- ------ ")
print("Q3 ---the following amount could have been saved in 2018 if there weren't any otp for 2018 ")
print (n_by_year_otp)

print ("----- ----- ------ ")
print ("----- ----- ------ ")
print ("----- ----- ------ ")

#Q4 -- Top5 JobTitle -- And How much do they cost SFO
df_2018_otp = df.query('Year==2015') 
#print (df_2018.info() )
print ("----- ----- ------ ")
df2= df_2018_otp.groupby("JobTitle")["TotalPayBenefits"].sum().astype(int).reset_index()
#print ("df2", df2.head(5))

jt_value_counts = df_2018_otp['JobTitle'].value_counts()
# converting to df and assigning new names to the columns
df_jt_value_counts = pd.DataFrame(jt_value_counts)
df_jt_value_counts = df_jt_value_counts.reset_index()
df_jt_value_counts.columns = ['JobTitle', 'counts'] # change column names
#print ( "df_jt_value_counts", df_jt_value_counts.head(5))

merged_cnt_sum = pd.merge(df_jt_value_counts,df2, on="JobTitle")

#top5
print ("----- ----- ------ ")
print ("Q4-- Top5 normal JobTitle and their cost for SFO --" )
merged_cnt_sum_top5 = merged_cnt_sum.head(5)
print ("Q4----" )
print ("" , merged_cnt_sum_top5 )

print ("----- ----- ------ ")
print ("----- ----- ------ ")
print ("----- ----- ------ ")


#Q5 --- Top Employee -- Earning ---  across all years ---
print ("----- ----- ------ ")
print ("Q5-- Highly paid EmployeeName by Year --" )
df_high_sal = df[['Year','EmployeeName','TotalPayBenefits']]
df_high_sal_proc = df.groupby('Year').apply(lambda x: x[x['TotalPayBenefits'] == x['TotalPayBenefits'].max()])
df_high_sal_proc_2 = df_high_sal_proc[["Year",'EmployeeName','TotalPayBenefits']]
#df_high_sal_proc_2.info()
print ( "", df_high_sal_proc_2)
print ("----- ----- ------ ")

print ("----- ----- ------ ")
print ("----- ----- ------ ")
print ("----- ----- ------ ")
#Q5 -- 2
#tpb_high_sal = df.groupby(['Year'])["EmployeeName"].agg({'TotalPayBenefits':['max']})
#tpb_high_sal.columns = ['max', 'highsal_max'] # change column names

# tpb_high_sal_sorted = tpb_high_sal.sort_values(by='highsal_max',ascending=False).head(1)
# tpb_high_sal = df.groupby(["Year", "TotalPayBenefits"]).agg("max").filter(["Year", "TotalPayBenefits", "EmployeeName"])

# print("q3 ", tpb_high_sal.head())

#print (tpb_high_sal_sorted)






