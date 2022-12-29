import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')

'Start!!!'

latestiteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latestiteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)







#use_column_width サイトの横幅に合わせて画像を表示する
#api reference より、画像以外のmediaも表示可能（音声や動画など）



# st.write('Display DateFrame')

# df = pd.DataFrame({
#     '1列目' : [ 1 , 2 , 3 , 4 ],
#     '2列目' : [ 10 , 20 , 30 , 40 ]
# })

# #writeでも表を表示できる
# st.write(df)

#dataframe : 表の大きさを指定できるメリットがある
# st.dataframe(df.style.highlight_max(axis=0))

#table : ただ表を表示するだけ（静的な表）
# st.table(df.style.highlight_max(axis=0))

#マジックコマンド(テキストを書く) 
#api referenceのdisplay text
#texも書ける
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

#mapを書く
# df = pd.DataFrame(
#     np.random.rand(100 , 2)/[50 , 50] +[35.69 , 139.70],
#     columns = ['lat' , 'lon']
# )

# st.map(df)


#api referenceにchartの詳細について記載されている
# st.bar_chart(df)


#インタラクティブなウィジェット
#動的なUIの作成
#値を動的に変化させたりしてみよう

st.write('Interactive Widgets')

left_column , right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
#checkbox
# if st.checkbox('Show Image'):
#     img = Image.open('PB120032.JPG')
#     st.image(img , caption= 'kakegawa' , use_column_width= True)

#selectbox
# option = st.selectbox(
#     'あなたの好きな数字を教えてください、',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、', option , 'です。'

#text 入力
# text = st.sidebar.text_input('あなたの趣味を教えてください。') sidebarに持っていくことができる
# text = st.text_input('あなたの趣味を教えてください。')

# #スライダー
# condition = st.slider('あなたの今の調子は?' , 0 ,100 , 50)

# 'あなたの趣味 : ', text
# 'コンディション : ', condition

