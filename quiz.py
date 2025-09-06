import tkinter as tk
from tkinter import messagebox

# Lista de perguntas com opções e o índice da resposta correta
questions = [
    {
        "question": "What is the main cause of global warming?",
        "options": ["Deforestation", "Recycling", "Water pollution", "Air pollution"],
        "correct": 0,  # Índice da resposta correta: "Deforestation"
    },
    {
        "question": "Which of these is a renewable resource?",
        "options": ["Coal", "Wind", "Oil", "Natural gas"],
        "correct": 1,  # Índice da resposta correta: "Wind"
    },
    {
        "question": "What does recycling help reduce?",
        "options": ["Waste", "Water", "Temperature", "Noise"],
        "correct": 0,  # Índice da resposta correta: "Waste"
    },
    {
        "question": "What should you do with plastic bottles?",
        "options": ["Burn them", "Bury them", "Leave them outside", "Recycle them"],
        "correct": 3,  # Índice da resposta correta: "Recycle them"
    },
    {
        "question": "Which of these is harmful to the environment?",
        "options": [
            "Planting trees",
            "Using renewable energy",
            "Deforestation",
            "Recycling waste",
        ],
        "correct": 2,  # Índice da resposta correta: "Deforestation"
    },
    {
        "question": "What gas is primarily responsible for the greenhouse effect?",
        "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
        "correct": 1,  # Índice da resposta correta: "Carbon dioxide"
    },
    {
        "question": "Which process helps restore soil fertility?",
        "options": [
            "Salinization",
            "Pesticide application",
            "Crop rotation",
            "Deforestation",
        ],
        "correct": 2,  # Índice da resposta correta: "Crop rotation"
    },
    {
        "question": "What is a common effect of acid rain?",
        "options": [
            "Increased biodiversity",
            "Mosquito reduction",
            "Soil acidification",
            "Improved air quality",
        ],
        "correct": 2,  # Índice da resposta correta: "Soil acidification"
    },
    {
        "question": "Which material is not biodegradable?",
        "options": ["Glass", "Paper", "Cotton", "Wood"],
        "correct": 0,  # Índice da resposta correta: "Glass"
    },
    {
        "question": "Which practice helps conserve water at home?",
        "options": [
            "Taking longer showers",
            "Watering lawns during midday",
            "Leaving taps running",
            "Installing low-flow fixtures",
        ],
        "correct": 3,  # Índice da resposta correta: "Installing low-flow fixtures"
    },
]

# Variáveis para guardar pontuação e número da pergunta atual
score = 0
question_num = 0


def display_question():
    # Mostra a pergunta atual e coloca o texto nos botões
    current_question = questions[question_num]
    question_label.config(text=current_question["question"])
    for i, option in enumerate(current_question["options"]):
        buttons[i].config(
            text=option,
            state="normal",
            bg="SystemButtonFace",  # cor padrão do botão
            fg="black",  # texto preto padrão
        )
    next_button.config(state="disabled")  # só libera depois de responder


def check_answer(selected_index):
    # Verifica se a resposta está certa e deixa os botões verde (se acertar) ou vermelho (se errar)
    global score
    correct_index = questions[question_num]["correct"]

    if selected_index == correct_index:
        buttons[selected_index].config(bg="#4CAF50", fg="white")  
        score += 1 # soma ponto se acertar
    else:
        buttons[selected_index].config(bg="#F44336", fg="white")  
        buttons[correct_index].config(bg="#4CAF50", fg="white") # mostra qual era a alternativa correta

    for b in buttons:
        b.config(state="disabled")

    next_button.config(state="normal")


def next_question():
    # Vai para a próxima pergunta ou finaliza o quiz
    global question_num
    question_num += 1
    if question_num < len(questions):
        display_question()
    else:
        messagebox.showinfo("Quiz Complete", f"Your score: {score}/{len(questions)}")
        root.quit()


def start_quiz():
    # Começa o quiz do zero
    global score, question_num
    score = 0
    question_num = 0
    start_button.config(state="disabled")
    display_question()


# Configuração da janela principal
root = tk.Tk()
root.title("Environmental Awareness Quiz")

# Label para mostrar a pergunta
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
question_label.pack(pady=20)

# Cria os botões das alternativas
buttons = []
for i in range(4):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 12),
        width=30,
        height=2,
        command=lambda i=i: check_answer(i),
    )
    btn.pack(pady=5)
    buttons.append(btn)

# Botão para iniciar o quiz
start_button = tk.Button(
    root, text="Start Quiz", font=("Arial", 12), command=start_quiz
)
start_button.pack(pady=20)

# Botão para ir para a próxima pergunta
next_button = tk.Button(
    root,
    text="Next Question",
    font=("Arial", 12),
    state="disabled",
    command=next_question,
)
next_button.pack(pady=20)

root.mainloop()
