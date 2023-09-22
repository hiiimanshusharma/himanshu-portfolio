# imports
import streamlit as st
import os
import webbrowser
from pathlib import Path
from PIL import Image
import webbrowser
import urllib.request

st.set_page_config(page_title="Himanshu Sharma's portfolio", page_icon="👨‍🔬")
# Create Header for Website
st.markdown("Himanshu Sharma's Portfolio")

# Create tabs
tab2, tab3, tab1 = st.tabs(["Projects", "Experience", "Overiew"])

# tab 2 examples
with tab2:
    tab2_names = ["Computer Vision", "Machine Learning", "Natural Language Processing"]
    tab2_1, tab2_2, tab2_3 = st.tabs(tab2_names)

    st.write("-------------------------------------------------------------------------------------------------------")
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
    I am Himanshu Sharma, currently pursuing a B.Tech in Computer Science and Engineering at the Indian Institute of Information Technology, Una. My educational background includes a strong foundation in programming languages like C/C++, Python, and R, along with web technologies, frameworks like Django, and cloud technology like AWS. My diverse skill set extends to machine learning, computer vision, financial analysis, and web scraping. I've also gained hands-on experience as a Quantitative Trading Analyst, and I've worked on various projects in areas such as question-answering bots, product recognition, OCR, and terrain classification. My commitment to continuous learning is reflected in my certifications in R and IoT.
    """
    )

    #####################
    # Navigation

    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True,
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

    st.markdown(
        """
    ## Skills
    """
    )
    txt3("Programming", "`Python`,`C`, `C++`, `R`, `GIT`, `Linux`")
    txt3("Data processing/wrangling", "`SQL`, `pandas`, `numpy`")
    txt3("Data visualization", "`matplotlib`, `seaborn`, `plotly`")
    txt3("Developer Tools", "`GIT`,`Docker`, `Google-Colab`, `Labelme`, `Anaconda`, `RStudio`")
    txt3("Deep Learning", "`TensorFlow`")
    txt3("Web development", "`Streamlit`, `Django`, `HTML`, `CSS`")
    txt3("Databases", "`MySQL`, `RDS`, `S3`")
    txt3("Cloud Technology", "`AWS`")

    #####################
    st.markdown(
        """
    ## Social Media
    """
    )
    txt2("LinkedIn", "https://www.linkedin.com/in/himanshu-sharma-b0716b162/")
    txt2("GitHub", "https://github.com/hiiimanshusharma")
    txt2("Instagram", "https://www.instagram.com/hiiimanshu_sharma/")
    txt2("Twitter", "https://twitter.com/h__sharma")





# tab 3 music

with tab3:
    tab3_names = ["Quantitative Trading Analyst Intern", "Machine Learning Intern"]
    tab3_1, tab3_2 = st.tabs(tab3_names)

    st.write("-------------------------------------------------------------------------------------------------------")
    with tab3_1:
        st.markdown("#### Quantitative Trading Analyst for Tanmay Agarwal(Market Researcher)")
        st.markdown("#### From `June 2023` To `July 2023`")
        highlighted_text = """
        <div style="background-color: rgba(169, 169, 169, 0.7); padding: 20px; border-radius: 10px; color: black; text-align: left; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <p style="font-size: 16px; font-weight: bold;">As a Quantitative Trading analyst, I was responsible for fetching Trading data from NSE's website. I’ve also built strategies for trading and also fetched delivery volume of each company from NSE. I’ve fetched data of every country’s major indices.</p></div>
        """

        # Display the highlighted text in the Streamlit app
        st.markdown(highlighted_text, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])

        with col1:
            st.subheader("Trading Strategy")
            st.markdown("[Github](https://github.com/hiiimanshusharma/Trading_strategy)")

        with col2:
            st.write("""
            This trading strategy involves two simple rules based on daily historical data of the Bank Nifty stock index from 2007 to 2023:
            1. Long Entry (Buy Signal): Buy the Bank Nifty if the current day's high is 0.5% or more higher than the previous day's closing price.
            2. Short Entry (Sell Signal): Sell the Bank Nifty short if the current day's low is 0.5% or more lower than the previous day's closing price.
            These rules guide trading decisions: buying when there's upward momentum and selling short when there's downward momentum, aiming to profit from short-term price movements.

            """)
        col3, col4 = st.columns([1, 3])

        with col3:
            st.subheader("Delivery Quantities")
            st.markdown("[Github](https://github.com/hiiimanshusharma/Delivery-Quantities)")

        with col4:
            st.write("""
            Obtaining daily delivery volume data for all stocks listed on the National Stock Exchange (NSE) from 2000 to 2023 is a complex and data-intensive task that necessitates access to comprehensive historical market data.

            Used [nsedt python package](https://pypi.org/project/nsedt/) for retrieval of data.
            """)

        image1 = Image.open('./images/tanmayAgarwal.jpg')

        st.write("-------------------------------------------------------------------------------------------------------")
        st.write("#### About Employer")
        st.image(image1, caption='Tanmay Agarwal')
        st.write("""He is a qualified Chartered Accountant and in full-time markets for the last 5 years, managing funds of over 20 crores. He is a full time systematic trader for the last 7 years. He is into hardcore research of market data to find profitable systems through python. """)
    with tab3_2:
        st.markdown("#### Machine Learning Intern @ Feynn Labs")
        st.markdown("#### From `June 2023` To  `August 2023`")
        highlighted_text = """
        <div style="background-color: rgba(169, 169, 169, 0.7); padding: 20px; border-radius: 10px; color: black; text-align: left; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <p style="font-size: 16px; font-weight: bold;">My responsibilities were focused on leveraging machine learning techniques to create innovative AI products and services. Interns will engage in tasks such as prototyping AI solutions, utilizing machine learning algorithms for market segmentation within specific domains, developing financial models for AI prototypes, and formulating practical business models. They will be assigned to primary projects including AI product prototyping, large-scale market segmentation, analogy bot generation, and AI prototype development, along with secondary projects such as adaptive question systems, product segmentation using machine learning, and macro-economic analysis and forecasting.
</p></div>
        """

        # Display the highlighted text in the Streamlit app
        st.markdown(highlighted_text, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])

        with col1:
            st.subheader("Online Vehicle booking Market segmentation")
            st.markdown("[Github](https://github.com/hiiimanshusharma/CabBooking)")

        with col2:
            st.write("""
            For our online cab booking market analysis project, we collected a dataset focused on customer reviews and ratings, conducted exploratory data analysis, applied clustering and classification techniques to gain insights, and documented the entire process in a report. I also created a dedicated GitHub repository to share my work with the team, demonstrating our commitment to the project's success and individual efforts in contributing to data-driven decision-making.

            """)
        col3, col4 = st.columns([1, 3])

        with col3:
            st.subheader("LyricSpark")
            st.markdown("[Github](https://github.com/hiiimanshusharma/LyricSpark)")

        with col4:
            st.write("""
            The manual generation of song lyrics is time-consuming and requires extensive creativity. Existing automated approaches lack depth, producing generic and uninspiring lyrics. They rely on simplistic patterns or statistical models that fail to capture human xpression, resulting in mechanical compositions. Moreover, current systems struggle to adapt to different genres, moods, and themes. A solution is needed—a sophisticated automated system that combines machine learning, natural language processing, and creative algorithms to generate high-quality lyrics. It should understand diverse musical genres, adapt to various emotions and themes, and offer a user-friendly interface for customization. This solution would revolutionize songwriting, streamlining the process, inspiring artists, and producing captivating lyrics that resonate deeply with listeners.

            """)



        image5 = Image.open('./images/feynnLabs.jpg')
        # image6 = Image.open('./images/seasonality_trends.png')
        st.write("#### About Employer")
        st.image(image5)
        st.write("""Feynn Labs is an Artificial Intelligence company currently focusing on AI integration in Small/Medium Businesses and providing high quality education in AI/Machine Learning. Our goal is to build premier chain of institutes in India where students will apply  and experiment with what they learn hand in hand, with our  “Project based Top-Down Learning” approach focusing  in frontier technologies like  Artificial Intelligence, Crypto-currency, Quantum Computing, Augmented Reality etc.""")
