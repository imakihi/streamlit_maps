import streamlit as st
import numpy as np 
import pandas as pd 
from PIL import Image
import time

st.title('Streamlit 超入門')

df = pd.read_csv('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv')

# progress bar
'プログレスバーの表示'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

# column
left_column, right_column = st.columns(2)

btn = left_column.button('右カラムに文字を表示')
if btn:
    right_column.write('右')

# expander
expder = st.expander('問い合わせ')
expder.write('コメント１')
expder.write('コメント２')
expder.write('コメント３')

# table
st.dataframe(df.style.highlight_max(axis=0))

# chart
st.line_chart(df[['mag']])

# map
st.map(df)

st.write('Image')

# select box
option = st.selectbox(
    '好きな数字を入れて',
    list(range(1,11))
)
'好きな数字は', option, 'です'

# text box (side bar)
txt = st.text_input(
    'あなたの趣味を教えてください'
)
'趣味は', txt, 'です'

# check box.
if st.checkbox('show image'):
    img = Image.open('https://ichef.bbci.co.uk/news/976/cpsprodpb/E9DF/production/_96317895_gettyimages-164067218.jpg')
    st.image(img, caption='test', use_column_width=True)


# slider (side bar)
cond = st.slider('今の感情は', 0,100,50)
'感情レベルは', cond, 'です'

# マジックコマンドでテキスト
"""
# 1
## 2
### 3

```python
import streamlit as st
import numpy as np 
import pandas as pd 
```

"""