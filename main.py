from pyscript import document, when

# ==========================================
# 1. FRIENDSHIP TIERS (Highest to Lowest)
# ==========================================
TIERS = [
    {
        "min_percent": 100,
        "title": "Stop taking your own test Maxwell",
        "tagline": "Nice try, Maxwell—nobody else knows every single one of these.",
    },
    {
        "min_percent": 85,
        "title": "Certified Best Friend",
        "tagline": "You practically know Maxwell's brain better than he does.",
    },
    {
        "min_percent": 60,
        "title": "Close Friend",
        "tagline": "Solid score! You definitely pay attention when Maxwell talks.",
    },
    {
        "min_percent": 35,
        "title": "Casual Acquaintance",
        "tagline": "You know the basics, but there's still plenty to learn about Maxwell.",
    },
    {
        "min_percent": 0,
        "title": "Complete Stranger",
        "tagline": "Are you sure you clicked on the right person's quiz?",
    },
]

# ==========================================
# 2. QUESTION BANK (20 Placeholders)
# Note: Keep all strings in "answers" lowercase.
# ==========================================
QUESTIONS = [
    {
        "id": 1,
        "type": "choice",
        "prompt": "What is Maxwell's favorite soda?",
        "options": ["Dr. Pepper", "Coca-Cola", "Sprite", "Root Beer"],
        "answers": ["dr. pepper"],
    },
    {
        "id": 2,
        "type": "text",
        "prompt": "What month was Maxwell born in?",
        "answers": ["october"],
    },
    {
        "id": 3,
        "type": "choice",
        "prompt": "Of the single-player options below, which is Maxwell's favorite video game?",
        "options": ["Portal", "Oblivion", "Neon White", "Vholume", "Arkham City", "Mirror's Edge"],
        "answers": ["portal"],
    },
    {
        "id": 4,
        "type": "text",
        "prompt": "What is Maxwell's favorite color?",
        "answers": ["purple"],
    },
    {
        "id": 5,
        "type": "choice",
        "prompt": "Which pizza place does Maxwell prefer to order delivery from?",
        "options": ["Little Caesars", "Pizza Hut", "Dominos", "Papa Johns"],
        "answers": ["papa johns"],
    },
    {
        "id": 6,
        "type": "choice",
        "prompt": "Which is Maxwell's irrational fear?",
        "options": ["Popsicle sticks", "Paper cuts", "Electrical Sockets", "Tripping in public"],
        "answers": ["popsicle sticks"],
    },
    {
        "id": 7,
        "type": "choice",
        "prompt": "What was the name of Maxwell's pet frog?",
        "options": ["Batman", "Chewbacca", "Doctor Who", "Ferb"],
        "answers": ["chewbacca"],
    },
    {
        "id": 8,
        "type": "choice",
        "prompt": "Which season does Maxwell like best?",
        "options": ["Spring", "Summer", "Fall", "Winter"],
        "answers": ["fall"],
    },
    {
        "id": 9,
        "type": "choice",
        "prompt": "What is Maxwell's favorite kind of dessert?",
        "options": ["Cookies", "Cake", "Ice cream", "Donuts"],
        "answers": ["donuts"],
    },
    {
        "id": 10,
        "type": "text",
        "prompt": "How many degrees in total does Maxwell's spine curve? (Last confirmed)",
        "answers": ["32", "32 degrees", "32°"],
    },
    {
        "id": 11,
        "type": "choice",
        "prompt": "Who is Maxwell's favorite youtuber?",
        "options": ["Sunlesskhan", "Wirtual", "Summoning Salt", "Matpat", "3fs", "Sideways"],
        "answers": ["3fs"],
    },
    {
        "id": 12,
        "type": "text",
        "prompt": "What subject did Maxwell enjoy most in school?",
        "answers": ["math", "mathematics"],
    },
    {
        "id": 13,
        "type": "choice",
        "prompt": "What is Maxwell's go-to movie genre?",
        "options": ["Sci-Fi", "Comedy", "Action", "Horror"],
        "answers": ["horror"],
    },
    {
        "id": 14,
        "type": "choice",
        "prompt": "What is Maxwell's top listened to artist of the last year? (at the time of making this question)",
        "options": ["Djo", "Valley", "Dreams We've Had", "Songs by Jonas", "Bastille"],
        "answers": ["djo"],
    },
    {
        "id": 15,
        "type": "choice",
        "prompt": "What is Maxwell's second favorite movie?",
        "options": ["The Batman", "Everything Everywhere All at Once", "Obsession", "The Odyssey", "The Black Phone"],
        "answers": ["everything everywhere all at once"],
    },
    {
        "id": 16,
        "type": "choice",
        "prompt": "What is Maxwell's highest ever rank in Rocket League? (any game mode)",
        "options": ["Champion 1", "Champion 2", "Champion 3", "Grand Champ 1", "Grand Champ 2", "Grand Champ 3"],
        "answers": ["champion 3"],
    },
    {
        "id": 17,
        "type": "choice",
        "prompt": "Which superpower would Maxwell choose?",
        "options": ["Invisibility", "Flight", "Teleportation", "Super speed"],
        "answers": ["super speed"],
    },
    {
        "id": 18,
        "type": "text",
        "prompt": "What episode of One Piece is Maxwell currently on?",
        "answers": ["950", "episode 950", "ep 950"],
    },
    {
        "id": 19,
        "type": "choice",
        "prompt": "What was Maxwell's favorite area on his mission?",
        "options": ["Greenwich", "Gosford", "Wollongong", "Armidale", "Sutherland", "Oakhurst", "Camden", "Prariewood"],
        "answers": ["wollongong"],
    },
    {
        "id": 20,
        "type": "text",
        "prompt": "Who is this quiz about?",
        "answers": ["maxwell", "maxwell cannon"],
    },
]


