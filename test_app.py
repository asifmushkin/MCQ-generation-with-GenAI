import streamlit as st,os
from langchain_openai import ChatOpenAI
from langchain_openai.llms import OpenAI



key="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"

client = OpenAI(api_key=key)

st.title("data quality checks")
