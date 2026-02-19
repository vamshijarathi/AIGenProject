import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,  # 0 - 2
    # max_output_tokens=100,
)

system_prompt="Act as a financial analyst with 20+ years of experience; provide expert advice on stocks, mutual funds, and trading using the 'ELI5' (Explain Like I'm 5) method so that concepts like 'compounding' or 'liquidity' are easily understood by school and college students through relatable analogies and zero jargon."

st.title("Personal Investment Assistant")

question = st.text_input("Enter your query:")

if st.button("Get Suggestion"):
    messages = [
        {"role": "system", "content": system_prompt},  
        {"role": "user", "content": question}
        ]
    st.write("**Answer:**")
    st.write(llm.invoke(messages).content)