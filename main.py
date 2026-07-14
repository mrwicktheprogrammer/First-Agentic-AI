def diagnose():
    print("=== Advanced Medical Expert System ===")
    print("Answer with yes or no.\n")

    # Collect Symptoms
    symptoms = {
        "fever": input("Do you have a fever? ").lower(),
        "cough": input("Do you have a cough? ").lower(),
        "rash": input("Do you have a skin rash? ").lower(),
        "headache": input("Do you have a headache? ").lower(),
        "nausea": input("Do you feel nauseous? ").lower(),
        "sneezing": input("Are you sneezing? ").lower(),
        "runny_nose": input("Do you have a runny nose? ").lower(),
        "fatigue": input("Do you feel fatigued? ").lower(),
        "sore_throat": input("Do you have a sore throat? ").lower(),
    }

    # Knowledge base: conditions mapped to required symptoms
    conditions = {
        "Flu": ["fever", "cough", "fatigue", "sore_throat"],
        "Measles": ["fever", "rash", "cough"],
        "Migraine": ["headache", "nausea"],
        "Common Cold": ["sneezing", "runny_nose", "sore_throat"],
        "Food Poisoning": ["nausea", "fever", "fatigue"],
    }

    # Diagnosis scoring
    possible_diagnoses = {}
    for condition, required_symptoms in conditions.items():
        score = sum(1 for s in required_symptoms if symptoms[s] == "yes")
        if score > 0:
            confidence = round((score / len(required_symptoms)) * 100, 1)
            possible_diagnoses[condition] = confidence

    # Output result
    print("\n=== Diagnosis Result ===")
    if possible_diagnoses:
        print("Possible conditions (with confidence levels):")
        for condition, confidence in sorted(possible_diagnoses.items(), key=lambda x: -x[1]):
            print(f"- {condition}: {confidence}% match")
    else:
        print("Unable to determine the illness. Please consult a doctor.")


# Run the expert system
diagnose()
