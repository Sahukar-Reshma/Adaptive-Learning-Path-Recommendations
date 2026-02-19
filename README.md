# Adaptive-Learning-Path-Recommendations

# Adaptive Learning Path for Students

A **Python-based project** that provides an **adaptive learning path** for students based on their performance, queries, and understanding.  
The system recommends topics, exercises, and explanations tailored to each student’s learning level.

---

## Features

- Personalized **learning path** based on student inputs  
- **Topic recommendation** according to skill and difficulty  
- **Query understanding** to provide relevant explanations and examples  
- **Difficulty assessment**: Beginner, Intermediate, Advanced  
- Works **offline** with pre-trained models  

---

## Tech Stack

- **Language:** Python 3.10  
- **IDE:** VS Code  
- **Libraries / Dependencies:**
  - `numpy` – for numerical operations  
  - `pandas` – for handling student data  
  - `sentence-transformers` – for query understanding  
  - `scikit-learn` – for classification models  
  - `matplotlib` / `seaborn` (optional) – for visualizing student progress  

---

## Setup / Installation

### Prerequisites

- Python 3.10+ installed: [Download Python]([https://www.python.org/downloads/](https://www.python.org/downloads/release/python-3100/))  
- Git installed: [Download Git]([https://git-scm.com/downloads](https://desktop.github.com/download/))  
- VS Code (optional but recommended): [Download VS Code]([https://code.visualstudio.com/](https://code.visualstudio.com/download))  

### Steps

1. **Clone the repository**
```bash``

git clone https://github.com/your-username/adaptive-learning-path.git
cd adaptive-learning-path

2. **Install dependencies**

pip install numpy pandas sentence-transformers scikit-learn matplotlib seaborn


3. Run the main program

python main.py


**Usage**
The system will prompt for student queries or input.

Type your query or student response.

Type exit or quit to stop the program.

4.Output Example:

Student Question: I don't understand gradient descent
--- Output ---
{
    "recommended_topic": "Gradient Descent",
    "difficulty_level": "Intermediate",
    "next_steps": [
        "Watch a short explanation video on gradient descent",
        "Try a beginner-level exercise",
        "Read summary notes"
    ],
    "answer": "Explanation on Gradient Descent: This is a concise explanation tailored to your level."
}

5. Project Structure
adaptive-learning-path/
│
├─ main.py                  # Entry point for adaptive learning path
├─ src/
│   └─ adaptive_learning.py  # Core module for learning path generation
├─ README.md                # Project documentation
└─ data/                    # Optional: student progress or topic data

git clone https://github.com/your-username/adaptive-learning-path.git
cd adaptive-learning-path
