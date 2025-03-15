# AI-Powered Schedule Assistant

This is a simple AI-powered scheduling assistant that allows you to create, modify, and view your schedule using natural language commands. The assistant processes user input and updates the schedule accordingly.

## Features
- Create and delete a schedule
- View your current schedule
- Update your schedule using natural language (e.g., "I want to have lunch at 5pm, gym at 5am, and call my mom at 3pm.")
- Persistent schedule storage in a text file

## Requirements
Ensure you have Python installed along with the necessary dependencies:

```sh
pip install groq
```

You also need to set up a **Groq AI API key** for processing natural language inputs. Replace `api_key=""` with your actual API key in the script.

## Usage
Run the script with:

```sh
python schedule_assistant.py
```

### Available Commands
- `create schedule` – Create a new schedule (must delete existing one first)
- `delete schedule` – Delete the current schedule
- `tell me my schedule` – Show the full schedule
- `exit` – Exit the program

You can also describe your schedule in natural language, and the AI will update it accordingly.

## Limitations
- Requires a Groq AI API key to function properly.
- The schedule is stored in a simple text file and may not handle complex scheduling needs.
- May not always format tasks perfectly due to AI response variability.

## Disclaimer
Use this script responsibly. The author is not responsible for any issues arising from its use.

