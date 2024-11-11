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
from docx import Document
import PyPDF2

# Show title and description.
st.title("📄 Upload School Course Catalogue")
st.write(
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys)."
)

# Ask user for their OpenAI API key.
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Let the user upload a file.
    uploaded_file = st.file_uploader(
        "Upload a document (.txt, .md, .pdf, .docx)", type=("txt", "md", "pdf", "docx")
    )

    def read_pdf(file):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    def read_docx(file):
        document = Document(file)
        text = ""
        for para in document.paragraphs:
            text += para.text + "\n"
        return text

    # Process the uploaded file.
    if uploaded_file:
        file_extension = uploaded_file.name.split('.')[-1].lower()
        if file_extension in ['txt', 'md']:
            document = uploaded_file.read().decode()
        elif file_extension == 'pdf':
            document = read_pdf(uploaded_file)
        elif file_extension == 'docx':
            document = read_docx(uploaded_file)
        else:
            st.error("Unsupported file type.")
            document = None

        # Ask the user for a question.
        question = st.text_area(
            "Now ask a question about the document!",
            placeholder="Can you give me a short summary?",
            disabled=not document,
        )

        if document and question:
            # Prepare the message for the OpenAI API.
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

            # Stream the response to the app.
            st.write_stream(stream)