# ==========================================
# 3. DYNAMIC QUESTION RENDERER (Step 5)
# ==========================================
def render_quiz():
    container = document.querySelector("#quiz-questions")
    container.innerHTML = ""

    for index, question in enumerate(QUESTIONS, start=1):
        card = document.createElement("div")
        card.className = "question-card"
        card.id = f"card-{question['id']}"

        prompt = document.createElement("p")
        prompt.className = "question-prompt"
        prompt.textContent = f"{index}. {question['prompt']}"
        card.appendChild(prompt)

        if question["type"] == "choice":
            options_list = document.createElement("div")
            options_list.className = "options-list"

            for option_text in question["options"]:
                label = document.createElement("label")
                label.className = "option-label"

                radio = document.createElement("input")
                radio.type = "radio"
                radio.name = question["id"]
                radio.value = option_text

                span = document.createElement("span")
                span.textContent = option_text

                label.appendChild(radio)
                label.appendChild(span)
                options_list.appendChild(label)

            card.appendChild(options_list)

        elif question["type"] == "text":
            text_input = document.createElement("input")
            text_input.type = "text"
            text_input.name = question["id"]
            text_input.id = f"input-{question['id']}"
            text_input.className = "text-input"
            text_input.placeholder = "Type your answer..."
            text_input.autocomplete = "off"
            card.appendChild(text_input)

        container.appendChild(card)

    status = document.querySelector("#loading-status")
    status.textContent = "Quiz ready — answer all 20 questions below!"


# ==========================================
# 4. VALIDATION & GRADING ENGINE (Step 6)
# ==========================================
@when("submit", "#quiz-form")
def handle_submit(event):
    event.preventDefault()

    validation_box = document.querySelector("#validation-message")
    results_banner = document.querySelector("#results-banner")

    unanswered_numbers = []
    first_missing_card = None
    user_answers = {}

    # Check every question for a non-empty response
    for index, question in enumerate(QUESTIONS, start=1):
        qid = question["id"]
        card = document.querySelector(f"#card-{qid}")
        card.classList.remove("unanswered")

        if question["type"] == "choice":
            selected = document.querySelector(f'input[name="{qid}"]:checked')
            if selected is None:
                unanswered_numbers.append(index)
                card.classList.add("unanswered")
                if first_missing_card is None:
                    first_missing_card = card
            else:
                user_answers[qid] = selected.value.strip().lower()

        elif question["type"] == "text":
            text_el = document.querySelector(f"#input-{qid}")
            cleaned = text_el.value.strip().lower()
            if not cleaned:
                unanswered_numbers.append(index)
                card.classList.add("unanswered")
                if first_missing_card is None:
                    first_missing_card = card
            else:
                user_answers[qid] = cleaned

    # Block submission if anything was left blank
    if unanswered_numbers:
        results_banner.hidden = True
        missing_str = ", ".join(str(num) for num in unanswered_numbers)
        validation_box.textContent = (
            f"Please answer every question before submitting. "
            f"Missing question(s): {missing_str}."
        )
        validation_box.hidden = False
        if first_missing_card is not None:
            first_missing_card.scrollIntoView()
        return

    # All questions answered — grade exact matches
    validation_box.hidden = True
    score = 0
    for question in QUESTIONS:
        qid = question["id"]
        if user_answers[qid] in question["answers"]:
            score += 1

    total = len(QUESTIONS)
    percent = round((score / total) * 100)

    # Match score percentage to the highest qualifying tier
    matched_tier = TIERS[-1]
    for tier in TIERS:
        if percent >= tier["min_percent"]:
            matched_tier = tier
            break

    # Populate and reveal the results banner
    document.querySelector("#score-display").textContent = (
        f"You scored {score} / {total} ({percent}%)"
    )
    document.querySelector("#tier-title").textContent = matched_tier["title"]
    document.querySelector("#tier-tagline").textContent = matched_tier["tagline"]
    results_banner.hidden = False
    results_banner.scrollIntoView()


render_quiz()