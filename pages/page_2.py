import streamlit as st

with st.form(key='profile_form'):
    name = st.text_input('名前')
    address = st.text_input('住所')

    age_category = st.radio(
        '年齢層',
        ('子ども（１８歳未満)', '大人(１８歳以上)'))

    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(F'ようこそ！{name}さん!{address}に書籍を送ります!!')
        st.text(f'年齢層: {age_category}')

