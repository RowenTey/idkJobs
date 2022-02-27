import streamlit as st
import webbrowser
from time import sleep

st.set_page_config(
    page_title="idkJobs",
    page_icon="https://cdn-icons-png.flaticon.com/512/747/747086.png",
    initial_sidebar_state='collapsed'
) 

roles = ["Software Engineer", "Data Engineer", "Cloud Engineer", "Blockchain Engineer",
         "Front-End Developer", "Back-End Developer", 
         "Game Developer", "Mobile Developer"]

prep = ["Resume", "Behavioural Questions", "General Technical Questions", "Interview Dos and Don'ts"]

st.markdown("<h1 style='text-align: center;'>Welcome to idkJobs!</h1>", unsafe_allow_html=True) 
st.markdown("""<h3 style='text-align: center; font-style: italic;'>Looking for an internship/entry-level 
            role in the tech industry but don't know where to start? Fear not, you've came to the right place!</h3>""", unsafe_allow_html=True)
st.markdown("""---""")

st.sidebar.header("What role are you looking for?")
user_input = st.sidebar.selectbox("Select a role", roles)
st.sidebar.write("Selected role: ", user_input)
st.sidebar.header("Which area do you want to prepare for?")
user_input_prep = st.sidebar.selectbox("Select an area", prep)
st.sidebar.write("Selected area: ", user_input_prep)
sleep(0.5)

### Top companies
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

### Step by step guide
st.markdown("""---""")
st.markdown("<h2 style='text-align: center;'>From Zero to <i>Hero</i></h2>", unsafe_allow_html=True)
st.markdown("""
            <ol>
                    <li>Find your area of passion in the tech field.</li>
                    <li>Pick a language from the tech stack in that area.</li>
                    <li>Master the language by doing side projects and/or taking courses.</li>
                    <li>Study and revise  relevant topics in that area.</li>
                    <li>Practice technical questions with Leetcode/HackerRank.</li>
                    <li>Prepare for potential behavioral questions.</li>
                    <li>Craft your resume neatly.</li>
                    <li>Prepare a list of good questions to ask.</li>
                    <li>Be confident in your abilities.</li>
                    <li>Ace the interview and get the job.</li>
            </ol>
            """, unsafe_allow_html=True)
st.markdown("""---""")

### Interview formats
st.markdown("<h2 style='text-align: center;'>Interview <i>Formats</i></h2>", unsafe_allow_html=True)
st.markdown("<h3>Quiz:</h3>", unsafe_allow_html=True)
st.markdown("""
            <p>
                    Quizzes are meant to be a first-pass filter as a quick and dirty way of weeding out extremely weak 
                    (or even non-technical) candidates. They are structured questions and have clear-cut answers which makes them 
                    possible to be administered by recruiters/non-technical folks or automated graders. 
                    They are typically done early in the process.
            </p>
            """, unsafe_allow_html=True)
st.markdown("<h3>Onlline coding assessment:</h3>", unsafe_allow_html=True)
st.markdown("""
            <p>
                    Like quizzes, online coding assessments are usually given early in the process. An algorithm problem is given 
                    with well-formed input and output and candidates are expected to write code in an online coding interface to 
                    solve the problem. Hackerrank is a very common platform for conducting online coding assessments. LeetCode 
                    would be a good way to practice for the problem solving aspects of online coding assessments. However, in 
                    Hackerrank you are typically expected to write code to read from stdin and also print to stdout, which can 
                    trip candidates up if they aren't familiar with the APIs.
            </p>
            """, unsafe_allow_html=True)
st.markdown("<h3>Take home assignment:</h3>", unsafe_allow_html=True)
st.markdown("""
            <p>
                    There has been numerous debates on whether asking algorithm questions are a good way of assessing individual 
                    abilities as they aren't exactly the most relevant skills needed on a day-to-day basis at a job. Take home assignment 
                    is a format designed to address the shortcomings of the algorithm interview by getting candidates to work on larger 
                    projects which allow them to demonstrate software design skills.
            </p>
            """, unsafe_allow_html=True)
st.markdown("""
            <p>
                    However, this interview format takes up more time from both the candidates and the company and hence it is not as 
                    commonly seen in large companies where they have a high volume of candidates. This format is more common among 
                    startups and small companies.
            </p>
            """, unsafe_allow_html=True)
