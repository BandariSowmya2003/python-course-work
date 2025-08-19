#HTML Quiz Game in Python

def run_quiz():
    print("Welcome to the HTML Quiz Game!\n")

    questions = [
        {
            "question": "1. What does HTML stand for?",
            "options": {
                "a": "Hyper Text Markup Language",
                "b": "Hyperlinks and Text Markup Language",
                "c": "Home Tool Markup Language",
                "d": "Hyper Transfer Markup Language"
            },
            "answer": "a"
        },
        {
            "question": "2. Which HTML element is used for the largest heading?",
            "options": {
                "a": "<heading>",
                "b": "<h6>",
                "c": "<h1>",
                "d": "<head>"
            },
            "answer": "c"
        },
        {
            "question": "3. Which tag is used to create a hyperlink?",
            "options": {
                "a": "<link>",
                "b": "<href>",
                "c": "<a>",
                "d": "<hyper>"
            },
            "answer": "c"
        },
        {
            "question": "4. Which tag is used to display an image?",
            "options": {
                "a": "<img>",
                "b": "<image>",
                "c": "<pic>",
                "d": "<src>"
            },
            "answer": "a"
        },
        {
            "question": "5. Which tag is used to create a numbered list?",
            "options": {
                "a": "<ul>",
                "b": "<ol>",
                "c": "<list>",
                "d": "<nl>"
            },
            "answer": "b"
        },
        {
            "question": "6. Which tag is used to create a table row?",
            "options": {
                "a": "<td>",
                "b": "<tr>",
                "c": "<th>",
                "d": "<row>"
            },
            "answer": "b"
        },
        {
            "question": "7. Which tag is used to create a drop-down list?",
            "options": {
                "a": "<dropdown>",
                "b": "<select>",
                "c": "<option>",
                "d": "<list>"
            },
            "answer": "b"
        },
        {
            "question": "8. Which HTML tag is used for a checkbox?",
            "options": {
                "a": "<input type='checkbox'>",
                "b": "<check>",
                "c": "<checkbox>",
                "d": "<box>"
            },
            "answer": "a"
        },
        {
            "question": "9. Which HTML element is used for a paragraph?",
            "options": {
                "a": "<para>",
                "b": "<pg>",
                "c": "<p>",
                "d": "<paragraph>"
            },
            "answer": "c"
        },
        {
            "question": "10. Which HTML tag is used to create a list item?",
            "options": {
                "a": "<li>",
                "b": "<list-item>",
                "c": "<item>",
                "d": "<point>"
            },
            "answer": "a"
        }
    ]

    score = 0
    for q in questions:
        print(q["question"])
        for key, value in q["options"].items():
            print(f"{key}) {value}")
        answer = input("Your answer (a/b/c/d): ").lower()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{q['answer']}'\n")

    print(f"Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("Perfect! You're an HTML master!")
    elif score >= 15:
        print("Great job! Keep practicing!")
    else:
        print("You can improve! Review HTML basics.")


#Run the game
run_quiz()
