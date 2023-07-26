import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="main menu",
        options=[
            "About me",
            "Education",
            "Skills",
            "Internship",
            "Position of responsibility",
            "Projects",
            "Social Media",
        ],
    )
with open("style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

#####################
# Header
if selected == "About me":
    st.write(
        """
  # **Samarth Pratap Singh, CSE undergraduate**.
  ##### *Resume* 
  """
    )

    image = Image.open("dp.png")
    st.image(image, width=150)

    st.markdown("## About me", unsafe_allow_html=True)
    st.info(
        """
  A meticulous and hard-working person who strives to become one of the best in his field.
  Proactive and excited to partner with like minded individuals to achieve Organisational goals.
  """
    )

#####################

# Custom function for printing text


def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"`{a}`")
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f"`{a}`")
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
if selected == "Education":
    st.markdown(
        """
  ## Education
  """
    )

    txt(
        "Pre-final year student at Jaypee institute of information technology",
        "2020-present",
    )
    st.markdown(
        """
  - CGPA: `7.2`
  """
    )

    txt("**Class XII** *Delhi Public School*, Greater Noida", "2019-2020")
    st.markdown(
        """
  - percentage: `94%`
  """
    )
    txt("**Class X** *Delhi Public School*, Greater Noida", "2017-2018")
    st.markdown(
        """
  - percentage: `96%`
  """
    )

#####################
if selected == "Skills":
    st.markdown(
        """
  ## Skills
  """
    )
    txt3("Programming", "`Python`, `C/C++`")
    txt3("Data processing", "`Mysql`, `pandas`, `numpy`")
    txt3("Data visualization", "`matplotlib`, `seaborn`, `plotly`")
    txt3("Data structures", " ")
    txt3("Data Analysis", " ")
    txt3("Microsoft Excel", " ")
    txt3("Tableau", " ")


if selected == "Internship":
    st.markdown(
        """
  ## Internship
  """
    )
    st.markdown(
        """**Backend Developer** \n
  **TO THE NEW** \n
  06/2023-08/2023"""
    )
    st.markdown("""*key skills- Python, MySQL, Database Normalization, REST APIs*""")
    st.markdown(
        """Worked on creating connection between excel workbook and MySql database using python. The database would store important details of project timesheet like timesheet generation date, startdate, end date , per day billing etc. and details like everyday tasks of employees. the database will be updated automatically whenever the timesheet is updated and a new excel file is generated with required calculations like billing amount of employees based on working days.The employee can also fetch details from database or add his details by logging in."""
    )

if selected == "Position of responsibility":
    st.markdown(
        """
  ## Position of responsibility 
  """
    )
    txt(
        "**Mentor at Microcontrollers hub**  "
        " *(Jaypee Institute of Information Technology)*",
        "2022",
    )
    st.markdown(
        """
  Using sensor platforms like Arduino uno to implement various projects in the university,involved in making a simple robotic arm and a line following robot"
  """
    )


#####################
if selected == "Projects":
    st.markdown(
        """
  ## Projects
  """
    )
    st.markdown(
        """**Stock and Crypto price analysis Dashboard--**
      The user can view opening, closing, high, low prices of stocks of various companies and compare them using various charts. This will help the user to decide on which stocks to buy and when to sell to maximize profits. Similarly, the user can also choose to view live market value of various cryptocurrencies and compare them and choose the one that will yield maximum benefits."""
    )
    st.markdown(
        """**Youtube Content moderation--**
              the user will get information about the topics that arediscussed in the Youtube video and it also labels thecontent under various sub-headings. This can help add acheck on the videos and identify sensitive informationpresent in videos."""
    )


#####################


#####################
if selected == "Social Media":
    st.markdown(
        """
  ## Social Media
  """
    )
    txt2("LinkedIn", "https://www.linkedin.com/in/samarth-pratap-singh-326b1722a/")
    txt2("GitHub", "https://github.com/Samarthh7")