st.markdown("<h3>Phone Interview:</h3>", unsafe_allow_html=True)
st.markdown("""
            <p>
                    Phone interviews are the most common format and every candidate will face this at least once while interviewing. 
                    You will be asked to speak with an interviewer either over a phone call or VoIP (BlueJeans/Skype/Google Hangout). 
                    A question will be given to you and you will work on that question using an online collaborative editor 
                    (CoderPad/CodePen/Google Docs).
            </p>
            """, unsafe_allow_html=True)
st.markdown("""
            <p>
                    You are usually not allowed to execute the code even if the editor supports execution. So don't rely on that for 
                    verifying the correctness of your solution. Formats would differ slightly depending on the roles you are applying 
                    to. Many companies like to use CoderPad for collaborative code editing. CoderPad supports running of the program, 
                    so it is possible that you will be asked to fix your code such that it can be run. For front end interviews, many 
                    companies like to use CodePen, and it will be worth your time to familiarize yourself with the user interfaces of 
                    such web-based coding environments.
            </p>
            """, unsafe_allow_html=True)
st.markdown("<h3>Onsite:</h3>", unsafe_allow_html=True)
st.markdown("""
            <p>
                    If you have made it to this stage, congratulations! This is usually the final stage before an offer decision. 
                    Candidates who made it to the onsite stage will be required to have an in-person interview at the office. If you 
                    are an overseas candidate, companies might even fly you in and pay for your accommodations!
            </p>
            """, unsafe_allow_html=True)
st.markdown("""
            <p>
                    The onsite stage usually consists of multiple rounds (coding, system design, behavioral) and is expected to last 
                    for a few hours. Since you are onsite, it is possible that you will be asked to do a whiteboard exercise with an 
                    interviewer, usually either solving an algorithm question or a system design question. It is also possible that you 
                    have to bring your own laptop and work on a project/solve a coding problem on the spot.
            </p>
            """, unsafe_allow_html=True)
st.markdown("""
            <p>
                    For onsite interviews at smaller (non-public) companies, most will allow (and prefer) that you use your own laptop. 
                    Hence it is important that you prepare your development environment in advance.
            </p>
            """, unsafe_allow_html=True)
st.markdown("""
            <p>
                    If the company provides lunch, you might also have a lunch session with an employee where you can find out more 
                    about the company culture.
            </p>
            """, unsafe_allow_html=True)
st.markdown("""---""")

st.markdown("""<h3 style='text-align: center; font-style: italic;'>
            Now simply open the sidebar for more info to prepare for your interview!
            </h3>""", unsafe_allow_html=True)
st.markdown("""---""")

### Role info
if (user_input=="Front-End Developer"):
    c = st.container()
    c.image("http://dreamsoft4u.com/blog/wp-content/uploads/2019/05/Technologies-Encapsulating-the-Frontend.png")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Front-End Developer</h2>", unsafe_allow_html=True) 
    c.markdown("<h3>What does a Front-End Developer do?</h3>", unsafe_allow_html=True)
    c.info("A front-end developer is responsible for using their knowledge of programming languages to code user-side applications, including visual elements like menu bars, clickable buttons and the overall layout of websites or web applications.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Web Development, HTTP Protocols, Data Structures and Algorithms, User Interface</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Tech-Stacks:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>HTML/CSS, Javascript, React/Angular/Vue, Webpack/Rollup/BaBel/AST/Gulp</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>What is ‘Version Control System’?</li>
                    <li>What are your favorite features of HTML5, and how have you implemented them in your front-end development projects?</li>
                    <li>Can you explain the concept of a CSS float and provide an example of its usage?</li>
                    <li>Explain how you would ensure that your web design is user-friendly and what kinds of steps would you use?</li>
                    <li>What is User Centered Design?</li>
                    <li>If Node.js is single threaded, then how does it handle concurrency?</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)
    c.markdown("<h5>Junior : <i>$1000 - $5400</i></h5>",
               unsafe_allow_html=True)

