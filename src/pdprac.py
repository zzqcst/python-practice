import pandas as pd
import numpy as np
from datetime import date
off_test = pd.read_csv('ccf_offline_stage1_test_revised.csv')
off_test.columns = ['user_id','merchant_id','coupon_id','discount_rate','distance','date_received']
dataset3 = off_test
t2 = dataset3[['user_id','coupon_id','date_received']]
t2.date_received = t2.date_received.astype('str')
t2 = t2.groupby(['user_id','coupon_id'])['date_received'].agg(lambda x:':'.join(x)).reset_index()
t2['receive_number'] = t2.date_received.apply(lambda s:len(s.split(':')))
t2 = t2[t2.receive_number>1]
t2['max_date_received'] = t2.date_received.apply(lambda s:max([int(d) for d in s.split(':')]))
t2['min_date_received'] = t2.date_received.apply(lambda s:min([int(d) for d in s.split(':')]))
t2 = t2[['user_id','coupon_id','max_date_received','min_date_received']]
t3 = dataset3[['user_id','coupon_id','date_received']]
t3 = pd.merge(t3,t2,on=['user_id','coupon_id'],how='left')
print(t3)
t3['this_month_user_receive_same_coupon_lastone'] = t3.max_date_received - t3.date_received
t3['this_month_user_receive_same_coupon_firstone'] = t3.date_received - t3.min_date_received