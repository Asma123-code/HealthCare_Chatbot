import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_mic_recorder import speech_to_text
from model_pipeline import ModelPipeLine

from gtts import gTTS
from io import BytesIO

mdl = ModelPipeLine()
final_chain = mdl.create_final_chain()

st.set_page_config(page_title="PeacePal")

st.title('PeacePal')

## generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm your Mental health Assistant, How may I help you?"]
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

# Layout of input/response containers

colored_header(label='', description='', color_name='blue-30')
response_container = st.container()
input_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

def generate_response(prompt):
    response = mdl.call_conversational_rag(prompt,final_chain)
    return response['answer']

def text_to_speech(text):
    # Use gTTS to convert text to speech
    tts = gTTS(text=text, lang='en')
    # Save the speech as bytes in memory
    fp = BytesIO()
    tts.write_to_fp(fp)
    return fp

def speech_recognition_callback():
    # Ensure that speech output is available
    if st.session_state.my_stt_output is None:
        st.session_state.p01_error_message = "Please record your response again."
        return
    
    # Clear any previous error messages
    st.session_state.p01_error_message = None
        
    # Store the speech output in the session state
    st.session_state.speech_input = st.session_state.my_stt_output


## Applying the user input box        

    # Add a radio button to choose input mode
query = None
input_mode = st.sidebar.radio("Select input mode:", ["Text", "Speech"])

if input_mode == "Speech":
    # Use the speech_to_text function to capture speech input
    speech_input = speech_to_text(
        key='my_stt', 
        callback=speech_recognition_callback
    )

    # Check if speech input is available
    if 'speech_input' in st.session_state and st.session_state.speech_input:
        # Display the speech input
        st.text(f"Speech Input: {st.session_state.speech_input}")
        
        # Process the speech input as a query
        query = st.session_state.speech_input
        st.session_state.speech_input = None
        
else:
    # Add a text input field for query
    query = st.text_input("Query: ", key="input")
with input_container:
        # Process the query if it's not empty
    if query:
        with st.spinner("typing....."):
            response = generate_response(query)
            st.session_state.past.append(query)
            st.session_state.generated.append(response)
            
            # Convert the response to speech
            speech_fp = text_to_speech(response)
            # Play the speech
            st.audio(speech_fp, format='audio/mp3')

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
