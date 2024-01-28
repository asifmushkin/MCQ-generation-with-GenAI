from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
import PyPDF2
import streamlit as st



st.title("Data QC app with Langchain 🦜⛓️")


with st.form("user input"):
    st.file_uploader("csv file")
    button=st.form_submit_button("Check Data")
    if button and uploaded_file is not None:
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_file)

                prompt = f''' your job is to analyze the data in column COMMENT_1 for typo errors, make sure asterick represent multiplication sign.
                                Extract the incorrect values as a JSON object.
                                ser
                                incorrect_values
                                This is the body of data for finding out incorrect values.
                                {"csv file"}'''
                response = client.chat.completions.create(   
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt},
                ]
                )
                result = response.choices[0].message.content
                result
            

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")