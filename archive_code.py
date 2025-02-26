#     tab3_names = ["Quantitative Trading Analyst Intern", "Machine Learning Intern"]
#     tab3_1, tab3_2 = st.tabs(tab3_names)

#     st.write("-------------------------------------------------------------------------------------------------------")
#     with tab3_1:
#         st.markdown("#### Quantitative Trading Analyst for Tanmay Agarwal(Market Researcher)")
#         st.markdown("#### From `June 2023` To `July 2023`")
#         highlighted_text = """
#         <div style="background-color: rgba(169, 169, 169, 0.7); padding: 20px; border-radius: 10px; color: black; text-align: left; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
#             <p style="font-size: 16px; font-weight: bold;">As a Quantitative Trading analyst, I was responsible for fetching Trading data from NSE's website. I’ve also built strategies for trading and also fetched delivery volume of each company from NSE. I’ve fetched data of every country’s major indices.</p></div>
#         """

#         # Display the highlighted text in the Streamlit app
#         st.markdown(highlighted_text, unsafe_allow_html=True)

#         col1, col2 = st.columns([1, 3])

#         with col1:
#             st.subheader("Trading Strategy")
#             st.markdown("[Github](https://github.com/hiiimanshusharma/Trading_strategy)")

#         with col2:
#             st.write("""
#             This trading strategy involves two simple rules based on daily historical data of the Bank Nifty stock index from 2007 to 2023:
#             1. Long Entry (Buy Signal): Buy the Bank Nifty if the current day's high is 0.5% or more higher than the previous day's closing price.
#             2. Short Entry (Sell Signal): Sell the Bank Nifty short if the current day's low is 0.5% or more lower than the previous day's closing price.
#             These rules guide trading decisions: buying when there's upward momentum and selling short when there's downward momentum, aiming to profit from short-term price movements.

#             """)
#         col3, col4 = st.columns([1, 3])

#         with col3:
#             st.subheader("Delivery Quantities")
#             st.markdown("[Github](https://github.com/hiiimanshusharma/Delivery-Quantities)")

#         with col4:
#             st.write("""
#             Obtaining daily delivery volume data for all stocks listed on the National Stock Exchange (NSE) from 2000 to 2023 is a complex and data-intensive task that necessitates access to comprehensive historical market data.

#             Used [nsedt python package](https://pypi.org/project/nsedt/) for retrieval of data.
#             """)

#         image1 = Image.open('./images/tanmayAgarwal.jpg')

#         st.write("-------------------------------------------------------------------------------------------------------")
#         st.write("#### About Employer")
#         st.image(image1, caption='Tanmay Agarwal')
#         st.write("""He is a qualified Chartered Accountant and in full-time markets for the last 5 years, managing funds of over 20 crores. He is a full time systematic trader for the last 7 years. He is into hardcore research of market data to find profitable systems through python. """)
#     with tab3_2:
#         st.markdown("#### Machine Learning Intern @ Feynn Labs")
#         st.markdown("#### From `June 2023` To  `August 2023`")
#         highlighted_text = """
#         <div style="background-color: rgba(169, 169, 169, 0.7); padding: 20px; border-radius: 10px; color: black; text-align: left; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
#             <p style="font-size: 16px; font-weight: bold;">My responsibilities were focused on leveraging machine learning techniques to create innovative AI products and services. Interns will engage in tasks such as prototyping AI solutions, utilizing machine learning algorithms for market segmentation within specific domains, developing financial models for AI prototypes, and formulating practical business models. They will be assigned to primary projects including AI product prototyping, large-scale market segmentation, analogy bot generation, and AI prototype development, along with secondary projects such as adaptive question systems, product segmentation using machine learning, and macro-economic analysis and forecasting.
# </p></div>
#         """

#         # Display the highlighted text in the Streamlit app
#         st.markdown(highlighted_text, unsafe_allow_html=True)

#         col1, col2 = st.columns([1, 3])

#         with col1:
#             st.subheader("Online Vehicle booking Market segmentation")
#             st.markdown("[Github](https://github.com/hiiimanshusharma/CabBooking)")

#         with col2:
#             st.write("""
#             For our online cab booking market analysis project, we collected a dataset focused on customer reviews and ratings, conducted exploratory data analysis, applied clustering and classification techniques to gain insights, and documented the entire process in a report. I also created a dedicated GitHub repository to share my work with the team, demonstrating our commitment to the project's success and individual efforts in contributing to data-driven decision-making.

#             """)
#         col3, col4 = st.columns([1, 3])

#         with col3:
#             st.subheader("LyricSpark")
#             st.markdown("[Github](https://github.com/hiiimanshusharma/LyricSpark)")

#         with col4:
#             st.write("""
#             The manual generation of song lyrics is time-consuming and requires extensive creativity. Existing automated approaches lack depth, producing generic and uninspiring lyrics. They rely on simplistic patterns or statistical models that fail to capture human xpression, resulting in mechanical compositions. Moreover, current systems struggle to adapt to different genres, moods, and themes. A solution is needed—a sophisticated automated system that combines machine learning, natural language processing, and creative algorithms to generate high-quality lyrics. It should understand diverse musical genres, adapt to various emotions and themes, and offer a user-friendly interface for customization. This solution would revolutionize songwriting, streamlining the process, inspiring artists, and producing captivating lyrics that resonate deeply with listeners.

#             """)



#         image5 = Image.open('./images/feynnLabs.jpg')
#         # image6 = Image.open('./images/seasonality_trends.png')
#         st.write("#### About Employer")
#         st.image(image5)
#         st.write("""Feynn Labs is an Artificial Intelligence company currently focusing on AI integration in Small/Medium Businesses and providing high quality education in AI/Machine Learning. Our goal is to build premier chain of institutes in India where students will apply  and experiment with what they learn hand in hand, with our  “Project based Top-Down Learning” approach focusing  in frontier technologies like  Artificial Intelligence, Crypto-currency, Quantum Computing, Augmented Reality etc.""")