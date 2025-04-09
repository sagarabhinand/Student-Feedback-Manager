def search_feedback(feedback_list, keyword):
    """Search feedback entries by a keyword in the comments."""
    results = [feedback for feedback in feedback_list if keyword.lower() in feedback.get("comment", "").lower()]
    return results

