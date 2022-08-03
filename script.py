import codecademylib3
import pandas as pd
import numpy as np

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

utm_source_c=ad_clicks.groupby('utm_source').user_id.count()
print(utm_source_c)

ad_clicks['is_click']=~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head())

click_by_source=ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

clicks_pivot=click_by_source.pivot(index='utm_source',columns='is_click', values='user_id').reset_index()

clicks_pivot['percent_clicked']=clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])

exp=ad_clicks.groupby('experimental_group').user_id.count()

print(exp)
percentage=ad_clicks.groupby(['experimental_group','is_click']).user_id.count()
print(percentage)
a_clicks=ad_clicks[ad_clicks.experimental_group=='A']
b_clicks=ad_clicks[ad_clicks.experimental_group=='B']
print(a_clicks)

a_clicks_g=a_clicks.groupby(['is_click','day']).user_id.count().reset_index()
a_pivot=a_clicks_g.pivot(columns='is_click',index='day',values='user_id').reset_index()
a_pivot['percent']=a_pivot[True]/(a_pivot[True]+a_pivot[False])

b_clicks_g=b_clicks.groupby(['is_click','day']).user_id.count().reset_index()
b_pivot=b_clicks_g.pivot(columns='is_click',index='day',values='user_id').reset_index()
b_pivot['percent']=b_pivot[True]/(b_pivot[True]+b_pivot[False])

print(a_pivot)
print(b_pivot)

a_median=np.median(a_pivot['percent'])
b_median=np.median(b_pivot['percent'])

print('A: '+str(a_median))
print('B: '+str(b_median)) # A option is better with value 0.38, while B one is 0.3