if (user_input=="Back-End Developer"):
    c = st.container()
    c.image("https://media.bitdegree.org/storage/media/images/2018/10/front-end-vs-back-end-developer-back-end-toolbox.png")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Back-End Developer</h2>", unsafe_allow_html=True) 
    c.markdown("<h3>What does a Back-End Developer do?</h3>", unsafe_allow_html=True)
    c.info("A back-end Developer is  responsible for server-side web application logic and integration of the work front-end web developers do. Back-end developers usually write web services and APIs used by front-end developers and mobile application developers.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Web Development, API Development, Data Structures and Algorithms, Databases</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Tech-Stacks:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Golang, Node.js, Django, Laravel(PHP), SQL/NoSQL Databases, Agile/Scrum</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>How would you manage Web Services API versioning?</li>
                    <li>What is CAP Theorem?</li>
                    <li>How would you find the most expensive queries in an application?</li>
                    <li>How to mitigate the SQL Injection risks?</li>
                    <li>How does B-trees Index work?</li>
                    <li>Which sorting algorithm to use and when?</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)
    c.markdown("<h5>Junior : <i>$1000 - $5000</i></h5>",
               unsafe_allow_html=True)
    
if (user_input=="Game Developer"):
    c = st.container()
    c.image("https://support.musicgateway.com/wp-content/uploads/2021/06/3-game-developer-jobs-2.png")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Game Developer</h2>", unsafe_allow_html=True)
    c.markdown("<h3>What does a Game Developer do?</h3>", unsafe_allow_html=True)
    c.info("A game developer is responsible for designing and developing video games for PC, console, and mobile applications. Their job is to code the base engine from the ideas of the design team. They may also be involved in character design, level design, animation, and unit testing.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Game Design Pattern, 3D Graphics and Associated Maths, Graphics Programming</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Tech-Stacks:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Unity, three.js. Unreal Engine, Phaser, Godot</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>What game are you most proud of developing and why?</li>
                    <li>What are the models used to make money in gaming business?</li>
                    <li>Why C++ language is more preferred for game development?</li>
                    <li>How can you reduce game lag?</li>
                    <li>How good is Bitbucket/GitHub for game development?</li>
                    <li>What is “onsurfacecreated” in Android game development?</li> 
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)
    c.markdown("<h5>Junior : <i>$1000 - $4100</i></h5>",
               unsafe_allow_html=True)     

if (user_input=="Cloud Engineer"):
    c = st.container()
    c.image("https://sados.com/wp-content/uploads/2019/01/cloudengineer-750x400.jpeg")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Cloud Engineer</h2>", unsafe_allow_html=True)
    c.markdown("<h3>What does a Cloud Engineer do?</h3>", unsafe_allow_html=True)
    c.info("A cloud engineer is responsible to design, implement, and manage cloud-based systems for businesses. They develop and implement cloud-applications, migrate existing on-premise applications to the cloud, and debug cloud stacks.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Understand LinuxOS, Networking and Internet Protocols, DevOps and Containerization</h5>",
               unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Understand Virtualization, Web Services and API, Cloud Service Providers</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Tech-Stacks:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Java/AngularJS/C++/Python/PHP/Ruby, MySQL/Hadoop, Linux, AWS/Azure/Firebase/GCP</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>Describe the different cloud service models?</li> 
                    <li>What is The Packaging of Hybrid Cloud? What are the two main types of packaged hybrid cloud?</li>
                    <li>What is a Distributed Cloud?</li>
                    <li>What does Edge Computing mean, and how is it related to the cloud?</li>
                    <li>Which are the main constituents of the cloud ecosystem?</li>
                    <li>Mention the reliability and availability of Cloud Computing.</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)  
    c.markdown("<h5>Junior : <i>$1800 - $5300</i></h5>",
               unsafe_allow_html=True)  

if (user_input=="Mobile Developer"):
    c = st.container()
    c.image("https://www.ipraxa.com/blog/wp-content/uploads/2018/09/mobile-app-development-technologies.png")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Mobile Developer</h2>", unsafe_allow_html=True)
    c.markdown("<h3>What does a Mobile Developer do?</h3>", unsafe_allow_html=True)
    c.info("A mobile developer uses programming languages and development skills to create, test, and develop applications on mobile devices. They work in popular operating system environments like iOS and Android and often take into account UI and UX principles when creating applications.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Program Design, User Interface, Data Structures and Algorithms, Databases, Operating System</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Tech-Stacks:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Flutter/React Native, Cordova/Ionic</h5>",
               unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>IOS - Objectice-C & Swift</h5>",
               unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Android - Java & Kotlin</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>List some benefits of using React Native for building mobile apps?</li>
                    <li>What are the advantages of hybrid apps over native apps?</li>
                    <li>How to persist data in an Android app?</li>
                    <li>What is the difference between PhoneGap, Cordova, and Ionic?</li>
                    <li>How to avoid reverse engineering of an APK file? </li>
                    <li>What is Builder pattern?</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True) 
    c.markdown("<h5>Junior : <i>$2500 - $5000</i></h5>",
               unsafe_allow_html=True)     
    
