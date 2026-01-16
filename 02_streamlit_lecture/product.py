import streamlit as st

# 1:1 비율 컬럼
col1, col2 = st.columns(2)

with col1:
    st.header("왼쪽")
    st.write("여기에 왼쪽 내용")

with col2:
    st.header("오른쪽")
    st.write("여기에 오른쪽 내용")
