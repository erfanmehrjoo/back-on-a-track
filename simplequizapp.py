# a dictionary that stores questions and ansewrs
# have a variable that tracks the score of the player
# loop throught the dictionary using the key values pairs
# display each question to the user and allow them to ansewr 
# tell them if they are right or wrong 
# show the final result when queiz is completed

quiz = {
    "questions1": {
        "question": "what is the capital of france?",
        "answer": "paris",
        "correct": True
    },
    "questions2": {
        "question": "what is the capital of germany?",
        "answer": "berlin",
        "correct": True
    },
    "questions3":{
        "question": "what is the capital of china?",
        "answer": "beijing",
        "correct": True
    },
    "questions4":{
        "question": "what is the capital of india?",
        "answer": "new delhi",
        "correct": True
    },
    "questions5":{
        "question": "what is the capital of usa?",
        "answer": "washington dc",
        "correct": True
    },
    "question6":{
        "question": "what is the capital of russia?",
        "answer": "moscow",
        "correct": True
    },
    "questions7":{
        "question": "what is the capital of brazil?",
        "answer": "brasilia",
        "correct": True
    },
}

score = 0

for question, answer in quiz.items():
    print(answer["question"])
    user_answer = input("answer: ")
    if user_answer == answer["answer"]:
        score += 1
        
    else:
        print("wrong answer")
        print("the awnser is :" , answer["answer"])

print(f"your score is {score}/7")