if (user_input=="Data Engineer"):
    c = st.container()
    c.image("https://149695847.v2.pressablecdn.com/wp-content/uploads/2017/11/why-data-engineer-trending-01.jpg")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Data Engineer</h2>", unsafe_allow_html=True)
    c.markdown("<h3>What does a Data Engineer do?</h3>", unsafe_allow_html=True)
    c.info("A developer who is responsible to build systems that collect, manage, and convert raw data into usable information for data scientists and business analysts to interpret. Their ultimate goal is to make data accessible so that organizations can use it to evaluate and optimize their performance.")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Operating Systems, Databases, Data Warehousing, Machine Learning</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Tech-Stacks:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>SQL, Java/Python/Go, DynamoDB/Hadoop/MongoDB, AWS/GCP/Azure, Spark/Apache, Beam, Flink</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Popular Interview Questions:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>What are the differences between structured and unstructured data?</li> 
                    <li>Can you speak about types of design schemas in data modelling?</li>
                    <li>What is your experience of Big Data in a cloud environment?</li>
                    <li>What is the replication factor in HDFS?</li>
                    <li>How can Data Analytics and Big Data help to positively impact the bottom line of the company?</li>
                    <li>What are the security features in Hadoop?</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)
    c.markdown("<h5>Intern : <i>$900 - $2000</i></h5>",
               unsafe_allow_html=True)
    c.markdown("<h5>Junior : <i>$3150 - $8500</i></h5>",
               unsafe_allow_html=True)
    c.markdown("<h5>Median : <i>$5500</i></h5>",
               unsafe_allow_html=True)
    
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
    c.markdown("""
               <ul>
                    <li>What is Software configuration management?</li>
                    <li>What are functional and non-functional requirements?</li>
                    <li>What is modularization?</li>
                    <li>Which process model removes defects before software gets into trouble?</li>
                    <li>Do you think that the maintenance of software is expensive?</li>
                    <li>What are your thoughts on Agile development</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Salary Range:</h3>", unsafe_allow_html=True)
    c.markdown("<h5>Intern : <i>$1000 - $4000</i></h5>",
               unsafe_allow_html=True)
    c.markdown("<h5>Junior : <i>$3000 - $7500</i></h5>",
               unsafe_allow_html=True)
    c.markdown("<h5>Median : <i>$4750</i></h5>",
               unsafe_allow_html=True)

if (user_input=="Blockchain Engineer"):
    c = st.container()
    c.image("https://d1rytvr7gmk1sx.cloudfront.net/wp-content/uploads/2020/08/istock-1131340856.jpg")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Blockchain Engineer</h2>", unsafe_allow_html=True)
    c.markdown("<h3>What does a Blockchain Engineer do?</h3>", unsafe_allow_html=True)
    c.info("A developer who is responsible for designing, developing and optimizing blockchain protocols, designing the network architecture of blockchain system that can be used for centralizing or decentralizing the data, developing and monitoring smart contracts and web apps using blockchain technology, developing front-end designs according to client requirements and backend development according to the Blockchain protocols in general. ")
    c.markdown("<h3>Pre-Requisites:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>Blockchain Architecture, Cryptography, Smart Contract Development, Web-Development</h5>",
               unsafe_allow_html=True)
    c.markdown("<h3>Tech-Stacks:</h3>", unsafe_allow_html=True)
    c.markdown("<h5 style='font-style: italic;'>C++, Java, C#, JavaScript, Go, Python, Ruby, Solidity</h5>",
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
    c.markdown("<h5>Junior : <i>$3730 - $10400</i></h5>",
               unsafe_allow_html=True)  

### Revision area
if (user_input_prep=="Resume"):
    c = st.container()
    c.markdown("""---""")
    c.image("https://static.jobscan.co/blog/uploads/Top-Resume-Keywords-1.jpg")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>How To Create Your Resume</h2>", unsafe_allow_html=True)
    c.markdown("<h3>Four steps:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ol>
                    <li>Set up your ATS-proof resume template</li>
                    <li>Fill up your template with effective resume content following a recommended format</li>
                    <li>Optimize your resume with keywords</li>
                    <li>Review your resume using free tools</li>
                </ol>
               """,
               unsafe_allow_html=True)

