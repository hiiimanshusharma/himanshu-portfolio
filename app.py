import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import os
import webbrowser
from pathlib import Path
from PIL import Image
import webbrowser
import urllib.request

st.set_page_config(page_title="Himanshu Sharma", page_icon="👨‍🔬")
# Create Header for Website
st.markdown("## Hi I'm **Himanshu** 👋", unsafe_allow_html=True)
st.markdown("*(2x BTSA Intern @ZS Associates | x Backend @VarsityPro)*", unsafe_allow_html=True)
st.info(
    """
Currently Technology Associate - Intern @ ZS Associates. 
Proficient in engineering stack like backend and data engineering & Data Science. 
During my internships at ZS Associates and VarsityPro, I delivered scalable backend solutions, optimized data pipelines, and leveraged Generative AI for impactful innovations.
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


# Create tabs
tab3, tab2, tab4, tab5, tab1 = st.tabs(["Experience", "Projects", 'SKills', "Resume","Overiew"])

# tab 2 examples
with tab2:
    projects_tabs = ["Backend Engineering", "Data Engineering", "Data Science"]
    BE_tab, DE_tab, DS_tab = st.tabs(projects_tabs)
    with BE_tab:
        st.markdown("#### Galaxy Search")
        with st.container():
            col1, col2 = st.columns([1, 5])

            with col1:
                st.markdown("[Github](https://github.com/hiiimanshusharma/Galaxy-Search)")
                st.markdown("`December 2024`")

            with col2:
                st.write("""
                - Developed Galaxy Search, a search engine for astronomy images, utilizing ElasticSearch for 40% faster data retrieval,
                - FastAPI for the backend, and Streamlit for an interactive frontend.
                - It allows seamless document insertion and search functionality. ElasticSearch is containerized using Docker.
                """)
            
        with st.container():
            st.markdown("#### Scheduled Product Scraper")
            col3, col4 = st.columns([1, 5])

            with col3:
                st.markdown("[Github](https://github.com/hiiimanshusharma/Django-Celery-Scraper)")
                st.markdown("`October 2024`")

            with col4:
                st.write("""
                - Developed a web scraper using Python, Selenium, and Django to automate product scraping at scheduled intervals, parsing data with BeautifulSoup and storing it in a Django database for ongoing analysis.    
                - Integrated Celery for asynchronous task scheduling, increasing scraping efficiency by 30%. Leveraged Redis for task queue management, ensuring smooth execution and enabling the scraper to adapt dynamically to changing website structures.
                """)
        
        with st.container():
            st.markdown("#### Task Management")
            col5, col6 = st.columns([1, 5])

            with col5:
                st.markdown("[Github](https://github.com/hiiimanshusharma/TaskManager)")
                st.markdown("`October 2023`")

            with col6:
                st.write("""
                - Developed a secure and documented Django Advanced API for task management, featuring user authentication and authorization, role-based access control, CRUD operations on tasks, and robust input validation.
                - Enhanced user experience with filtering, sorting, pagination, and search functionality for tasks while ensuring proper security measures such as CSRF protection and JWT-based authentication.
                - Implemented comprehensive testing, including unit tests, integration tests, and rate limiting to safeguard the API and prevent abuse.
                """)

    with DE_tab:
        with st.container():
            st.markdown("#### Github Data Stream")
            col1, col2 = st.columns([1, 5])

            with col1:
                st.markdown("[Github](https://github.com/hiiimanshusharma/weather-data-stream-with-kafka)")
                st.markdown("`November 2024`")

            with col2:
                st.write("""
                - It utilizes the GitHub Firehose, a live feed of JSON events, to create a real-time data pipeline.
                - Integrating Python, Kafka, and the Quick Streams library, it ensures efficient ingestion, processing, and streaming of GitHub events to enable actionable insights into open-source activities.
                """)
            
        with st.container():
            st.markdown("#### ELT Pipeline")
            col3, col4 = st.columns([1, 5])

            with col3:
                st.markdown("[Github](https://github.com/hiiimanshusharma/elt-pipeline-with-dbt)")
                st.markdown("`September 2024`")

            with col4:
                st.write("""
                - Built an end-to-end data pipeline leveraging Docker, Airflow, DBT, and SQL databases to automate data ingestion, transformation, and storage. The pipeline ensures scalability, consistency, and persistence, with containerized services and modular data transformations for real-world applications.
                - Automated workflows using Apache Airflw to orchestrate tasks and Kafka for real-time data streaming. Integrated cron jobs and Docker volumes for seamless scheduling and data persistence, ensuring timely and reliable updates for analytics and reporting.
                """)
        
    with DS_tab:
        tab2_names = ["Gen AI", "NLP", "Machine Learning", "Computer Vision"]
        GenAI_tab, tab2_3, tab2_2, tab2_1 = st.tabs(tab2_names)
        with GenAI_tab:
            with st.container():
                st.markdown("#### Handlo")
                col1, col2 = st.columns([1, 5])

                with col1:
                    st.markdown("[Github](https://github.com/hiiimanshusharma/weather-data-stream-with-kafka)")
                    st.markdown("`December 2024`")

                with col2:
                    st.write("""
                    - Developed an innovative hashtag suggestion feature within Handlo that generated 200+ context-specific hashtags daily using advanced tools like Qdrant and LlamaIndex to maximize social media reach for clients.
                    - Developed the HashtagRetriever tool leveraging Qdrant, LlamaIndex, and Hugging Face APIs to generate relevant hashtags based on minimal input; enhanced retrieval speed by 40% while improving user engagement metrics.
                    """)
                
            with st.container():
                st.markdown("#### Peer RAG")
                col3, col4 = st.columns([1, 5])

                with col3:
                    st.markdown("[Github](https://github.com/hiiimanshusharma/elt-pipeline-with-dbt)")
                    st.markdown("`November 2024`")

                with col4:
                    st.write("""
                    - PeerRAG is a RAG chatbot integrating LangChain, FAISS, and HuggingFaceEmbeddings for context-aware query handling using advanced NLP and vector search.
                    - Engineered a comprehensive employee dataset by scraping Peerlist using BeautifulSoup and FireCrawl; enhanced chatbot intelligence, enabling data retrieval for over 500 distinct employee profiles, improving response accuracy by 40%.
                    """)

        with tab2_1:
            col1, col2 = st.columns([1, 3])

            with col1:
                st.subheader("Face Detection Using MediaPipe")
                st.markdown("[Github](https://github.com/hiiimanshusharma/Face-Detection-Using-Mediapipe-Face_Alignment)")

            with col2:
                st.write("""
                This project involves utilizing an open-source face detection pipeline, such as 'face-alignment' or 'MediaPipe Face Detection,' to process a given video and identify faces within it. Following this detection process, the faces must be cropped and extracted from their original frames, ultimately creating a new video containing only the isolated faces. This final video, showcasing the detected faces, should then be saved as an output file, necessitating a proficient understanding of programming, video processing, and the chosen face detection library's APIs for successful implementation.

                [Mediapipe Link](https://github.com/google/mediapipe/blob/master/docs/solutions/face_detection.md)

                [Face Alignment Link](https://pypi.org/project/face-alignment/)
                """)

            col3, col4 = st.columns([1, 3])

            with col3:
                st.subheader("Open OCR")
                st.markdown("[Github](https://github.com/hiiimanshusharma/OpenOcr)")
                st.markdown("[Live](https://openocr-ef1r.onrender.com)")

            with col4:
                st.write("""
                Deployed a Website made in streamlit performs OCR using Google Cloud Vision API , performs Realtime OCR also provide feature to change formats of image among tiff, jpeg, png.

                Requirements:
                ```pip install -r requirements.txt```
                """)

            col5, col6 = st.columns([1, 3])

            with col5:
                st.subheader("McCain Product Recognition systematic")
                st.markdown("[Github](https://github.com/hiiimanshusharma/McCain-Product-Recognition)")
                st.markdown("[Roboflow](https://app.roboflow.com/himanshu-sharma-sbm0z/mccain/deploy/3)")

            with col6:
                st.write("""
                I designed and implemented a product recognition solution tailored specifically for identifying and categorizing a wide range of products within the McCain Brand. Leveraging advanced computer vision techniques and deep learning algorithms, this system can accurately analyze images and videos to recognize McCain products, distinguishing between different product variants and packaging designs. The solution provides valuable insights for inventory management, marketing, and quality control, enhancing the overall efficiency and performance of McCain's product operations.

                [Webcam Inference](https://www.loom.com/share/9f4c3a4b2d0241adbe727ef55fa5fb9c?sid=94c6fecf-94c3-4b75-887a-9985b1183e4c)

                [Youtube Inference](https://www.loom.com/share/82afa1672f1845288fc130e2a8f9db69?sid=59778160-5333-407e-ab31-16ddc0b79d84)
                """)
        with tab2_2:
            col1, col2 = st.columns([1, 3])

            with col1:
                st.subheader("Customer Churn Prediction")
                st.markdown("[Github](https://github.com/hiiimanshusharma/Customer_Churn_Prediction)")

            with col2:
                st.write("""
                I created a machine learning model to predict customer churn by analyzing historical customer data. After gathering and preprocessing the data, I selected and trained the best-performing model. This predictive tool empowers businesses to identify and target customers at risk of leaving, based on their past behavior and interactions. By deploying this model in a production environment, companies can proactively implement retention strategies, ultimately reducing customer churn and enhancing customer satisfaction and loyalty.
                """)
            col3, col4 = st.columns([1, 3])

            with col3:
                st.subheader("App Rating Prediction")
                st.markdown("[Github](https://github.com/hiiimanshusharma/appRatingPrediction)")

            with col4:
                st.write("""
                I created a system to predict app ratings, a task known for its complexity. My system is effective at estimating user reviews and ratings of mobile applications, both before and after their launch. It considers various factors that influence ratings, like user preferences, app features, design, and marketing efforts. This solution helps developers and businesses make informed decisions about improving apps, marketing strategies, and engaging users, ultimately contributing to the app's success.

                [Link to Dataset](https://www.kaggle.com/datasets/lava18/google-play-store-apps)
                """)

            col5, col6 = st.columns([1, 3])

            with col5:
                st.subheader("Terrain Classifier")
                st.markdown("[Github](https://github.com/hiiimanshusharma/terrain_classifier )")

            with col6:
                st.write("""
                I classified three distinct terrains, namely Desert, Mountain, and Plain, within three regions of India using LANDSAT-8 satellite imagery spanning from January 2014 to March 2022. By employing remote sensing techniques and machine learning algorithms, I processed the satellite data to differentiate and categorize these terrains accurately. This classification aids in various applications, including land use planning, environmental monitoring, and disaster management, enabling better understanding and management of India's diverse geographical landscapes.

                [Link to Dataset](https://drive.google.com/drive/folders/1qP8ceXoLhBKOV3f32j8c_6u3mkTGEzb-?usp=sharing)
                """)
        with tab2_3:
            col1, col2 = st.columns([1, 3])

            with col1:
                st.subheader("Falcon LLM based Question Answering bot")
                st.markdown("[Github](https://github.com/hiiimanshusharma/Falcon_QA_bot)")

            with col2:
                st.write("""
                I developed a question answering bot leveraging the Falcon LLM open source model, which is a powerful language model designed for natural language processing tasks. Additionally, I created an interactive Streamlit WebApp that utilizes this model for question answering. This user-friendly web application allows users to input questions, and the bot intelligently generates accurate responses based on its understanding of the context and language. This combined solution provides an accessible and efficient way for users to obtain answers to their inquiries.
                """)

# tab 1 overview
with tab1:
    with open("style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


    #####################
    # Header
    st.write(
        """
    # Himanshu Sharma
    """
    )
# Load the image
    image = './images/image.jpeg'

    # Display the image with desired width and alignment
    st.image(image, width=300)


    st.markdown("## Summary", unsafe_allow_html=True)
    st.info(
        """
    I am Final year student pursuing B.Tech CSE at IIIT Una. Proficient in modern frameworks like Django, FastAPI, and Flask, and skilled in cloud technologies like AWS and Kubernetes, I thrive on solving complex challenges. During my internships at ZS Associates and VarsityPro, I delivered scalable backend solutions, optimized data pipelines, and leveraged Generative AI for impactful innovations.
    """
    )

    #####################
    # Navigation

    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True,
    )



    

    #####################

    st.markdown(
        """
    ## Education
    """
    )

    txt(
        " *Indian Institute of Information Technology*, Una, Himachal Pradesh",
        "2021-Present",
    )
    st.markdown(
        """
    - B. Tech. - **Computer Science and Engineering**
    """
    )

    #####################
with tab4:
    with st.container():
        st.markdown(
            """
        ## Skills
        """
        )
        txt3("Programming Languages", "`C`, `C++`, `Python`, `R`")
        txt3("Frameworks", "`Flask`, `FastAPI`, `Streamlit`, `Gradio`, `Django`, `DRF`, `GraphQL`, `Celery`, `pytest`")
        txt3("Databases", "`MongoDB`, `Cassandra`, `Redis`, `SQL`, `PostgreSQL`, `Qdrant`, `ChromaDB`, `Weaviate`")
        txt3("DevOps", "`Docker`, `Kubernetes`, `Git`")
        txt3("Data Engineering", "`Snowflake`, `Apache Kafka`, `Databricks`, `AWS Glue`, `PySpark`, `DBT`, `Airbyte`, `Airflow`, `MetaBase`")


# Experience
with tab3:
    with st.container():
        st.markdown("#### Bussiness Technology Solutions Associate (BTSA) - Intern @ ZS Associates")
        col1, col2 = st.columns([1, 4])

        with col1:
            st.markdown("`January 2025` - `Present`")
            st.markdown("Pune, Maharashtra")

        with col2:
            st.write("""
            Enhancing the backend and data pipelines of a Drug Resource Planning platform for pharmaceutical companies, optimizing resource management.
            """)

    with st.container():
        st.markdown("#### Backend Enginnering Intern @ VarsityPro")
        col3, col4 = st.columns([1, 4])
        with col3:
            st.markdown("`July 2024` - `December 2024`")
            st.markdown("New Delhi (Remote)")

        with col4:
            st.write("""
            Developed the backend for 4+ platforms, including a Career Accelerator, Alumni Network, Placement Cell & Campus Recruiter Connection, and Coworking Space Management, using Django REST Framework (DRF).
            
            Implemented Django Celery to efficiently execute tasks like code evaluation for a coding platform and AI-driven resume scoring and interview preparation.
            """)
    
    with st.container():
        st.markdown("#### Bussiness Technology Solutions Associate (BTSA) - Intern @ ZS Associates")
        col7, col8 = st.columns([1, 4])

        with col7:
            st.markdown("`Febuary 2024` - `June 2024`")
            st.markdown("Pune, Maharashtra")
            

        with col8:
            st.write("""
            Contributed to the development of a data processing pipeline leveraging Generative AI to streamline data management for pharmaceutical companies. Played a key role in designing a data crawler that integrated data from 4+ sources, including Databricks, S3, Snowflake, and Redshift, improving the efficiency of the ingestion process.
            
            Re-architected the project from MVP to business-ready state, ensuring scalability and usability.
            
            Contributed to ZS's multi-layered Data Warehousing pipeline (ingestion, acquisition, and warehousing), upgraded Airflow DAGs to the latest version, and integrated Generative AI solutions for DQM checks in the ingestion layer.
            """)

    with st.container():
        st.markdown("#### Python Developer - Intern @ Culida Inc.")
        col5, col6 = st.columns([1, 4])

        with col5:
            st.markdown("`January 2024`")
            st.markdown("Hyderabad, Telangana (Remote)")
            

        with col6:
            st.write("""
            Collabrated for building Cyber Security RAG using Weaviate DB. Integrated scraping script to database using MYSQLConnection manager
            """)


with tab5:
    be_resume = "./resume/HimanshuResume-BE.pdf"
    de_resume = "./resume/HimanshuResume-DE.pdf"
    ds_resume = "./resume/HimanshuResume-DS.pdf"
    with st.expander("Backend Engineering Resume"):
        if os.path.exists(be_resume):
            pdf_viewer(f"{be_resume}")
        else:
            st.error("PDF file not found!")
        st.markdown("[Download PDF](https://drive.google.com/file/d/1xIggFIE6R0a7hRo-kejCf8R8Q779mtjO/view?usp=sharing)")

    with st.expander("Data Engineering Resume"):
        if os.path.exists(de_resume):
            pdf_viewer(f"{de_resume}")
        else:
            st.error("PDF file not found!")
        st.markdown("[Download PDF](https://drive.google.com/file/d/13SIciBWMy9UPN2ouOkmrqWrHmJifSOMz/view?usp=sharing)")
    
    with st.expander("Data Science Resume"):
        if os.path.exists(ds_resume):
            pdf_viewer(f"{ds_resume}")
        else:
            st.error("PDF file not found!")
        st.markdown("[Download PDF](https://drive.google.com/file/d/1pFe2T2PHMHu4NY-4tIorTVgGlQ9OBtrx/view?usp=sharing)")

#####################
with st.container():
    st.divider()
    st.markdown(""" <h3 style="text-align:center;">Get In Touch ✉️</h3>""", unsafe_allow_html=True)
    st.markdown(""" <p style="text-align:center;">
        Reach out to me: <a href="mailto:himanushubasotiya10@gmail.com" style="text-decoration:underline; color: black;">himanushubasotiya10@gmail.com</a>, also social profiles for more details.
        </p>
        """, unsafe_allow_html=True)
    _ ,_, col1, col2, col3, col4, _, _ = st.columns([1]*8)
    with col1:
        st.markdown("[LinkedIn](https://www.linkedin.com/in/himanshu-sharma-b0716b162/)")
    with col2:
        st.markdown("[GitHub](https://github.com/hiiimanshusharma)")
    with col3:
        st.markdown("[Instagram](https://www.instagram.com/hiiimanshu_sharma/)")
    with col4:
        st.markdown("[Twitter](https://twitter.com/h__sharma)")

