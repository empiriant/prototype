from dotenv import load_dotenv
import openai
import streamlit as st

@st.cache_data
def get_response(user_prompt, temperature):
    response = client.responses.create(
            model = "gpt-4o",
            input= [
                {"role": "user", "content": user_prompt}
            ],
            temperature= temperature,
            max_output_tokens= 500
        )
    
    return response



load_dotenv()
client = openai.OpenAI()

st.title("Hello, GenAI")
st.write("First Streamlit app")

user_prompt = st.text_input("Enter your input", "Describe GenAI in 1 sentence")

# add slider for temp
temperature = st.slider(
    "Model temperature",
    min_value= 0.0,
    max_value= 1.0,
    value= 0.7,
    step = 0.1,
    help= "Controls randomness"
)

with st.spinner("AI is working..."):
    response = get_response(user_prompt,temperature)
    st.write(response.output[0].content[0].text)
