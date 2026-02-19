from src.adaptive_learning import AdaptiveLearningPath
import json

# Initialize adaptive learning module
adaptive_module = AdaptiveLearningPath()

print("===== Q2: Adaptive Learning Path Recommendation =====")
print("Type 'exit' to quit.\n")

while True:
    current_topic = input("Current Topic: ")
    if current_topic.lower() in ["exit", "quit"]:
        break

    try:
        quiz_score = float(input("Quiz Score (0-100): "))
        attempts = int(input("Number of Attempts: "))
        time_spent = float(input("Time Spent on Topic (minutes): "))
    except ValueError:
        print("Please enter valid numeric values.")
        continue

    previous_questions = input("Previously Asked Questions (comma separated): ")
    previous_questions_list = [t.strip() for t in previous_questions.split(",") if t.strip()]

    student_profile = {
        "current_topic": current_topic,
        "quiz_score": quiz_score,
        "attempts": attempts,
        "time_spent": time_spent,
        "previous_questions": previous_questions_list
    }

    recommendation = adaptive_module.recommend(student_profile)

    print("\n--- Q2: Adaptive Learning Recommendation ---")
    print(json.dumps(recommendation, indent=4))
    print("\n" + "="*80 + "\n")

