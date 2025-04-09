def calculate_score(feedback_list):
    """Calculate the average score based on feedback data."""
    total_score = 0
    total_entries = len(feedback_list)
    
    for feedback in feedback_list:
        total_score += feedback.get("score", 0)
    
    average_score = total_score / total_entries if total_entries > 0 else 0
    return average_score

