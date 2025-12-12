# 🤖 Streamlit AI Chat Application

A beautiful and interactive AI chat application built with Streamlit and RouteLLM (Abacus AI).

## Features

- 💬 Interactive chat interface
- 🤖 Powered by RouteLLM API
- 🔒 Secure API key management
- 🎨 Modern and clean UI
- 📱 Responsive design

## Prerequisites

- Python 3.8 or higher
- RouteLLM API key from Abacus AI

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd streamlit_AI_Chat
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key (Local Development)**
   
   **Option A: Using config.py (Recommended for local)**
   - Copy `config.example.py` to `config.py`
   - Replace `YOUR_API_KEY_HERE` with your actual RouteLLM API key
   - The API endpoint is already configured: `https://routellm.abacus.ai/v1`
   - Save the file

   **Option B: Using Streamlit secrets (Alternative for local)**
   - Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
   - Replace `YOUR_API_KEY_HERE` with your actual RouteLLM API key
   - Save the file

   **Important:** Both `config.py` and `.streamlit/secrets.toml` are in `.gitignore`, so your API key won't be committed to GitHub.

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Deployment to Streamlit Cloud

Deploy your app to [share.streamlit.io](https://share.streamlit.io) for free!

### Steps:

1. **Push your code to GitHub**
   - Make sure `config.py` is NOT committed (it's in `.gitignore`)
   - Only commit: `app.py`, `config.example.py`, `requirements.txt`, `.gitignore`, `README.md`

2. **Connect to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository and branch
   - Set the main file path to: `app.py`

3. **Add your API key as a Secret**
   - In the Streamlit Cloud dashboard, go to your app settings
   - Click on "Secrets" in the sidebar
   - Add your secrets in TOML format:
     ```toml
     [ROUTELLM]
     API_KEY = "your_actual_api_key_here"
     API_BASE_URL = "https://routellm.abacus.ai/v1"
     ```
   - Click "Save"

4. **Deploy!**
   - Click "Deploy" and your app will be live at `https://your-app-name.streamlit.app`

**Note:** The app automatically uses Streamlit secrets when deployed to Streamlit Cloud, and falls back to `config.py` for local development.

## Project Structure

```
streamlit_AI_Chat/
├── app.py                      # Main Streamlit application
├── config.py                   # API key configuration (not tracked by git)
├── config.example.py           # API key template (safe to commit)
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore file
├── README.md                  # Project documentation
└── .streamlit/
    └── secrets.toml.example    # Streamlit secrets template (safe to commit)
```

## Security Notes

- ⚠️ **Never commit `config.py` to version control**
- ✅ The `config.py` file is already included in `.gitignore`
- 🔐 Keep your API key secure and don't share it publicly
- 💡 Consider using environment variables for production deployments

## Customization

You can customize the application by:

- Changing the model in `app.py` (e.g., `gpt-4`, `gpt-3.5-turbo`)
- Adjusting `temperature` and `max_tokens` parameters
- Modifying the UI theme and layout
- Adding additional features like chat history persistence

## Troubleshooting

**Error: API key not found**
- Make sure you've added your API key to `config.py`
- Verify the API key is correct and has sufficient credits

**Error: Module not found**
- Make sure you've installed all dependencies: `pip install -r requirements.txt`
- Verify your virtual environment is activated

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome!

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [RouteLLM from Abacus AI](https://routellm.abacus.ai/)

