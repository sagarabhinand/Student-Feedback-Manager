from score_calculator import calculate_score

def generate_summary(feedback_list):
    """Summarize the feedback data."""
    if not feedback_list:
        return "No feedback available."
    
    summary = {
        "total_entries": len(feedback_list),
        "average_score": calculate_score(feedback_list),
        "positive_feedback_count": sum(1 for f in feedback_list if f.get("score", 0) >= 4),
        "negative_feedback_count": sum(1 for f in feedback_list if f.get("score", 0) <= 2),
    }
    
    return summary

