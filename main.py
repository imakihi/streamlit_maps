import streamlit as st
import numpy as np 
import pandas as pd 
#from PIL import Image
import time
import pydeck as pdk

st.title('Streamlit でインタラクティブな地図アプリ作成')

df = pd.read_csv('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv')

# drop na,　I got a trouble to show data if there are none in the data
# https://github.com/streamlit/streamlit/issues/984
df = df[['time','latitude','longitude','depth','mag']]
df = df.dropna()

# progress bar
#'アプリを準備しています。'
#latest_iteration = st.empty()
#bar = st.progress(0)
#for i in range(100):
#    
#    latest_iteration.text(f'進み具合 {i+1}')
#    bar.progress(i + 1)
#    time.sleep(0.1)

# column
#left_column, right_column = st.columns(2)

#btn = left_column.button('右カラムに文字を表示')
#if btn:
#    right_column.write('右')

# expander
#expder = st.expander('問い合わせ')
#expder.write('コメント１')
#expder.write('コメント２')
#expder.write('コメント３')

# table
'USGSの地震のデータです。自動的に最新のデータにアップデートされます。'
st.dataframe(df.style.highlight_max(axis=0))

# chart
'マグニチュードの頻度分布'
hist_values = np.histogram(df[['mag']], bins=8, range=(0,8))[0]
st.bar_chart(hist_values)

# map
st.map(df)

# pydeck
st.pydeck_chart(pdk.Deck(
    map_style = 'mapbox://styles/mapbox/light-v10',
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),    
    layers=[
        pdk.Layer(
        'HexagonLayer',
        data=df,
        get_position='[longitude, latitude]',
        radius=200,
        elevation_scale=50,
        elevation_range=[0, 1000],
        pickable=True,
        extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[longitude, latitude]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],    
))

#st.write('Image')

# select box
option = st.selectbox(
    '今まで経験した一番大きな地震のマグニチュードを教えてください。',
    list(range(1,11))
)
'一番大きかった地震はマグニチュード', option, 'です'

# text box (side bar)
txt = st.text_input(
    '地震が来たとき、どうしますか？'
)
'わたしは', txt

# check box.
#if st.checkbox('show image'):
#    img = Image.open('monkey.jpg')
#    st.image(img, caption='test', use_column_width=True)


# slider (side bar)
cond = st.slider('このアプリの完成度はどうでしょう？', 0,100,50)
'完成度は', cond, 'です'

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