# HealthCare_Chatbot

This is a Streamlit-based chatbot application designed to provide mental health support to users by analyzing their Facebook & Twitter comments/activity and offering appropriate responses.

Features
Data Preprocessing: Fetched Twitter data is preprocessed using a preprocessing pipeline to prepare it for analysis.
Semantic Analysis: Perform semantic analysis on user input to identify mental health entities, topics, and sentiment.
Response Generation: Generate responses tailored to the user's mental health state using a response generator.
Topic Modeling: Conduct topic modeling on user input to identify key topics of discussion.
Chat History: Maintain a chat history for each user session to keep track of conversations.
Setup
Clone this repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Run the Streamlit app by executing streamlit run main.py.
Access the app through the provided URL.
Usage
Type your messages in the text area labeled "You:" and click the "Send" button to interact with the chatbot.
The chatbot will analyze your input, generate responses, and display them in the chat interface.
You can view identified mental health entities, topics, sentiment, and topic modeling results in the chat interface.
The chatbot will provide appropriate responses and suggestions based on your current mental health state.

