API_KEY = "B4EcU4VGlw"
import csv
from fuzzywuzzy import process
import google.generativeai as genai
from datetime import datetime

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def load_dataset_from_csv(filename):
    dataset = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            dataset[row[0]] = row[1]
    return dataset

def get_best_match(question, dataset):
    best_match, score = process.extractOne(question, dataset.keys())
    if score >= 90:
        return dataset[best_match]
    else:
        return None

def chatbot(question, dataset):
    answer = get_best_match(question, dataset)
    if answer:
        return answer
    else:
        return ask_gpt(question)

def ask_gpt(prompt):
    response = model.start_chat(history=[]).send_message(prompt)
    return response.text

def main():
    dataset_filename = "C:/Users/win11/Desktop/Sem-VI PBL/NLP/Questions.csv"
    dataset = load_dataset_from_csv(dataset_filename)

    # Fetching current date and time
    Date = datetime.now().strftime("%d-%m-%Y")
    # print("Current Time:", Date)
    current_time = datetime.now().strftime("%H:%M:%S")
    # print("Current Time:", current_time)
    Day = datetime.now().strftime("%A")
    # print("Current Time:", Day)
    print()
    print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print("::            Welcome to Advance Chatbot Assistance!!!!😊😊                ::")
    print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print()
    print(" _________________________________________________________________________")
    print("|                       Today's Date is: "+ Date+"                       |")
    print("|                        And the Time is: "+ current_time + "                        |")
    print("|     So, What would you like to know, specifically on this "+ Day+ "?     |")
    print("|_________________________________________________________________________|\n\n")
    
    print("Chatbot: Hello! I'm your chatbot. You can ask me anything.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot(user_input, dataset)
        print("Chatbot:", response)
if __name__ == "__main__":
    main()