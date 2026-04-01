# 🚀 LLM Apps with Chainlit

A modern conversational AI application built with Chainlit and OpenAI's language models. This project demonstrates how to create interactive LLM-powered applications with a clean and intuitive chat interface.

## 📺 Walkthrough Video



https://github.com/user-attachments/assets/04a4a829-c313-4178-806c-843a026f72ae



> **Note:** Replace `YOUR_VIDEO_LINK_HERE` with your actual YouTube video link

## ✨ Features

- 🤖 **Conversational AI** - Interactive chat interface powered by OpenAI
- 💬 **Real-time Responses** - Instant message processing and replies
- 🎨 **Modern UI** - Clean and intuitive Chainlit interface
- 📝 **Message History** - Maintains conversation context
- 🔧 **Extensible** - Easy to customize and extend functionality

## 🛠️ Tech Stack

- **[Chainlit](https://chainlit.io/)** - Conversational AI framework
- **[OpenAI API](https://openai.com/)** - Language model integration
- **Python 3.8+** - Core programming language
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- An OpenAI API key

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/LLM-Apps-with-Chainlit.git
cd LLM-Apps-with-Chainlit
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp _env .env
```

Edit the `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=your_actual_openai_api_key_here
```

> ⚠️ **Important:** Never commit your `.env` file to version control. It's already included in `.gitignore`.

### 5. Run the Application

```bash
chainlit run app.py -w
```

The application will start and open in your default browser at `http://localhost:8000`

## 📁 Project Structure

```
LLM-Apps-with-Chainlit/
│
├── app.py                 # Main application file
├── chainlit.md           # Welcome screen content
├── requirements.txt      # Python dependencies
├── setup.py             # Package setup configuration
├── _env                 # Environment variables template
├── _gitignore          # Git ignore rules
├── LICENSE             # MIT License
├── README.md           # This file
│
└── src/
    └── llm.py          # LLM logic and message handling
```

## 💡 Usage

1. Start the application using the command above
2. Open your browser and navigate to `http://localhost:8000`
3. Start chatting with the AI assistant
4. The conversation context is maintained throughout the session

## 🔧 Customization

### Modify Welcome Screen

Edit the `chainlit.md` file to customize the welcome message that users see when they first open the application.

### Adjust LLM Behavior

Modify the `src/llm.py` file to:
- Change the AI model
- Adjust temperature and other parameters
- Add custom prompts or system messages
- Implement specialized functionality

### Styling

Chainlit supports custom theming. Create a `.chainlit/config.toml` file to customize colors, fonts, and other UI elements.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Chainlit](https://chainlit.io/) for the amazing conversational AI framework
- [OpenAI](https://openai.com/) for providing powerful language models
- All contributors who help improve this project


⭐ **If you find this project useful, please consider giving it a star!** ⭐

Made with ❤️ by Harshit
