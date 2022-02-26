import streamlit as st
import streamlit.components.v1 as components
from time import sleep

st.set_page_config(
    page_title="idkJobs",
    page_icon="https://icon-library.com/images/career-icon-png/career-icon-png-0.jpg",
    initial_sidebar_state='collapsed'
) 

roles = ["Sofware Engineer", "Data Engineer", "Cloud Engineer", "Blockchain Engineer",
         "Full-Stack Developer", "Front-End Developer", "Back-End Developer", 
         "Game Developer", "Mobile Developer"]

st.image("https://cdn.substack.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4b8647a-09e8-4576-95de-e622dcc38d72_1280x720.jpeg")
st.title("Welcome to idkJobs!") 
st.subheader("_Looking for an internship in the tech industry but don't know where to start? Fear not, you've came to the right place, simply click on the sidebar to find out more!_")

st.markdown("""---""")

st.sidebar.header("What role are you looking for?")
user_input = st.sidebar.selectbox("Select a role", roles)
st.sidebar.write("Selected role: ", user_input)
sleep(0.5)

### Kai Seong

if (user_input=="Front-End Developer"):
    c = st.container()
    c.header("**_Front-End Developer_**")
    c.markdown("<h3>What does a Front-End Developer do?</h3>", unsafe_allow_html=True)
    c.info("A front-end developer is responsible for implementing visual elements that users see and interact with in a web application.")
    c.markdown("<p>Basic knowledge needed: Web Development, HTTP Protocols</p>",
               unsafe_allow_html=True)
    c.markdown("<p>Typical tech stacks used: HTML/CSS, Javascript, React/Angular/Vue, Figma/AdobeXd</p>",
               unsafe_allow_html=True)
    
if (user_input=="Full-Stack Developer"):
    c = st.container()
    c.header("**_Full-Stack Developer_**")
    c.markdown("<h3>What does a Full-Stack Developer do?</h3>", unsafe_allow_html=True)
    c.info("A full-stack developer is responsible for designing user interactions on websites, developing servers and databases for website functionality.")
    
###

### Shao Wei
container1 = st.container()
container1.title("**_Software Engineer_**")
container1.subheader("What is a software engineer?")
container1.info("Software engineers, sometimes called software developers, create software for computers and applications.")
container1.subheader("General Job Scope:")
container1.text("-Analyze, design and develop tests and test-automation suites.\n-Design and develop a processing platform using various configuration management technologies.\n-Test software development methodology in an agile environment.\n-Provide ongoing maintenance, support and enhancements in existing systems and platforms.\n-Collaborate cross-functionally with data scientists, business users, project managers and other engineers to achieve elegant solutions.\n-Provide recommendations for continuous improvement.\n-Work alongside other engineers on the team to elevate technology and consistently apply best practices.")
container1.subheader("Pre-Requisites:")
container1.subheader("Popular Interview Questions:")
container1.text("-Experience:\nEg: Share more about the projects in your current and past work\n-Online Assessment, Live Coding, Leetcode/HackerRanks Questions\nEg: Array, Linkedlist, BinaryTree, Sort, String, Dynamic Programming, Stack&Queue, Matrix\n-System and Database Design\nEg: API Design, URL shorteners, Booking System, University Course Allocation System\n-Networking and Web Security\nEg: HTTP/HTTPS , DNS-How does it work, SSL handshake protocol\n-Operating Systems\nEg: Thread and Processes, Mutex vs Semaphore, Condition of deadlock\n")
container1.subheader("Salary Range")
# Junior	: $3000 -$7500, median: $4750
# Mid		: $4250 - $9500, median: $6500
# Senior	: $5250 - $11500, median: $7500
# Lead		: $6500 - $15950, median: $9000
# Principal	: $6700 - $17000, median: $10000
# Manager	: $7000 - $21000, median: $12000


###

### Horstann


###

### Ci Hui


###

# footer
st.markdown("---")          
st.markdown("*By **Kai Seong**, **Shao Wei**, **Ci Hui** & **Horstann** for iNTUition 2022.*")