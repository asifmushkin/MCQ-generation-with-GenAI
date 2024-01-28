import pandas as pd
from langchain import OpenAI
import streamlit as st,json,os


key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key)

def main():
    st.title("File Upload and Analysis App")
    uploaded_file = st.file_uploader("Upload a file", type=["pdf", "csv"])
    if st.button("Click to Analyze"):
        if uploaded_file is not None:
            prompt = f''' your job is to analyze the data in column COMMENT_1 for typo errors, make sure asterick represent multiplication sign.
            Extract the incorrect values as a JSON object.
            ser
            incorrect_values
            This is the body of data for finding out incorrect values.
            {uploaded_file}'''


            response = client.chat.completions.create(   
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
            ]
            )
            result = response.choices[0].message.content

            json_result = json.loads(result)

            st.success(f"Number of lines in the file: {json_result}")


        else:
            st.warning("Please upload a file first.")

if __name__ == "__main__":
    main()
