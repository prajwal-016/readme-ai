# AI Software README Generator

A modern, full-stack web application designed for academic project submission. This tool leverages **Google Gemini AI** to automatically generate professional `README.md` files based on user-provided project details.

## ✨ Features

- **AI Integration**: Powered by Google Gemini Pro for intelligent content generation.
- **Premium UI**: Glassmorphism design with animated gradient backgrounds.
- **Markdown Preview**: Real-time rendering of generated README content.
- **Database Support**: Persistent storage of generated records using SQLite.
- **Utility Tools**: One-click "Copy to Clipboard" and "Download README.md" functionality.
- **Theme Support**: Dark/Light mode toggle for enhanced user experience.
- **Responsive Design**: Fully functional on mobile and desktop devices.

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **ORM**: Flask-SQLAlchemy
- **AI**: Google Generative AI (Gemini Pro)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Glassmorphism, CSS Variables, FontAwesome
- **Markdown Rendering**: Marked.js

## 🚀 Setup Instructions

1. **Prerequisites**:
   Ensure you have Python installed on your system.
   
2. **Install Dependencies**:
   ```bash
   pip install flask flask-sqlalchemy google-generativeai
   ```

3. **API Key Configuration**:
   The application is already configured with a Gemini API key. If you wish to change it, update the `GEMINI_API_KEY` variable in `app.py`.

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access**:
   Open your browser and navigate to `http://127.0.0.1:5000`

## 📁 Folder Structure

```
readme_generator/
│
├── app.py              # Flask server & Gemini integration
├── templates/          # HTML templates
│   ├── index.html      # Landing page
│   ├── form.html       # Input details
│   └── result.html     # README preview
│
├── static/             # Static assets
│   ├── css/style.css   # Premium styling
│   └── js/script.js    # Frontend logic
│
├── database.db         # SQLite storage (auto-generated)
└── README.md           # Project documentation
```

## 👨‍🎓 Author
- **Project**: Academic Mini-Project Submission
- **Year**: 2024
