import json

def enter_feedback(feedback_data, file_path="feedback_data.json"):
    """Enter feedback data into the system and save it to a JSON file."""
    try:
        with open(file_path, "a+") as file:
            file.seek(0)
            feedback = json.load(file) if file.read() else []
            feedback.append(feedback_data)
            
            file.seek(0)
            json.dump(feedback, file, indent=4)
            print("Feedback successfully entered.")
    except Exception as e:
        print(f"Error while entering feedback: {e}")

