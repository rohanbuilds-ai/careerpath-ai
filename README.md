# CareerPath AI 🚀

An intelligent web application designed to help users transition into new tech roles by generating highly personalized, step-by-step learning roadmaps using Generative AI.

## 📖 Project Context
**Capstone-I Project:** Hybrid UG program in Computer Science & Data Analytics
**Institution:** Indian Institute of Technology Patna (Bihta)

Career transitions are often overwhelming, and beginners struggle to figure out exactly what they need to learn and in what order. CareerPath AI removes this guesswork. By asking users to provide their target career, the app dynamically generates a role-specific skill assessment. Based on the user's answers, it leverages the Google Gemini Large Language Model (LLM) to identify skill gaps and generate a structured curriculum based purely on where the user currently stands.

## ✨ Core Features
- **Dynamic Skill Assessment:** Routes users to specific question banks based on their target role (e.g., Data Science, Web Development).
- **AI-Powered Analysis:** Sends skill gaps to an LLM to generate a customized, phase-by-phase learning roadmap.
- **Strict JSON Enforcement:** Utilizes advanced prompt engineering to ensure the AI returns data in a predictable, parsable format.
- **Modern UI/UX:** A responsive, dark-themed Single Page Application (SPA) with smooth CSS transitions and progress tracking.

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Backend:** Python 3, Flask
* **AI Integration:** Google Generative AI SDK (Gemini 2.5 Flash)

## 👥 The Team
1. **Rohan K (Project Manager & GitHub Lead):** Managed version control, established branching strategies, resolved merge conflicts, delegated tasks, and finalized all project documentation.
2. **Kshitija Ravikant Jugele (Frontend Developer - UI/UX):** Designed and developed the SPA interface, dark mode theme, CSS animations, and dynamic 3-step transition logic.
3. **Khusham Jolly (Backend API Developer):** Developed the core Flask server logic and API routes for serving dynamic questions and securely handling data flow.
4. **Shivjyoti Kumar (AI & Prompt Engineer):** Integrated the Gemini API and engineered system prompts to ensure the LLM strictly outputted JSON-formatted roadmaps.
5. **Kumari Jyoti (QA Tester & DevOps):** Conducted rigorous edge-case testing, managed environment variables, and handled application security and deployment.

---

## 💻 Local Setup Instructions

Follow these steps to run the application on your local machine.

### Prerequisites
- Python 3.8 or higher installed on your system.
- A free API Key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 1. Clone the Repository
```bash
git clone [https://github.com/rohanbuilds-ai/careerpath-ai.git](https://github.com/rohanbuilds-ai/careerpath-ai.git)
cd careerpath-ai
```

### 2. Create a Virtual Environment
It is highly recommended to run this project inside a virtual environment to keep dependencies isolated.
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a file named exactly `.env` in the root directory of the project. **Do not commit this file to GitHub.** Add your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
FLASK_APP=app.py
FLASK_ENV=development
```

### 5. Run the Application
Start the Flask development server:
```bash
flask run
```
Open your web browser and navigate to `http://127.0.0.1:5000` to view the app!

## 🔒 Security Note
This project uses a `.gitignore` file to ensure the `.env` file (which contains the secret API key) is never pushed to the public repository. Never hardcode your API keys directly into `app.py`.
