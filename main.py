import os
import groq
from datetime import datetime

# Set up Groq AI API key
groq_client = groq.Client(api_key="") #Try to store API key in environment variables

SCHEDULE_FILE = "schedule.txt"
HELP_MESSAGE = """
Available commands:
- create schedule: Create a new schedule (must delete existing first)
- delete schedule: Delete the current schedule
- tell me my schedule: Show the full schedule
- exit: Exit the program

You can also just describe what you want, e.g.:
- "I want to have lunch at 5pm, gym at 5am, and call my mom at 3pm."
"""

def create_schedule():
    if os.path.exists(SCHEDULE_FILE):
        return "A schedule already exists. Delete it first before creating a new one."
    with open(SCHEDULE_FILE, "w") as file:
        file.write("Your schedule:\n")
    return "Schedule created successfully."

def delete_schedule():
    if os.path.exists(SCHEDULE_FILE):
        os.remove(SCHEDULE_FILE)
        return "Schedule deleted."
    return "No schedule found to delete."

def show_schedule():
    if not os.path.exists(SCHEDULE_FILE):
        return "No schedule found. Create one first."
    with open(SCHEDULE_FILE, "r") as file:
        return file.read()

def process_natural_input(user_input):
    if not os.path.exists(SCHEDULE_FILE):
        return "No schedule found. Create one first."
    
    with open(SCHEDULE_FILE, "r") as file:
        schedule_data = file.read()
    
    response = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a scheduling assistant. Extract tasks and times from the user input and update the schedule in a structured way."},
            {"role": "user", "content": f"Current Schedule:\n{schedule_data}\nUser input: {user_input}\nFormat it correctly."}
        ]
    )
    
    updated_schedule = response.choices[0].message.content.strip()
    
    with open(SCHEDULE_FILE, "w") as file:
        file.write(updated_schedule)
    
    return "Schedule updated successfully!"

def main():
    print("Welcome to your AI-powered schedule assistant!")
    print(HELP_MESSAGE)
    
    while True:
        user_input = input("Enter command: ").strip()
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "help":
            print(HELP_MESSAGE)
        elif user_input.lower() == "create schedule":
            print(create_schedule())
        elif user_input.lower() == "delete schedule":
            print(delete_schedule())
        elif user_input.lower() == "tell me my schedule":
            print(show_schedule())
        else:
            print(process_natural_input(user_input))

if __name__ == "__main__":
    main()
