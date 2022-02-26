from enum import auto
from importlib_metadata import always_iterable
import streamlit as st
from time import sleep

st.set_page_config(
    page_title="idkJobs",
    page_icon="https://icon-library.com/images/career-icon-png/career-icon-png-0.jpg",
    initial_sidebar_state='collapsed'
) 

roles = ["Software Engineer", "Data Engineer", "Cloud Engineer", "Blockchain Engineer",
         "Front-End Developer", "Back-End Developer", 
         "Game Developer", "Mobile Developer"]

# st.image("https://cdn.substack.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4b8647a-09e8-4576-95de-e622dcc38d72_1280x720.jpeg")
st.markdown("<h1 style='text-align: center;'>Welcome to idkJobs!</h1>", unsafe_allow_html=True) 
st.markdown("<h3 style='text-align: center; font-style: italic;'>Looking for an internship/entry-level role in the tech industry but don't know where to start? Fear not, you've came to the right place, simply click on the sidebar to find out more!</h3>", unsafe_allow_html=True)

st.markdown("""---""")

st.sidebar.header("What role are you looking for?")
user_input = st.sidebar.selectbox("Select a role", roles)
st.sidebar.write("Selected role: ", user_input)
sleep(0.5)

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn01.vulcanpost.com/wp-uploads/2016/01/grab-new-logo.jpg")
    st.image("https://www.iproov.com/wp-content/uploads/2020/10/GovTech-logo-jpg.jpg")

with col2:
    st.image("https://rec-data.kalibrr.com/logos/WZ52AL7ZTEAVKP8GCSXZ-5a0ac3b4.jpg")
    st.image("https://www.gizchina.com/wp-content/uploads/images/2020/05/ByteDance-a.png")
    
with col3:
    st.image("https://mms.businesswire.com/media/20180503005604/en/3799/23/logo_white_.jpg")
    st.image("https://www.schemecolor.com/wp-content/uploads/dbs-bank-logo-768x403.png")


st.markdown("""---""")
st.markdown("<h2 style='text-align: center;'>From Zero to <i>Hero</i></h2>", unsafe_allow_html=True)
st.markdown("""
            <ol>
                    <li>Find your area of passion in the tech field.</li>
                    <li>Pick a language from the tech stack in that area.</li>
                    <li>Master the language by doing side projects and/or taking courses.</li>
                    <li>Study and revise the relevant topics in that area.</li>
                    <li>Pratice technical questions with Leetcode/HackerRank.</li>
                    <li>Prepare for potential behavioral questions.</li>
                    <li>Craft your resume neatly.</li>
                    <li>Be confident in your abilities.</li>
                    <li>Ace the interview and get the job.</li>
            </ol>
            """, unsafe_allow_html=True)
st.markdown("""---""")

### Kai Seong

if (user_input=="Front-End Developer"):
    c = st.container()
    c.image("http://dreamsoft4u.com/blog/wp-content/uploads/2019/05/Technologies-Encapsulating-the-Frontend.png")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Front-End Developer</h2>", unsafe_allow_html=True) 
    c.markdown("<h3>What does a Front-End Developer do?</h3>", unsafe_allow_html=True)
    c.info("A front-end developer is responsible for using their knowledge of programming languages to code user-side applications, including visual elements like menu bars, clickable buttons and the overall layout of websites or web applications.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Web Development, HTTP Protocols</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Tech-Stacks:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>HTML/CSS, Javascript, React/Angular/Vue, Webpack/Rollup/BaBel/AST/Gulp</h5>",
               unsafe_allow_html=True)

if (user_input=="Back-End Developer"):
    c = st.container()
    c.image("https://media.bitdegree.org/storage/media/images/2018/10/front-end-vs-back-end-developer-back-end-toolbox.png")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Back-End Developer</h2>", unsafe_allow_html=True) 
    c.markdown("<h3>What does a Back-End Developer do?</h3>", unsafe_allow_html=True)
    c.info("A back-end Developer is  responsible for server-side web application logic and integration of the work front-end web developers do. Back-end developers usually write web services and APIs used by front-end developers and mobile application developers.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Web Development, HTTP Protocols</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Tech-Stacks:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Golang, Node.js, Django, Laravel(PHP), SQL/NoSQL Databases, Agile/Scrum</h5>",
               unsafe_allow_html=True)
    