if (user_input_prep=="Behavioural Questions"):
    c = st.container()
    c.markdown("""---""")
    c.image("https://cdn.seeklearning.com.au/media/images/career-guide/article/career-advice/web_images/blogs/214/4170/2018June_Behavioural_940x485.webp")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Behavioural Questions</h2>", unsafe_allow_html=True)
    c.markdown("<h3>General questions:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>Why do you want to work for X company?</li>
                    <li>Why do you want to leave your current/last company?</li>
                    <li>What are you looking for in your next role?</li>
                    <li>Tell me about a time when you had a conflict with a co-worker.</li>
                    <li>Tell me about a time in which you had a conflict and needed to influence somebody else.</li>
                    <li>What project are you currently working on?</li>
                    <li>What is the most challenging aspect of your current project?</li>
                    <li>What was the most difficult bug that you fixed in the past 6 months?</li>
                    <li>How do you tackle challenges? Name a difficult challenge you faced while working on a project, how you overcame it, and what you learned.</li>
                    <li>What are you excited about?</li>
                    <li>What frustrates you?</li>
                    <li>Imagine it is your first day here at the company. What do you want to work on? What features would you improve on?</li>
                    <li>What are the most interesting projects you have worked on and how might they be relevant to this company's environment?</li>
                    <li>Tell me about a time you had a disagreement with your manager.</li>
                    <li>Talk about a project you are most passionate about, or one where you did your best work.</li>
                    <li>What does your best day of work look like?</li>
                    <li>What is something that you had to push for in your previous projects?</li>
                    <li>What is the most constructive feedback you have received in your career?</li>
                    <li>What is something you had to persevere at for multiple months?</li>
                    <li>Tell me about a time you met a tight deadline.</li>
                    <li>If this were your first annual review with our company, what would I be telling you right now?</li>
                    <li>Time management has become a necessary factor in productivity. Give an example of a time-management skill you've learned and applied at work.</li>
                    <li>Tell me about a problem you've had getting along with a work associate.</li>
                    <li>What aspects of your work are most often criticized?</li>
                    <li>How have you handled criticism of your work?</li>
                    <li>What strengths do you think are most important for your job position?</li>
                    <li>What words would your colleagues use to describe you?</li>
                    <li>What would you hope to achieve in the first six months after being hired?</li>
                    <li>Tell me why you will be a good fit for the position.</li>
                </ul>
               """,
               unsafe_allow_html=True)

if (user_input_prep=="Interview Dos and Don'ts"):
    c = st.container()
    c.markdown("""---""")
    c.image("https://au.hudson.com/wp-content/cache/bb-plugin/cache/dos-donts-01-1024x731-landscape.jpg")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>Interview Dos and Don'ts</h2>", unsafe_allow_html=True)
    c.markdown("<h4 style='text-align: center; font-style: italic;'>Source: <a href='https://www.techinterviewhandbook.org/cheatsheet/'>Tech Interview Handbook</a></h4>", unsafe_allow_html=True)
    c.markdown("<h3>Before interview:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>✅ Prepare pen, paper and earphones/headphones.</li>
                    <li>✅ Find a quiet environment with good Internet connection.</li>
                    <li>✅ Ensure webcam and audio are working. There were times I had to restart Chrome to get Hangouts to work again.</li>
                    <li>✅ Request for the option to interview over Hangouts/Skype instead of a phone call; it is easier to send links or text across.</li>
                    <li>✅ Decide on and be familiar with a programming language.</li>
                    <li>✅ Familiarize yourself with the coding environment (CoderPad/CodePen). Set up the coding shortcuts, turn on autocompletion, tab spacing, etc.</li>
                    <li>✅ Prepare answers to the frequently-asked behavioral questions in an interview.</li>
                    <li>✅ Prepare some questions to ask at the end of the interview.</li>
                    <li>✅ Dress comfortably. Usually you do not need to wear smart clothes, casual should be fine. T-shirts and jeans are acceptable at most places.</li>
                    <li>✅ Stay calm and composed.</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Introduction:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>✅ Introduce yourself in a few sentences under a minute or two.</li>
                    <li>✅ Mention interesting points that are relevant to the role you are applying for.</li>
                    <li>✅ Sound enthusiastic! Speak with a smile and you will naturally sound more engaging.</li>
                    <li>❌ Spend too long introducing yourself. The more time you spend talking the less time you have to code.</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Upon Receiving The Question:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>✅   Repeat the question back at the interviewer.</li>
                    <li>✅	Clarify any assumptions you made subconsciously. Many questions are under-specified on purpose. E.g. a tree-like diagram could very well be a graph that allows for cycles and a naive recursive solution would not work.</li>
                    <li>✅	Clarify input format and range. Ask whether input can be assumed to be well-formed and non-null.</li>
                    <li>✅	Work through a small example to ensure you understood the question.</li>
                    <li>✅	Explain a high level approach even if it is a brute force one.</li>
                    <li>✅	Improve upon the approach and optimize. Reduce duplicated work and cache repeated computations.</li>
                    <li>✅	Think carefully, then state and explain the time and space complexity of your approaches.</li>
                    <li>✅	If stuck, think about related problems you have seen before and how they were solved. Check out the tips in this section.</li>
                    <li>❌	Ignore information given to you. Every piece is important.</li>
                    <li>❌	Jump into coding straightaway.</li>
                    <li>❌	Start coding without interviewer's green light.</li>
                    <li>❌	Appear too unsure about your approach or analysis.</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Code Out Your Solution:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>✅	Explain what you are coding/typing to the interviewer, what you are trying to achieve.</li>
                    <li>✅	Practice good coding style. Clear variable names, consistent operator spacing, proper indentation, etc.</li>
                    <li>✅	Type/write at a reasonable speed. Too slow is no good.</li>
                    <li>✅	As much as possible, write actual compilable code, not pseudocode.</li>
                    <li>✅	Write in a modular fashion. Extract out chunks of repeated code into functions.</li>
                    <li>✅	Ask for permission to use trivial functions without having to implement them; saves you some time.</li>
                    <li>✅	Use the hints given by the interviewer.</li>
                    <li>✅	Demonstrate mastery of your chosen programming language.</li>
                    <li>✅	Demonstrate technical knowledge in data structures and algorithms.</li>
                    <li>✅	If you are cutting corners in your code, state that out loud to your interviewer and say what you would do in a non-interview setting (no time constraints). E.g., "Under non-interview settings, I would write a regex to parse this string rather than using split() which may not cover all cases."</li>
                    <li>✅	Practice whiteboard space-management skills.</li>
                    <li>❌	Remain quiet the whole time while coding.</li>
                    <li>❌	Spend too much time writing comments.</li>
                    <li>❌	Use extremely verbose or single-character (unless they're common like i, n) variable names.</li>
                    <li>❌	Copy and paste code without checking (e.g. variables need to be renamed).</li>
                    <li>❌	Interrupt your interviewer when they are talking. Usually if they speak, they are trying to give you hints or steer you in the right direction.</li>
                    <li>❌	Write too big (takes up too much space) or too small (illegible) if on a whiteboard.</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>After Coding:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>✅	Scan through your code for mistakes as if it was your first time seeing code written by someone else.</li>
                    <li>✅	Check for off-by-one errors.</li>
                    <li>✅	Come up with test cases. Try extreme test cases - empty sets, single item sets, negative numbers</li>
                    <li>✅	Step through your code with those test cases.</li>
                    <li>✅	Look out for places where you can refactor.</li>
                    <li>✅	Reiterate the time and space complexity of your code.</li>
                    <li>✅	Explain trade-offs and how the code/approach can be improved if given more time.</li>
                    <li>❌	Immediately announce that you are done coding. Do the above first!</li>
                    <li>❌	Argue with the interviewer. They may be wrong but that is very unlikely given that they are familiar with the question.</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Wrap UP:</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>✅	Ask questions. More importantly, ask good and engaging questions that are tailored to the company! Pick some questions from this list.</li>
                    <li>✅	Thank the interviewer.</li>
                    <li>✅	Record the interview questions and answers down as these can be useful for future reference.</li>
                    <li>❌	End the interview without asking any questions.</li>
                </ul>
               """,
               unsafe_allow_html=True)
    
