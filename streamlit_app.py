import streamlit as st
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Ag Chat",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 1rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: flex-start;
    }
    
    .user-message {
        background-color: #2e2e2e;
        margin-left: 2rem;
    }
    
    .bot-message {
        background-color: #2e2e2e;
        margin-right: 2rem;
    }
    
    .message-time {
        font-size: 0.7rem;
        color: #666;
        margin-top: 0.5rem;
    }
    
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 2px solid #e0e0e0;
    }
    
    .stButton > button {
        border-radius: 25px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #5a6fd8 0%, #6a4190 100%);
    }
</style>
""", unsafe_allow_html=True)

# Hardcoded responses for the chatbot
BOT_RESPONSES = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm doing well, thanks for asking!",
    "what can you do": "I'm a simple chatbot. I can respond to basic greetings and questions.",
    "help": "I'm here to help! Just type your message and I'll respond.",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
    "default": "I'm a simple chatbot. I can respond to basic greetings and questions."
}

def get_bot_response(user_input):
    """Get bot response based on user input"""
    user_input_lower = user_input.lower().strip()
    
    # Simple keyword matching
    if any(word in user_input_lower for word in ["hello", "hi", "hey"]):
        return BOT_RESPONSES["hello"]
    elif "how are you" in user_input_lower:
        return BOT_RESPONSES["how are you"]
    elif "what can you do" in user_input_lower or "help" in user_input_lower:
        return BOT_RESPONSES["what can you do"]
    elif any(word in user_input_lower for word in ["bye", "goodbye"]):
        return BOT_RESPONSES["bye"]
    elif any(word in user_input_lower for word in ["thanks", "thank you"]):
        return BOT_RESPONSES["thanks"]
    else:
        return BOT_RESPONSES["default"]

def main():
    # Header
    st.markdown('<h1 class="main-header">🌱 AgChat</h1>', unsafe_allow_html=True)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(f"""
                <div class="chat-message {'user-message' if message['role'] == 'user' else 'bot-message'}">
                    <div>
                        <strong>{'You' if message['role'] == 'user' else 'ChatBot'}</strong>
                        <p>{message['content']}</p>
                        <div class="message-time">{message['timestamp']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat history
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.messages.append({
            "role": "user", 
            "content": prompt, 
            "timestamp": timestamp
        })
        
        # Get bot response
        bot_response = get_bot_response(prompt)
        
        # Add bot response to chat history
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.messages.append({
            "role": "assistant", 
            "content": bot_response, 
            "timestamp": timestamp
        })
        
        # Rerun to display new messages
        st.rerun()
    
    # Sidebar with information
    with st.sidebar:
        st.markdown("## 💡 Chat Tips")
        st.markdown("""
        Try asking me:
        - "Hello" or "Hi"
        - "How are you?"
        - "What can you do?"
        - "Help"
        - "Bye"
        """)
        
        st.markdown("---")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main() 
