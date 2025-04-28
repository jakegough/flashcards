import json

# Create a list to store all 144 questions for times tables 1-12
questions = []

# Generate questions for times tables 1-12
for i in range(2, 13):
    for j in range(2, 13):
        question = f"{i} × {j} = ?"
        answer = i * j
        choices = [answer, answer - 1, answer + 1, answer - 2]
        # Ensure that answer is always in the choices
        choices = list(set(choices))  # Remove duplicates
        choices = choices[:3] if len(choices) > 3 else choices  # Ensure no more than 4 options
        choices.append(answer)
        choices = list(set(choices))  # Remove duplicates again
        choices = list(choices)  # Convert back to a list
        questions.append({
            "type": "multiple",
            "question": question,
            "choices": choices,
            "answer": str(answer),
            "time": 5  # 5 seconds per question
        })

# Convert to JSON format
questions_json = json.dumps(questions, indent=4)

# Save to a file
with open("times_tables_questions.json", "w") as f:
    f.write(questions_json)

# "/mnt/data/times_tables_questions.json"
