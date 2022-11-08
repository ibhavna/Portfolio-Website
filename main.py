import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json

# set page configurations from long to wide
st.set_page_config(page_title="Personal_Portfolio", page_icon="🧊", layout="wide",initial_sidebar_state="expanded",)

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


# Header 
st.subheader("**Hi, I am Bhavna :wave:**")
st.write('''
# **A Computer Science Engineer!** 
''')


def load(filepath:str):
  with open(filepath, "r") as f:
    return json.load(f)
  

animation = load("animation.json")
st_lottie(animation,speed = 5,height=250, loop = True)



st.markdown('## Summary', unsafe_allow_html=True)
st.error('''
- Logical and organised individual with a strong foundation in computer science engineering. 
- Passionate about implementing and launching new projects and always open to learn new technologies.
- Excellent teamwork, interpersonal and communication skills.
- Looking to start the career as an entry-level software engineer with a reputed firm driven by technology.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #800000;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experiences">Work Experiences</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#achievements-responsibilities">Achievements/Responsibilities</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#connect">Connect</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#download-resume">Download Resume</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)


def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

#####################
st.markdown('''
## Education
''')

txt('**Bachelor of Technology** (Computer Science), *Sagar Institute of Science Technology and Research (SISTec-R)*, Bhopal','2019-2023')
st.markdown('''
- CGPA: `8.58` (Till 5th Semester)
- Ongoing Course
''')

txt('**XII** (PCM), *Vikram Higher Secondary School (CBSE)*, Bhopal','')
st.markdown('''
- Percentage: `77.80%`
''')

txt('**X** *Vikram Higher Secondary School (CBSE)*, Bhopal','')
st.markdown('''
- CGPA: `9.0`
''')

st.write('#')
#####################
st.markdown('''
## Skills
''')
txt3('Programming:', '`Python (Strong)`, `C (Basic)`, `C++ (Basic)`')
txt3('DataBase:', '`MySQL`')
txt3('Data Analysis:', '`Pandas, Numpy, Scikit-learn`')
txt3('Business Intelligence:', '`Power BI`')
txt3('GUI:', '`Tkinter`, `Streamlit`')
txt3('Web Scraping:', '`Selenium`,`Beautiful Soup`')
txt3('Web development:', '`Flask`, `HTML5`')
txt3('Model deployment:', '`Streamlit Clouds`, `Heroku`')

st.write("#")
#####################
st.markdown('''
## Work Experiences
''')

txt('**Python Developer - Intern**, Credicxo Tech PVT Ltd, Delhi','Jan/2022- Apr/2021') 
st.markdown('''
- Developed automated code for trading in stocks and share market.
- Done Web Scraping for various sites and exported the data.
- Data Analysis and Cleaning of data using packages like Pandas, Numpy etc
''')

txt('**SEO Executive**, SEOBeam Infotech PVT Ltd, Bhopal','Dec/2021- Jan/2022')
st.markdown('''
- Worked as an Onpage Executive and lead a team of 4 members.
- Role was to design and implement On-Page strategies on the website and also to make Off-Page task calender.
- Made various types of SEO Reports, and enhanced SERP ranking of various webpages by fixing the On-page errors.
- Also collaborated Worked with developers to implement changes in the code of the website.
''')

txt('**Python Developer - Intern**, Abstinent Research and Technology, Bhopal','Sep/2021- Dec/2021')
st.markdown('''
- Built Flask web apps and integrated it with databases (MySQL and MongoDB).
- Done Web Scraping using libraries BS4, Selenium and created database for the same.
- Done Data Analysis using Pandas, Numpy and made Power BI Dashboards.
''')

txt('**SEO Executive**, DDM Informatics, Bhopal','Apr/2021- Sep/2021')
st.markdown('''
- Started here as an Off-Page Executive and had done tasks like Social Bookmarking, Various Submissions and Promotions.
- Had also worked on Google ADsense to generate inorganic traffic. 
- Got familiar and worked with many tools like SEMRush, Google Analytics, Google Search Console etc.
- Had worked on Backend of website as well for optimizing the code.
''')

st.write('#')
######################
st.markdown('''
## Projects
''')

st.markdown(""" **Python Based Personal Portfolio Website**-
<a href = "https://github.com/ibhavna/Portfolio-Website/">Link</a>""",
unsafe_allow_html=True)
st.markdown('''
- Made this website to showcase a detailed view of my profile to recruiters.
- This is entirely based on python's package 'Streamlit' and have also done basic styling using B4,CSS.
- Have also embedded a submission form which will directly mail the response to me.
- *Technologies :- Python, Streamlit, HTML, Bootstrap4, CSS.*
''',unsafe_allow_html=True)

st.markdown(""" **AI Based Virtual Assistant with GUI**-
<a href = "https://github.com/ibhavna/Personal-Assistant">Link</a>""",
unsafe_allow_html=True)
st.markdown('''
- Made this Virtual Assistant as my first AI project. I have also integrated it with an interactive GUI.
- GUI would allow us to change the name of the assistant and to run the assistant as many times we want.
- I have used various API's into it, like news reading, weathermap. This Assistant can also read a book for you.
- *Technologies :- Python, Speech Recognition, Tkinter, pysttx3, and many other python libraries.*
''',unsafe_allow_html=True)

st.markdown(""" **Automated Stock Order Placing Application with Telegram Bot**-
<a href = "https://github.com/ibhavna/Automated-Stock-Order-Placing-Application">Link</a>""",
unsafe_allow_html=True)
st.markdown('''
- This was developed to place specific stock orders from Zerodha Trade Platform to Kotak Security Trade Platform.
- Used regex to get the instrument token from the response of Kotak's API to get list of Stock Listings.
- It was also integrated with a Telegram Bot to send the error messages if orders were not placed.
- *Technologies :- Python, Jugaad Traders API, ks_api_client, Botfather, Pandas, Regex.*
''',unsafe_allow_html=True)


#####################
st.markdown('''
## Achievements/Responsibilities
''')
st.markdown('''
- 5 star coder at HackerRank in Python. 
- 1st Prize in Singing and Instrumental Performance (SISTec-R)
- Startup Coordinator at IIC (SISTec-R ).
- Cultural Coordinator at SAC (SISTec-R).
- Student Coordinator at Anti-Ragging Committee (SISTec-R)
''')




#####################
st.markdown('''
## Connect
''')
txt3('Mobile No :','+91-7974719844')
txt3('Mail @ :', 'bhavnach2000@gmail.com')
txt3('Residency :',' Bhopal, MadhyaPradesh, India')
txt3('LinkedIn :', 'https://www.linkedin.com/in/ibhavnachilhate/')
txt3('GitHub :', 'https://github.com/ibhavna')

pdfFileObj = open('Bhavna_Resume.pdf','rb')

embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="ibhavnachilhate" data-version="v1">
                <a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/ibhavnachilhate/?trk=profile-badge" style="display:none">Bhavna Chilhate</a></div>
                """}
# Documentation: https://formsubmit.co/ 
contact_form = """
    <form action="https://formsubmit.co/bhavnach2000@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

#####################
st.markdown('''
## Download Resume
''')
st.download_button('Download Resume',pdfFileObj, file_name='Bhavna_resume_p.pdf',mime='pdf')

with st.sidebar:
    st.header("**Connect with me!**")
    st.components.v1.html(embed_component['linkedin'],height=310)
    st.write("**Send me a message here!**")
    st.markdown(contact_form, unsafe_allow_html=True)
    st.markdown("#")
    




