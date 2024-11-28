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




