# 🧠 Agentic Medical Expert System

A simple **agentic AI prototype** written in Python that simulates a medical expert system.  
This project demonstrates how an AI agent can **collect information, reason about it, and act autonomously** by suggesting possible diagnoses based on user-reported symptoms.

---

## 📌 Features

- **Agentic loop**: The system follows a `Collect → Reason → Act` cycle, mimicking how autonomous agents operate.
- **Symptom collection**: Interactive prompts ask the user about common symptoms (fever, cough, rash, headache, etc.).
- **Knowledge base**: Conditions are stored in a structured dictionary mapping illnesses to their symptoms.
- **Reasoning engine**: Matches user inputs against conditions and calculates confidence scores.
- **Multiple diagnoses**: Suggests all possible conditions that match, not just one.
- **Confidence scoring**: Each condition is given a percentage match based on how many symptoms align.
- **Autonomous action**: The agent provides next-step suggestions (e.g., consult a physician, research further).

---

## ⚙️ How It Works

1. **Collect Symptoms**  
   The agent asks the user a series of yes/no questions about symptoms.

2. **Reasoning**  
   - Each condition has a set of required symptoms.  
   - The agent calculates how many symptoms match.  
   - Confidence = `(matched symptoms / total symptoms for condition) × 100`.

3. **Act**  
   - Displays all possible conditions with confidence levels.  
   - Suggests the most likely condition as a next step.  
   - Advises consulting a doctor if no match is found.

---

## 🚀 Usage

### 1. Clone the repository
```bash
git clone https://github.com/mrwicktheprogrammer/First-Agentic-AI.git
cd First-Agentic-AI

### 2. Run the program
```bash
python main.py

### 3. Example Interaction
=== Agentic Medical Expert System ===
Answer with yes or no.

Do you have a fever? yes
Do you have a cough? yes
Do you have a skin rash? no
Do you have a headache? no
Do you feel nauseous? no
Are you sneezing? no
Do you have a runny nose? yes
Do you feel fatigued? yes
Do you have a sore throat? yes
Are you sensitive to light? no

=== Diagnosis Result ===
Possible conditions (with confidence levels):
- Flu: 75.0% match
- Common Cold: 66.7% match

Agent Suggestion: Based on your symptoms, you may want to research Flu further or consult a physician.

🛠️ Code Structure
main.py
│
├── class MedicalAgent:
│   ├── collect_symptoms()   # Collects user input
│   ├── reason()             # Matches symptoms to conditions
│   └── act()                # Outputs diagnosis + suggestions
│
└── agent = MedicalAgent()   # Runs the agentic loop

⚠️ Disclaimer
This project is for educational purposes only.
It is not a medical tool and should not be used for real diagnosis.
Always consult a qualified healthcare professional for medical concerns.

🌟 Future Improvements
Add weighted symptoms (some symptoms matter more than others).
Introduce learning capability (store past cases and improve over time).
Connect to medical datasets/APIs for real-world accuracy.
Expand into a multi-agent system (diagnosis agent + recommendation agent).

👨‍💻 Author
Created by Jonathan as a first agentic AI project to explore autonomous reasoning systems.
Inspired by the idea of building simple, rule-based agents that can evolve into more advanced AI systems.
