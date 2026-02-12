%%writefile app.py

# import streamlit as st
# from sentiment_model import predict_sentiment
# 
# st.set_page_config(
#     page_title="Swiggy Review Sentiment Analysis",
#     page_icon="🍔",
#     layout="centered"
# )
# 
# st.title("🍔 Swiggy Review Sentiment Analysis")
# st.write("Analyze customer reviews using NLP")
# 
# review = st.text_area("Enter a Swiggy Review")
# 
# if st.button("Analyze Sentiment"):
#     if review.strip() == "":
#         st.warning("Please enter a review")
#     else:
#         sentiment = predict_sentiment(review)
#         st.success(f"Sentiment: {sentiment}")
#
