import streamlit
import datetime
import pandas as pd

streamlit.title('Holiday Countdown!!')
streamlit.text('Days left: ')
today = datetime.date.today()

#print(today)
dt = pd.to_datetime(today, format='%Y/%m/%d')
dt1 = pd.to_datetime('2022/09/15', format='%Y/%m/%d')

daysremaining = (dt1-dt).days
