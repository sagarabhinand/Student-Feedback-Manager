from feedback_summary import generate_summary

def generate_report(feedback_list, report_file="feedback_report.txt"):
    """Generate a report based on feedback data."""
    summary = generate_summary(feedback_list)
    
    with open(report_file, "w") as file:
        file.write("Feedback Report\n")
        file.write("====================\n")
        file.write(f"Total Entries: {summary['total_entries']}\n")
        file.write(f"Average Score: {summary['average_score']}\n")
        file.write(f"Positive Feedback Count: {summary['positive_feedback_count']}\n")
        file.write(f"Negative Feedback Count: {summary['negative_feedback_count']}\n")
        file.write("====================\n")
        print(f"Report successfully generated: {report_file}")

