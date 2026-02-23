# Adaptive-Learning-Path-Recommendations


# Adaptive Learning Path for Students

An AI-driven Python project that generates a personalized adaptive learning path for students based on their performance metrics, topic mastery, and prior learning behavior.

The system dynamically recommends the next topic, adjusts difficulty level, and guides structured learning progression using a rule-based adaptive recommendation engine.

---

## Project Objective

* Personalize learning progression for each student
* Identify knowledge gaps using performance indicators
* Recommend the next optimal topic
* Adjust difficulty dynamically
* Provide structured academic progression

---

## Core Concept

The system evaluates student learning behavior using multiple parameters:

* Current topic
* Quiz score
* Number of attempts
* Time spent on topic
* Previously asked questions

Based on these inputs, the system:

* Determines mastery level
* Identifies weak or strong areas
* Recommends progression or revision
* Adjusts difficulty accordingly

This ensures that students do not skip foundational concepts and progress only after demonstrating sufficient understanding.

---

## Technical Approach

* Rule-based adaptive decision engine
* Threshold-based performance evaluation
* Knowledge gap detection logic
* Dynamic topic sequencing
* Difficulty adjustment modeling
* Modular object-oriented architecture

The project is implemented using Python and follows OOPS principles for scalability and maintainability.

---

## System Workflow

Student Input
→ Performance Analysis
→ Threshold Evaluation
→ Mastery Detection
→ Adaptive Recommendation
→ Structured JSON Output

---

## Output Example

### Student Input

```
Current Topic: Neural Networks
Quiz Score (0-100): 99
Number of Attempts: 1
Time Spent on Topic (minutes): 20
Previously Asked Questions (comma separated): Linear Regression, Optimization, gradient descent learning rate
```

---

### Adaptive Learning Recommendation

```json
{
    "next_topic": "Backpropagation",
    "action": "Continue",
    "difficulty_adjustment": "Increase"
}
```

---

## Output Interpretation

* **next_topic** → Recommended next learning concept
* **action** → Continue / Revise / Practice
* **difficulty_adjustment** → Increase / Decrease / Maintain

In this example:

* High score (99/100)
* Minimal attempts (1)
* Efficient learning time

The system detects strong mastery and recommends progression to an advanced topic while increasing difficulty.

---

## Features

* Personalized learning path generation
* Performance-driven topic sequencing
* Knowledge gap detection
* Difficulty level adjustment
* Modular and scalable design
* Offline functionality
* Structured JSON output

---

## Tech Stack

**Language:** Python 3.10
**IDE:** VS Code

### Libraries / Dependencies

* `numpy` – Numerical operations
* `pandas` – Handling student performance data
* `sentence-transformers` – Semantic query understanding
* `scikit-learn` – Classification and modeling
* `matplotlib` / `seaborn` (optional) – Progress visualization

---

## Setup & Installation

### Prerequisites

* Python 3.10+
  [https://www.python.org/downloads/](https://www.python.org/downloads/)

* Git
  [https://git-scm.com/downloads](https://git-scm.com/downloads)

* VS Code (recommended)
  [https://code.visualstudio.com/](https://code.visualstudio.com/)

---

### Clone Repository

```bash
git clone https://github.com/Sahukar-Reshma/Adaptive-Learning-Path-Recommendations
cd Adaptive-Learning-Path-Recommendations
```

### Install Dependencies
pip install numpy pandas sentence-transformers scikit-learn matplotlib seaborn

## Run the Program
python main.py

### Project Structure
Adaptive-Learning-Path-Recommendations/
│
├── main.py                      # Entry point
├── src/
│   └── adaptive_learning.py     # Core adaptive learning logic
├── data/                        # Optional: student data storage
├── README.md                    # Project documentation


### OOPS Design

The project follows a modular class-based architecture:

Constructor initializes topic sequence and configuration

Recommendation logic encapsulated inside class

Public method (e.g., recommend()) exposes core functionality

Internal logic abstracted from user interface

This design ensures:

Clean separation of concerns

Maintainability

Scalability

Extensibility


### Future Enhancements

Reinforcement Learning for dynamic adaptation

Performance prediction modeling

Vector database integration

REST API deployment

Full integration with Student Query Understanding module

Cloud-based deployment

### Use Cases

AI-powered tutoring systems

Smart Learning Management Systems (LMS)

Personalized e-learning platforms

Educational analytics systems

### Repository Link
git clone https://github.com/Sahukar-Reshma/Adaptive-Learning-Path-Recommendations


