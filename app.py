from hugchat import hugchat
import pandas as pd

# Initialize the chatbot
chatbot = hugchat.ChatBot(cookie_path="cookies.json")
id = chatbot.new_conversation()
chatbot.change_conversation(id)

def chat(prompt):
    response = chatbot.chat(prompt)
    return response

def extract_info():
    name = None
    email = None
    phone = None
    address = None
    dob = None
    education = None
    
    # Ask for the user's name
    while not name:
        response = chat("What is your name?")
        name = input(f"Chatbot: {response}\nYou: ")
    
    # Ask for the user's email address
    while not email:
        response = chat("What is your email address?")
        email = input(f"Chatbot: {response}\nYou: ")
    
    # Ask for the user's phone number
    while not phone:
        response = chat("What is your phone number?")
        phone = input(f"Chatbot: {response}\nYou: ")
    
    # Ask for the user's address
    while not address:
        response = chat("What is your address?")
        address = input(f"Chatbot: {response}\nYou: ")
    
    # Ask for the user's date of birth
    while not dob:
        response = chat("What is your date of birth?")
        dob = input(f"Chatbot: {response}\nYou: ")
    
    # Ask for the user's education
    while not education:
        response = chat("What is your education?")
        education = input(f"Chatbot: {response}\nYou: ")
    
    # Save the extracted information to a CSV file
    data = pd.DataFrame({
        "Name": [name],
        "Email": [email],
        "Phone": [phone],
        "Address": [address],
        "Date of Birth": [dob],
        "Education": [education]
    })
    data.to_csv("user_info.csv", index=False)
    
    print("Information saved to user_info.csv")

extract_info()
