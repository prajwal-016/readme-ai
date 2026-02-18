import os
import datetime
from flask import Flask, render_template, request, jsonify, send_file, Response
from flask_sqlalchemy import SQLAlchemy
import google.generativeai as genai
import io
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'supersecretkey')

db = SQLAlchemy(app)

# Gemini AI Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def get_model():
    # Final verified working list for this API key
    preferred = [
        'gemini-flash-latest',  # Verified SUCCESS
        'gemini-pro-latest',    # Stable fallback
        'gemini-1.5-flash', 
        'gemini-2.0-flash'
    ]
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        print(f"Available models: {available_models}")
        
        for p in preferred:
            model_name = f"models/{p}" if not p.startswith("models/") else p
            if model_name in available_models:
                print(f"Using model: {model_name}")
                return genai.GenerativeModel(p)
    except Exception as e:
        print(f"Error checking models: {e}")
    
    # Absolute fallback
    return genai.GenerativeModel('gemini-1.5-flash')

model = get_model()

def generate_mock_readme(data):
    """Fallback generator in case of API Quota failure"""
    return f"""# {data['project_name']}

## Description
{data['description']}

## Key Features
{data['features']}

## Installation
{data['installation']}

## Usage
{data['usage']}

## Technology Stack
{data['tech_stack']}

## Author
{data['author']}

---
*Note: This README was generated using the system's fallback template due to AI Quota limits.*
"""

# Database Model
class ReadmeRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    features = db.Column(db.Text, nullable=True)
    installation = db.Column(db.Text, nullable=True)
    usage = db.Column(db.Text, nullable=True)
    tech_stack = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(200), nullable=True)
    github_link = db.Column(db.String(500), nullable=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "project_name": self.project_name,
            "description": self.description,
            "features": self.features,
            "installation": self.installation,
            "usage": self.usage,
            "tech_stack": self.tech_stack,
            "author": self.author,
            "github_link": self.github_link,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/result/<int:record_id>')
def result(record_id):
    record = ReadmeRecord.query.get_or_404(record_id)
    return render_template('result.html', record=record)

def create_prompt(data):
    return f"""
    Generate a professional, well-structured README.md for the following project:
    Project Name: {data.get('project_name')}
    Description: {data.get('description')}
    Key Features: {data.get('features')}
    Installation Steps: {data.get('installation', 'N/A')}
    Usage Instructions: {data.get('usage', 'N/A')}
    Technology Stack: {data.get('tech_stack')}
    Author: {data.get('author')}
    GitHub Link: {data.get('github_link', '')}

    The README should include:
    1. Project Title
    2. Description
    3. Features (bullet list)
    4. Installation section
    5. Usage section
    6. Tech Stack (nicely formatted)
    7. Author section
    8. License placeholder (MIT)

    Strictly return professional Markdown content. Do not include any text before or after the markdown.
    """

@app.route('/api/generate', methods=['POST'])
def generate_readme():
    try:
        data = request.json
        prompt = create_prompt(data)

        try:
            response = model.generate_content(prompt)
            markdown_content = response.text
        except Exception as ai_err:
            print(f"AI Generation failed: {ai_err}")
            if "429" in str(ai_err) or "quota" in str(ai_err).lower():
                markdown_content = generate_mock_readme(data)
            else:
                raise ai_err

        # Save to database
        new_record = ReadmeRecord(
            project_name=data.get('project_name'),
            description=data.get('description'),
            features=data.get('features'),
            installation=data.get('installation'),
            usage=data.get('usage'),
            tech_stack=data.get('tech_stack'),
            author=data.get('author'),
            github_link=data.get('github_link'),
            content=markdown_content
        )
        db.session.add(new_record)
        db.session.commit()

        return jsonify({
            "success": True,
            "id": new_record.id,
            "content": markdown_content,
            "is_mock": "fallback template" in markdown_content
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/regenerate/<int:record_id>', methods=['POST'])
def regenerate_record(record_id):
    try:
        record = ReadmeRecord.query.get_or_404(record_id)
        data = {
            'project_name': record.project_name,
            'description': record.description,
            'features': record.features,
            'installation': record.installation,
            'usage': record.usage,
            'tech_stack': record.tech_stack,
            'author': record.author,
            'github_link': record.github_link
        }
        
        prompt = create_prompt(data)
        
        try:
            response = model.generate_content(prompt)
            markdown_content = response.text
        except Exception as ai_err:
            print(f"AI Regeneration failed: {ai_err}")
            if "429" in str(ai_err) or "quota" in str(ai_err).lower():
                markdown_content = generate_mock_readme(data)
            else:
                raise ai_err
        
        # Update record
        record.content = markdown_content
        db.session.commit()
        
        return jsonify({
            "success": True,
            "content": markdown_content
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/recent')
def get_recent():
    records = ReadmeRecord.query.order_by(ReadmeRecord.timestamp.desc()).limit(5).all()
    return jsonify([r.to_dict() for r in records])

@app.route('/download/<int:record_id>')
def download_readme(record_id):
    record = ReadmeRecord.query.get_or_404(record_id)
    buffer = io.BytesIO()
    buffer.write(record.content.encode('utf-8'))
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name='README.md',
        mimetype='text/markdown'
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
