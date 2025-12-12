import streamlit as st
from openai import OpenAI

# Get API credentials from Streamlit secrets (for Streamlit Cloud) or config.py (for local)
try:
    # Try Streamlit secrets first (for Streamlit Cloud deployment)
    if hasattr(st, "secrets") and "ROUTELLM" in st.secrets:
        API_KEY = st.secrets["ROUTELLM"]["API_KEY"]
        API_BASE_URL = st.secrets["ROUTELLM"]["API_BASE_URL"]
    else:
        raise KeyError("Secrets not found")
except (KeyError, AttributeError, FileNotFoundError):
    # Fall back to config.py for local development
    try:
        from config import API_KEY, API_BASE_URL
    except ImportError:
        st.error("⚠️ API configuration not found!")
        st.markdown("""
        ### For Streamlit Cloud:
        1. Go to your app settings on [share.streamlit.io](https://share.streamlit.io)
        2. Click on **"Secrets"** in the sidebar
        3. Add your secrets in TOML format:
        ```toml
        [ROUTELLM]
        API_KEY = "your_actual_api_key_here"
        API_BASE_URL = "https://routellm.abacus.ai/v1"
        ```
        4. Click **"Save"** and the app will automatically redeploy
        
        ### For Local Development:
        Create a `config.py` file with your API key.
        """)
        st.stop()

# Page configuration
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title and description
st.title("🤖 AI Chat Assistant")
st.markdown("Chat with an AI assistant powered by RouteLLM")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Create OpenAI client with custom base URL
                client = OpenAI(
                    api_key=API_KEY,
                    base_url=API_BASE_URL
                )
                
                # Prepare messages for API
                messages_for_api = [
                    {"role": msg["role"], "content": msg["content"]}
                    for msg in st.session_state.messages
                ]
                
                # Call RouteLLM API with Meta Llama model
                response = client.chat.completions.create(
                    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
                    messages=messages_for_api,
                    temperature=0.7,
                    max_tokens=500
                )
                
                # Get assistant response
                assistant_response = response.choices[0].message.content
                
                # Display assistant response
                st.markdown(assistant_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                
            except Exception as e:
                error_message = f"Error: {str(e)}"
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})

# Sidebar with options
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📝 Instructions")
    st.markdown("""
    1. Type your message in the chat input
    2. Press Enter or click Send
    3. The AI will respond to your message
    4. Continue the conversation naturally
    """)
    
    st.markdown("---")
    st.markdown("### 🔒 Security")
    st.info("Your API key is stored securely using Streamlit secrets (Cloud) or config.py (local) and is not shared in the repository.")

