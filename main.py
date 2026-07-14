import random

class MedicalAgent:
    def __init__(self):
        self.symptoms = {}
        self.conditions = {
            "Flu": ["fever", "cough", "fatigue", "sore_throat"],
            "Measles": ["fever", "rash", "cough"],
            "Migraine": ["headache", "nausea", "sensitivity_to_light"],
            "Common Cold": ["sneezing", "runny_nose", "sore_throat"],
            "Food Poisoning": ["nausea", "fever", "fatigue"],
        }

    def collect_symptoms(self):
        print("=== Agentic Medical Expert System ===")
        print("Answer with yes or no.\n")

        questions = {
            "fever": "Do you have a fever? ",
            "cough": "Do you have a cough? ",
            "rash": "Do you have a skin rash? ",
            "headache": "Do you have a headache? ",
            "nausea": "Do you feel nauseous? ",
            "sneezing": "Are you sneezing? ",
            "runny_nose": "Do you have a runny nose? ",
            "fatigue": "Do you feel fatigued? ",
            "sore_throat": "Do you have a sore throat? ",
            "sensitivity_to_light": "Are you sensitive to light? ",
        }

        for symptom, question in questions.items():
            answer = input(question).lower()
            self.symptoms[symptom] = answer

    def reason(self):
        possible_diagnoses = {}
        for condition, required_symptoms in self.conditions.items():
            score = sum(1 for s in required_symptoms if self.symptoms.get(s) == "yes")
            if score > 0:
                confidence = round((score / len(required_symptoms)) * 100, 1)
                possible_diagnoses[condition] = confidence

        return possible_diagnoses

    def act(self, diagnoses):
        print("\n=== Diagnosis Result ===")
        if diagnoses:
            print("Possible conditions (with confidence levels):")
            for condition, confidence in sorted(diagnoses.items(), key=lambda x: -x[1]):
                print(f"- {condition}: {confidence}% match")
        else:
            print("Unable to determine the illness. Please consult a doctor.")

        # Agentic behavior: suggest next step
        if diagnoses:
            best_guess = max(diagnoses, key=diagnoses.get)
            print(f"\nAgent Suggestion: Based on your symptoms, you may want to research {best_guess} further or consult a physician.")
        else:
            print("\nAgent Suggestion: Seek professional medical advice immediately.")

# Run the agent
agent = MedicalAgent()
agent.collect_symptoms()
diagnoses = agent.reason()
agent.act(diagnoses)
