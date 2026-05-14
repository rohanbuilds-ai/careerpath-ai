import os
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure the LLM API (Using Gemini as the default configurable LLM)
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Predefined question banks
# Predefined question banks
QUESTIONS_DB = {
    "data scientist": [
        "Are you comfortable writing Python or R code for data analysis?",
        "Do you have experience querying databases using SQL?",
        "Do you understand basic statistics and probability?",
        "Have you trained basic Machine Learning models (e.g., linear regression)?",
        "Can you create data visualizations using tools like Matplotlib, Seaborn, or Tableau?"
    ],
    "web developer": [
        "Are you proficient in semantic HTML and modern CSS?",
        "Do you understand JavaScript fundamentals and ES6+ syntax?",
        "Have you built projects using a frontend framework (React, Vue, Angular)?",
        "Do you understand RESTful APIs and how to fetch data from them?",
        "Are you familiar with version control systems like Git?"
    ],
    "cybersecurity analyst": [
        "Do you understand core networking concepts (TCP/IP, DNS, HTTP)?",
        "Are you familiar with common vulnerabilities like SQL Injection and XSS?",
        "Have you used security tools like Wireshark, Nmap, or Metasploit?",
        "Do you know the basics of cryptography and encryption protocols?",
        "Are you comfortable working with Linux command-line interfaces?"
    ],
    "ai/ml engineer": [
        "Are you proficient in Python and libraries like NumPy or Pandas?",
        "Do you understand deep learning architectures (e.g., CNNs, RNNs)?",
        "Have you built and evaluated models using TensorFlow or PyTorch?",
        "Do you know how to handle and preprocess large datasets?",
        "Are you familiar with model deployment and MLOps basics?"
    ],
    "cloud architect": [
        "Do you have hands-on experience with AWS, Azure, or Google Cloud?",
        "Are you familiar with containerization tools like Docker and Kubernetes?",
        "Do you understand Infrastructure as Code (IaC) using Terraform or similar?",
        "Have you designed scalable and highly available system architectures?",
        "Do you understand cloud security and identity management (IAM)?"
    ],
    "generic": [
        "Do you have formal education or training related to this field?",
        "Are you familiar with the standard tools and software used in this role?",
        "Have you completed any hands-on projects or internships in this area?",
        "Are you comfortable communicating complex ideas to a team?",
        "Do you have experience troubleshooting and solving domain-specific problems?"
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions', methods=['POST'])
def get_questions():
    data = request.json
    career = data.get('career', '').strip().lower()
    
    # Simple fuzzy match for predefined lists
    if 'data' in career:
        questions = QUESTIONS_DB['data scientist']
    elif 'web' in career or 'software' in career or 'developer' in career:
        questions = QUESTIONS_DB['web developer']
    elif 'cyber' in career or 'security' in career or 'hacker' in career:
        questions = QUESTIONS_DB['cybersecurity analyst']
    elif 'ai' in career or 'machine learning' in career or 'ml' in career:
        questions = QUESTIONS_DB['ai/ml engineer']
    elif 'cloud' in career or 'architect' in career or 'aws' in career:
        questions = QUESTIONS_DB['cloud architect']
    else:
        questions = QUESTIONS_DB['generic']
        
    return jsonify({"questions": questions})

@app.route('/api/roadmap', methods=['POST'])
def generate_roadmap():
    if not api_key:
        return jsonify({"error": "API key not configured."}), 500

    data = request.json
    career = data.get('career', 'Unknown Role')
    answers = data.get('answers', [])

    # Construct the strict prompt
    prompt = f"""
    You are an expert career counselor. The user wants to become a "{career}".
    Here is their current skill assessment:
    {json.dumps(answers, indent=2)}
    
    Based on their gaps (where they answered 'No' or 'Partially'), create a learning roadmap.
    
    CRITICAL REQUIREMENT: You must return ONLY a valid JSON object matching this exact schema. Do not include markdown blocks, backticks, or any other text.
    {{
      "phases": [
        {{
          "title": "string",
          "duration": "string",
          "tasks": ["string"],
          "resources": ["string"]
        }}
      ],
      "expert_tips": ["string"]
    }}
    """

    try:
        # Initialize the model (using Gemini 1.5 Flash for fast JSON response)
        # Initialize the model (using the newer Gemini 2.5 Flash)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Enforce JSON output type
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
            )
        )
        
        # Parse output to ensure it's valid JSON before sending to frontend
        roadmap_json = json.loads(response.text)
        return jsonify(roadmap_json)
        
    except json.JSONDecodeError:
        return jsonify({"error": "The AI returned an invalid response format. Please try again."}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)