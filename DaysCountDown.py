import streamlit
import datetime
import pandas as pd

streamlit.title('Holiday Countdown!!')
#streamlit.text('Days left: ')
today = datetime.date.today()

#print(today)
dt = pd.to_datetime(today, format='%Y/%m/%d')
dt1 = pd.to_datetime('2022/09/15', format='%Y/%m/%d')

remaining = (dt1-dt).days

from PIL import Image
image = Image.open('Thailand.jpg')

streamlit.image(
  image, 
  width=400,
  caption='Thai Sunrise')

daysleft ='Days left: ' + str(remaining)
streamlit.header(daysleft)
