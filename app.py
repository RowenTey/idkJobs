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
                    <li>Study and revise  relevant topics in that area.</li>
                    <li>Pratice technical questions with Leetcode/HackerRank.</li>
                    <li>Prepare for potential behavioral questions.</li>
                    <li>Craft your resume neatly.</li>
                    <li>Prepare a list of good questions to ask.</li>
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
###

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

# footer
st.markdown("""---""")          
st.markdown("*By **Kai Seong**, **Shao Wei**, **Ci Hui** & **Horstann** for iNTUition 2022.*")