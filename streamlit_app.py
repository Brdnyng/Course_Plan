import streamlit as st

st.title("Student Information")

#Grade
grade = st.selectbox(
    "what grade are you going into",
    ("Freshman", "Sophomore", "Junior", "Senior"),
    index=None,
    placeholder="Select Grade...",
)

# plan after highschool
st.write("You selected:", grade)

plan = st.selectbox(
    "what is your plan after highschool",
    ("college", "find a job",),
    index=None,
    placeholder="Select plan...",
)

st.write("You selected:", plan)

st.write("Avg GPA required for admission to top 50 universities/colleges is 4.0-4.5")
# target weighted GPA

option = st.selectbox(
    "what is your target weighted GPA",
    ("4.5+", "4.0-4.5","3.5-4.0"),
    index=None,
    placeholder="Select target...",
)

print(option)

st.write("You selected:", option)

# intended major
option = st.selectbox(
    "what is your first choice of prefered major",
    ("4.5+", "4.0-4.5","3.5-4.0"),
    index=None,
    placeholder="Select target...",
)

st.write("You selected:", option)

st.write("please upload your school course catalogue")

import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("📄 upload school course catalogue")
st.write(
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Let the user upload a file via `st.file_uploader`.
    uploaded_file = st.file_uploader(
        "Upload a document (.txt or .md)", type=("txt", "md")
    )

    # Ask the user for a question via `st.text_area`.
    question = st.text_area(
        "Now ask a question about the document!",
        placeholder="Can you give me a short summary?",
        disabled=not uploaded_file,
    )

    if uploaded_file and question:

        # Process the uploaded file and question.
        document = uploaded_file.read().decode()
        messages = [
            {
                "role": "user",
                "content": f"Here's a document: {document} \n\n---\n\n {question}",
            }
        ]

        # Generate an answer using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True,
        )

        # Stream the response to the app using `st.write_stream`.
        st.write_stream(stream)
