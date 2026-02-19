import json
from difflib import get_close_matches

class AdaptiveLearningPath:
    """
    Adaptive learning path recommendation.
    Inputs:
      - Quiz scores
      - Number of attempts
      - Time spent on topics
      - Previously asked questions
    Outputs:
      - next_topic
      - action (Revision / Continue)
      - difficulty_adjustment (Increase / Decrease / Same)
    """

    def __init__(self):
        # Sequence of topics
        self.topic_sequence = [
            "Linear Regression",
            "Gradient Descent Learning Rate",
            "Neural Networks",
            "Backpropagation",
            "Optimization"
        ]

    def recommend(self, student_profile: dict):
        # Normalize current topic
        current_topic = student_profile.get("current_topic", "").strip()
        score = student_profile.get("quiz_score", 0)
        attempts = student_profile.get("attempts", 1)
        time_spent = student_profile.get("time_spent", 0)
        previous_questions = student_profile.get("previous_questions", [])

        # Determine action: Revision or Continue
        if score < 60 or attempts > 1 or time_spent > 40:
            action = "Revision"
        else:
            action = "Continue"

        # Determine difficulty adjustment
        if score > 85 and attempts == 1:
            difficulty_adjustment = "Increase"
        elif score < 60:
            difficulty_adjustment = "Decrease"
        else:
            difficulty_adjustment = "Same"

        # Match current_topic to the closest topic in sequence
        matches = get_close_matches(current_topic, self.topic_sequence, n=1, cutoff=0.5)
        if matches:
            matched_topic = matches[0]
        else:
            matched_topic = self.topic_sequence[0]

        # Determine next topic
        if action == "Revision":
            next_topic = matched_topic
        else:
            idx = self.topic_sequence.index(matched_topic)
            if idx + 1 < len(self.topic_sequence):
                next_topic = self.topic_sequence[idx + 1]
            else:
                next_topic = matched_topic  # last topic, stay

        return {
            "next_topic": next_topic,
            "action": action,
            "difficulty_adjustment": difficulty_adjustment
        }
