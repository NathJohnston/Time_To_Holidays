import streamlit
import datetime
import pandas as pd

streamlit.title("Holiday Countdown!! :hourglass_flowing_sand:")
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
  width=1200,
  caption='Thai Sunrise')

daysleft =str(remaining) + ' Days left until  :airplane:'
streamlit.header(daysleft)
