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
        "fun_fact": "Fun fact: All of these games are up there in my favorites",
    },
    {
        "id": 4,
        "type": "text",
        "prompt": "What is Maxwell's favorite color?",
        "answers": ["purple"],
        "fun_fact": "Fun fact: My favorite color to WEAR is green! Purple has been my favorite my whole life",
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
        "fun_fact": "Fun fact: SWEATER SEASON!",
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
        "fun_fact": "Fun fact: His back curves twice! 12 degrees one way, 20 degrees the other, totalling in 32 degrees",
    },
    {
        "id": 11,
        "type": "choice",
        "prompt": "Who is Maxwell's current favorite youtuber?",
        "options": ["Sunlesskhan", "Wirtual", "Summoning Salt", "Matpat", "3fs", "Sideways"],
        "answers": ["3fs"],
        "fun_fact": "Fun fact: Maxwell would consider MatPat his All-Time favorite youtuber!",
    },
    {
        "id": 12,
        "type": "text",
        "prompt": "What subject did Maxwell enjoy most in school? (core)",
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
        "fun_fact": "Fun fact: Those options are actually listed in exact order of Maxwell's top artists of the last year!",
    },
    {
        "id": 15,
        "type": "choice",
        "prompt": "What is Maxwell's second favorite movie?",
        "options": ["The Batman", "Everything Everywhere All at Once", "Obsession", "The Odyssey", "The Black Phone"],
        "answers": ["everything everywhere all at once"],
        "fun_fact": "Fun fact: Those options are actually listed in exact order of Maxwell's top favorite movies!",
    },
    {
        "id": 16,
        "type": "choice",
        "prompt": "What is Maxwell's highest ever rank in Rocket League? (any game mode)",
        "options": ["Champion 1", "Champion 2", "Champion 3", "Grand Champ 1", "Grand Champ 2", "Grand Champ 3"],
        "answers": ["champion 3"],
        "fun_fact": "Fun fact: Maxwell got this rank in Rumble! His highest in the standard modes is Champion 2",
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
        "prompt": "What episode of One Piece is Maxwell currently on? (to the nearest 10) (1180 episodes total)",
        "answers": ["950", "episode 950", "ep 950"],
        "fun_fact": "Fun fact: The exact number is actually 950.",
    },
    {
        "id": 19,
        "type": "choice",
        "prompt": "What was Maxwell's favorite area on his mission?",
        "options": ["Greenwich", "Gosford", "Wollongong", "Armidale", "Sutherland", "Oakhurst", "Camden", "Prariewood"],
        "answers": ["wollongong", "armidale", "sutherland"],
        "fun_fact": "Fun fact: My three favorite are Wollongong, Armidale, and Sutherland! Though, the original quiz only counted Wollongong",
    },
    {
        "id": 20,
        "type": "text",
        "prompt": "Who is this quiz about?",
        "answers": ["maxwell", "maxwell cannon", "maxwell jenkins cannon"],
        "fun_fact": "Fun fact: My life time friend, Isaac Sam, got this one wrong.",
    },
]


# ==========================================
# 3. DYNAMIC QUESTION RENDERER (Step 5)
# ==========================================
def render_quiz():
    container = document.getElementById("quiz-questions")
    container.innerHTML = ""

    for q in QUESTIONS:
        card = document.createElement("div")
        card.className = "question-card"
        card.id = f"card-{q['id']}"

        prompt = document.createElement("p")
        prompt.className = "question-prompt"
        prompt.textContent = f"{q['id']}. {q['prompt']}"
        card.appendChild(prompt)

        if q["type"] == "choice":
            options_group = document.createElement("div")
            options_group.className = "options-group"

            for opt in q["options"]:
                label = document.createElement("label")
                label.className = "option-label"

                radio = document.createElement("input")
                radio.type = "radio"
                radio.name = f"q-{q['id']}"
                radio.value = opt.lower()

                text = document.createElement("span")
                text.textContent = opt

                label.appendChild(radio)
                label.appendChild(text)
                options_group.appendChild(label)

            card.appendChild(options_group)
        else:
            text_input = document.createElement("input")
            text_input.type = "text"
            text_input.id = f"input-q-{q['id']}"
            text_input.name = f"q-{q['id']}"
            text_input.className = "text-input"
            text_input.placeholder = "Type your answer..."
            card.appendChild(text_input)

        feedback = document.createElement("div")
        feedback.className = "question-feedback"
        feedback.id = f"feedback-{q['id']}"
        card.appendChild(feedback)

        container.appendChild(card)

    status = document.getElementById("quiz-status")
    if status:
        status.textContent = f"Quiz ready — answer all {len(QUESTIONS)} questions below!"


def get_tier(percent):
    for tier in TIERS:
        if percent >= tier["min_percent"]:
            return tier
    return TIERS[-1]


@when("submit", "#quiz-form")
def handle_submit(event):
    event.preventDefault()

    answers = {}
    missing = []

    for q in QUESTIONS:
        if q["type"] == "choice":
            selected = document.querySelector(f'input[name="q-{q["id"]}"]:checked')
            if selected:
                answers[q["id"]] = selected.value.strip().lower()
            else:
                missing.append(q["id"])
        else:
            inp = document.getElementById(f"input-q-{q['id']}")
            val = inp.value.strip().lower() if inp else ""
            if val:
                answers[q["id"]] = val
            else:
                missing.append(q["id"])

    error_box = document.getElementById("error-msg")
    banner = document.getElementById("results-banner")

    if missing:
        msg = f"Please answer all questions before submitting (missing: {', '.join(str(m) for m in missing)})."
        if error_box:
            error_box.textContent = msg
            error_box.style.display = "block"
            error_box.scrollIntoView({"behavior": "smooth", "block": "center"})
        elif banner:
            banner.innerHTML = f'<p class="error-text">{msg}</p>'
            banner.style.display = "block"
            banner.scrollIntoView({"behavior": "smooth", "block": "center"})
        return

    if error_box:
        error_box.style.display = "none"

    score = 0
    total = len(QUESTIONS)

    for q in QUESTIONS:
        user_answer = answers[q["id"]]
        card = document.getElementById(f"card-{q['id']}")
        feedback = document.getElementById(f"feedback-{q['id']}")

        card.classList.remove("incorrect", "correct")
        feedback.innerHTML = ""

        status_line = document.createElement("div")
        if user_answer in q["answers"]:
            score += 1
            card.classList.add("correct")
            status_line.textContent = "✓ Correct"
        else:
            card.classList.add("incorrect")
            status_line.textContent = "✗ Incorrect"
        feedback.appendChild(status_line)

        if q.get("fun_fact"):
            fact_line = document.createElement("p")
            fact_line.className = "fun-fact"
            fact_line.textContent = q["fun_fact"]
            feedback.appendChild(fact_line)

    percent = round((score / total) * 100)
    tier = get_tier(percent)

    tier_el = document.getElementById("tier-title")
    score_el = document.getElementById("score-display")
    tagline_el = document.getElementById("tier-tagline")

    if tier_el:
        tier_el.textContent = tier["title"]
    if score_el:
        score_el.textContent = f"You scored {score}/{total} ({percent}%)"
    if tagline_el:
        tagline_el.textContent = tier["tagline"]

    if banner:
        banner.classList.remove("hidden")
        banner.removeAttribute("hidden")
        banner.style.display = "block"
        banner.scrollIntoView({"behavior": "smooth", "block": "center"})


render_quiz()