if (user_input_prep=="General Technical Questions"):
    c = st.container()
    c.markdown("""---""")
    c.image("https://www.yoreoyster.com/wp-content/uploads/2021/06/LeetCode-Review.png")
    c.markdown("<h2 style='text-align: center; text-decoration: underline;'>The Blind 75 LeetCode Questions</h2>", unsafe_allow_html=True)
    c.markdown("<h4 style='text-align: center; font-style: italic;'>Go to <a href='https://leetcode.com/'>Leetcode</a> and solve these problems.</h4>", unsafe_allow_html=True)
    c.markdown("<h4 style='text-align: center; font-style: italic;'>Source: <a href='https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions'>Blind 75</a></h4>", unsafe_allow_html=True)
    c.markdown("<h3>Sequences</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>Two Sum</li>
                    <li>Contains Duplicate</li>
                    <li>Best Time to Buy and Sell Stock</li>
                    <li>Valid Anagram</li>
                    <li>Valid Parentheses</li>
                    <li>Maximum Subarra</li>
                    <li>Product of Array Except Self</li>
                    <li>3Sum</li>
                    <li>Merge Intervals</li>
                    <li>Group Anagrams</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Data Structures</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>Reverse a Linked List</li>
                    <li>Detect Cycle in a Linked List</li>
                    <li>Container With Most Water</li>
                    <li>Find Minimum in Rotated Sorted Array</li>
                    <li>Longest Repeating Character Replacement</li>
                    <li>Longest Substring Without Repeating Characters</li>
                    <li>Number of Islands</li>
                    <li>Remove Nth Node From End Of List</li>
                    <li>Palindromic Substrings</li>
                    <li>Pacific Atlantic Water Flow</li>
                    <li>Minimum Window Substring</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Non-linear Data Structures</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>Invert/Flip Binary Tree</li>
                    <li>Validate Binary Search Tree</li>
                    <li>Non-overlapping Intervals</li>
                    <li>Construct Binary Tree from Preorder and Inorder Traversal</li>
                    <li>Top K Frequent Elements</li>
                    <li>Clone Graph</li>
                    <li>Course Schedule</li>
                    <li>Serialize and Deserialize Binary Tree</li>
                    <li>Binary Tree Maximum Path Sum</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>More Data Structures</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>Subtree of Another Tree</li>
                    <li>Lowest Common Ancestor of BST</li>
                    <li>Implement Trie (Prefix Tree)</li>
                    <li>Add and Search Word</li>
                    <li>Kth Smallest Element in a BST</li>
                    <li>Merge K Sorted Lists</li>
                    <li>Find Median from Data Stream</li>
                    <li>Insert Interval</li>
                    <li>Longest Consecutive Sequence</li>
                    <li>Word Search II</li>
                </ul>
               """,
               unsafe_allow_html=True)
    c.markdown("<h3>Dynammic Programming</h3>", unsafe_allow_html=True)
    c.markdown("""
               <ul>
                    <li>Climbing Stairs</li>
                    <li>Coin Change</li>
                    <li>Longest Increasing Subsequence</li>
                    <li>Combination Sum</li>
                    <li>House Robber</li>
                    <li>House Robber II</li>
                    <li>Decode Ways</li>
                    <li>Unique Paths</li>
                    <li>Jump Game</li>
                    <li>Word Break</li>
                </ul>
               """,
               unsafe_allow_html=True)

### Sources
st.markdown("<h2 style='text-align: center;'>Sources</h2>", unsafe_allow_html=True)
col4, col5, col6=  st.columns(3)
with col4:
    st.image("https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/egfdbogz9ptr50dfinet")
    if st.button("NodeFlair"):
        webbrowser.open_new_tab("https://www.nodeflair.com/")            
with col5:
    st.image("https://icon-library.com/images/linkedin-icon-for-resume/linkedin-icon-for-resume-11.jpg")
    if st.button("LinkedIn"):
        webbrowser.open_new_tab("https://www.linkedin.com/") 
with col6:
    st.image("https://static-s.aa-cdn.net/img/ios/589698942/b124131d1f8676c078cd215d158321ba?v=1")
    if st.button("GlassDoor"):
        webbrowser.open_new_tab("https://www.glassdoor.sg/")
col7, col8, col9, col10, col11 = st.columns(5)
with col7:
    pass
with col7:
    pass
with col10:
    pass
with col11:
    pass
with col9:
    if st.button("Tech Interview Handbook"):
        webbrowser.open_new_tab("https://github.com/yangshun/tech-interview-handbook")

# footer
st.markdown("""---""")          
st.markdown("*By **Kai Seong**, **Shao Wei**, **Ci Hui** & **Horstann** for iNTUition 2022.*")