if (user_input=="Game Developer"):
    c = st.container()
    c.image("https://support.musicgateway.com/wp-content/uploads/2021/06/3-game-developer-jobs-2.png")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Game Developer</h2>", unsafe_allow_html=True)
    c.markdown("<h3>What does a Game Developer do?</h3>", unsafe_allow_html=True)
    c.info("A game developer is responsible for designing and developing video games for PC, console, and mobile applications. Their job is to code the base engine from the ideas of the design team. They may also be involved in character design, level design, animation, and unit testing.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)    

if (user_input=="Cloud Engineer"):
    c = st.container()
    c.image("https://sados.com/wp-content/uploads/2019/01/cloudengineer-750x400.jpeg")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Cloud Engineer</h2>", unsafe_allow_html=True)
    c.markdown("<h3>What does a Cloud Engineer do?</h3>", unsafe_allow_html=True)
    c.info("A cloud engineer is responsible to design, implement, and manage cloud-based systems for businesses. They develop and implement cloud-applications, migrate existing on-premise applications to the cloud, and debug cloud stacks.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h3>Tech-Stacks:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Java/AngularJS/C++/Python/PHP/Ruby, MySQL/Hadoop, Linux, AWS/Azure/Firebase</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)    

if (user_input=="Mobile Developer"):
    c = st.container()
    c.image("https://www.ipraxa.com/blog/wp-content/uploads/2018/09/mobile-app-development-technologies.png")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Mobile Developer</h2>", unsafe_allow_html=True)
    c.markdown("<h3>What does a Mobile Developer do?</h3>", unsafe_allow_html=True)
    c.info("A mobile developer uses programming languages and development skills to create, test, and develop applications on mobile devices. They work in popular operating system environments like iOS and Android and often take into account UI and UX principles when creating applications.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)    
    
if (user_input=="Data Engineer"):
    c = st.container()
    c.image("https://149695847.v2.pressablecdn.com/wp-content/uploads/2017/11/why-data-engineer-trending-01.jpg")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Data Engineer</h2>", unsafe_allow_html=True)
    c.markdown("<h3>What does a Data Engineer do?</h3>", unsafe_allow_html=True)
    c.info("A developer who is responsible to build systems that collect, manage, and convert raw data into usable information for data scientists and business analysts to interpret. Their ultimate goal is to make data accessible so that organizations can use it to evaluate and optimize their performance.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Blockchain Architecture, Cryptography, Smart Contract Development, Web-Development</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>Differentiate between Blockchain and Hyperledger.</li>
                    <li>What happens when you try to deploy a file with multiple contracts?</li>
                    <li>List down some of the extensively used cryptographic algorithms.</li>
                    <li>Where do nodes run a smart contract code? </li>
                    <li>Explain a real-life use-case where Blockchain is being used.</li>
                    <li>What is a 51% attack? </li>
                    <li>Write a crowd-scale smart contract code in Solidity programming language.</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)
    
###

### Shao Wei

if (user_input=="Software Engineer"):
    c = st.container()
    c.image("http://www.cybersorcerors.com/uploads/1/2/0/3/120346811/softwareengineeringdiagram_orig.jpg")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Software Engineer</h2>", unsafe_allow_html=True)
    c.markdown("<h3>What does a Software Engineer do?</h3>", unsafe_allow_html=True)
    c.info("A software engineer is responsible for creating software for computers and applications. He will have to analyze, design and develop tests and test-automation as well as collaborate cross-functionally with data scientists, business users, project managers and other engineers to achieve elegant solutions")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Discrete Math, Data Structure and Algorithms, Algorithm Analysis, Web-Development, Databases, Operating Systems, System Design</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Tech-Stacks:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Node.js, Python/PHP/Java/C/JavaScript, React, MySQL, Django, Ruby, Apache, Nginx</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)
    

# container1 = st.container()
# container1.title("**_Software Engineer_**")
# container1.subheader("What is a software engineer?")
# container1.info("Software engineers, sometimes called software developers, create software for computers and applications.")
# container1.subheader("General Job Scope:")
# container1.text("-Analyze, design and develop tests and test-automation suites.\n-Design and develop a processing platform using various configuration management technologies.\n-Test software development methodology in an agile environment.\n-Provide ongoing maintenance, support and enhancements in existing systems and platforms.\n-Collaborate cross-functionally with data scientists, business users, project managers and other engineers to achieve elegant solutions.\n-Provide recommendations for continuous improvement.\n-Work alongside other engineers on the team to elevate technology and consistently apply best practices.")
# container1.subheader("Pre-Requisites:")
# container1.subheader("Popular Interview Questions:")
# container1.text("-Experience:\nEg: Share more about the projects in your current and past work\n-Online Assessment, Live Coding, Leetcode/HackerRanks Questions\nEg: Array, Linkedlist, BinaryTree, Sort, String, Dynamic Programming, Stack&Queue, Matrix\n-System and Database Design\nEg: API Design, URL shorteners, Booking System, University Course Allocation System\n-Networking and Web Security\nEg: HTTP/HTTPS , DNS-How does it work, SSL handshake protocol\n-Operating Systems\nEg: Thread and Processes, Mutex vs Semaphore, Condition of deadlock\n")
# container1.subheader("Salary Range")
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

if (user_input=="Blockchain Engineer"):
    c = st.container()
    c.image("https://d1rytvr7gmk1sx.cloudfront.net/wp-content/uploads/2020/08/istock-1131340856.jpg")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Blockchain Engineer</h2>", unsafe_allow_html=True)
    c.markdown("<h3>What does a Blockchain Engineer do?</h3>", unsafe_allow_html=True)
    c.info("A developer who is responsible for designing, developing and optimizing blockchain protocols, designing the network architecture of blockchain system that can be used for centralizing or decentralizing the data, developing and monitoring smart contracts and web apps using blockchain technology, developing front-end designs according to client requirements and backend development according to the Blockchain protocols in general. ")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Blockchain Architecture, Cryptography, Smart Contract Development, Web-Development</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>Differentiate between Blockchain and Hyperledger.</li>
                    <li>What happens when you try to deploy a file with multiple contracts?</li>
                    <li>List down some of the extensively used cryptographic algorithms.</li>
                    <li>Where do nodes run a smart contract code? </li>
                    <li>Explain a real-life use-case where Blockchain is being used.</li>
                    <li>What is a 51% attack? </li>
                    <li>Write a crowd-scale smart contract code in Solidity programming language.</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)

###

st.markdown("""---""")
st.markdown("<h2 style='text-align: center;'>Sources</h2>", unsafe_allow_html=True)
st.markdown("""
            
            """, unsafe_allow_html=True)
st.markdown("""---""")


# footer
st.markdown("""---""")          
st.markdown("*By **Kai Seong**, **Shao Wei**, **Ci Hui** & **Horstann** for iNTUition 2022.*")