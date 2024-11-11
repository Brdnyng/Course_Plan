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

st.write("Avg weighted GPA required for admission to top 50 universities/colleges is 4.0-4.5")
# target weighted GPA

GPA = st.selectbox(
    "what is your target weighted GPA",
    ("4.5+", "4.0-4.5","3.5-4.0"),
    index=None,
    placeholder="Select target...",
)

print(GPA)

st.write("You selected:", GPA)

# intended major
major = st.selectbox(
    "what is your first choice of prefered major",
    ("Business Administration", "Psychology", "Nursing", "Biology", "Education", "Computer Science", "Communication", "Criminal Justice", "Marketing", "Engineering", "English", "Political Science", "Economics", "History", "Finance", "Accounting", "Graphic Design", "Sociology", "Public Health", "Environmental Science", "Kinesiology", "Pharmacy", "Art", "Physics", "Chemistry", "Music", "Theatre", "Mathematics", "Anthropology", "Social Work", "Architecture", "International Relations", "Film Studies", "Culinary Arts", "Agricultural Science", "Veterinary Science", "Pre-Med", "Biochemistry", "Physical Therapy", "Philosophy", "Religious Studies", "Hospitality Management", "Statistics", "Linguistics", "Sports Management", "Fashion Design", "Forestry", "Geography", "Interior Design"),
    index=None,
    placeholder="Select major...",
)

st.write("You selected:", major)

st.write("please upload your school course catalogue")

import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("📄 Document question answering")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
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

