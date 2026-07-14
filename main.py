def diagnose():
    print("=== Simple Medical Expert System ===")
    print("Answer with yes or no.\n")

#Collect Symptoms
    fever = input("Do you gave a fever? ").lower()
    cough = input("Do you have a cough? ").lower()
    rash = input("Do you have a skin rash? ").lower()
    headache = input("Do you have a headache? ").lower()
    nausea = input("Do you feel nauseous? ").lower()
    sneezing = input("are you snezing? ").lower()
    runny_nose = input("do you have runny nose? ").lower()

    #Inference rules
    if fever == "yes" and cough == "yes":
        diagnosis = "Flu"
    elif fever == "yes" and rash == "yes":
        diagnosis = "Measles"
    elif headache == "yes" and nausea =="yes":
        diagnosis = "Migrane"
    elif sneezing == "yes" and runny_nose == "yes":
        diagnosis = "Common Cold"

    else:
        diagnose = "Unable to determine the illness."

#Output result
print("\n=== Diagnosis Result ===")
print("Possible condition:")

# Run the expert system
diagnose()