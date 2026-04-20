import pandas as pd

# Load your data into a dataframe
df = pd.read_csv("health_data.csv")

# Print welcome message
print("Healthbot: Hello there, I am your health assistant bot. Ask me about any symptoms.")

while True:
    # Get user input
    user_text = input("\nYou: ").lower()

    # Check if user wants to exit
    if user_text == "quit":
        print("Healthbot: Goodbye! Nice to have been of service to you. Have a healthy day!")
        break

    # Variable to track if answer found
    found_answer = False

    # Loop through dataframe rows
    for index, row in df.iterrows():
        symptom = str(row["symptom"]).lower()
        response = row["response"]

        if user_text in symptom:
            print("Healthbot:", response)
            found_answer = True
            break

    # If no match found
    if not found_answer:
        print("Healthbot: Sorry, I couldn't find information about that symptom.") index .row in df.iterrows():
    # clean up the keyboards from the csv 
    keywords_list=str(row["Keywords"]).split(",")

    # Below we check every keyword in that given row (Keywords)

    for  word in keywords_list:
        clean_word = word.strip().lower()

        # if the keyword is inside  of the user'sentence 
        if clean_word in user_text
        print("Health",row["Response"])
        found_answer = True
        break
    if found_answer:
        break
if not found_answer