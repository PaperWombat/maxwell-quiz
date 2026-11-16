# Project Plan: "All About Me" Browser Quiz (V1)

## 1. Goal
Build a lightweight, client-side web app that runs entirely in the browser using only **Python** and **HTML** (no backend server, no custom JavaScript). Users answer 20 mixed multiple-choice and fill-in-the-blank questions about you and receive a final score paired with one of 4 friendship tier titles upon submission.

---

## 2. Feature Scope

### V1 Must-Have Features
1. **Hybrid Question Renderer**
   - Dynamically renders 20 questions from a central Python list into the HTML page on load.
   - Supports two question formats:
     - **Multiple-Choice (`"choice"`):** Radio buttons where one option can be selected.
     - **Text Input (`"text"`):** Single-line text boxes graded using exact matching (case-insensitive, whitespace-trimmed, with support for a list of exact acceptable aliases).
2. **Score & Tier Title Engine**
   - Blocks submission and prompts the user if any question is left unanswered.
   - Once complete, evaluates all 20 responses in Python, calculates the raw score (`X / 20`) and percentage, and maps the result to **4 friendship tiers**.
3. **Single-Page Quiz Flow**
   - Displays all 20 questions on one clean, scrollable page styled with a minimal embedded `<style>` block.
   - Includes a single **Submit** button at the bottom that reveals the score and friendship tier banner without reloading the page.

### V2 Backlog (Out of Scope for V1)
- One-question-at-a-time pagination with a live progress bar
- Post-quiz answer key highlighting missed questions and correct answers
- Randomized question/option ordering per session
- Weighted point values for harder questions
- "Play Again" reset button or shareable result card

---

## 3. File Structure & Architecture
- **`index.html`**
  - Loads PyScript (Pyodide/WebAssembly runtime) via standard CDN `<link>` and `<script>` tags.
  - Contains a minimal `<style>` block for clean spacing, readable typography, and clear visual states for the validation warning and results banner.
  - Provides semantic containers (`#quiz-questions`, `#validation-message`, `#results-banner`) and connects `main.py` via `<script type="py" src="./main.py"></script>`.
- **`main.py`**
  - Holds two easily editable data structures at the top of the file:
    - `TIERS`: 4 friendship tiers ordered from highest to lowest threshold.
    - `QUESTIONS`: 20 clean placeholder questions mixing `"choice"` and `"text"` formats.
  - Handles initial DOM generation, completeness validation on submit, exact-match answer grading, and displaying the final tier result.

---

## 4. Data Design

### Friendship Tiers (`TIERS` — 4 Levels)
| Threshold | Tier Title (Placeholder) | Tagline (Placeholder) |
| :--- | :--- | :--- |
| `85% – 100%` (17–20 pts) | **Certified Best Friend** | You practically know my brain better than I do. |
| `60% – 84%` (12–16 pts) | **Close Friend** | Solid showing—you definitely pay attention. |
| `35% – 59%` (7–11 pts) | **Casual Acquaintance** | You know the basics, time to hang out more. |
| `0% – 34%` (0–6 pts) | **Complete Stranger** | Are you sure you clicked on the right person's quiz? |

### Question Bank (`QUESTIONS` — 20 Placeholders)
Each entry in `QUESTIONS` follows a consistent dictionary schema:
```python
{
    "id": "q1",
    "type": "choice",  # or "text"
    "prompt": "What is my go-to coffee or morning drink order?",
    "options": ["Iced Latte", "Black Coffee", "Matcha", "Water"],  # omitted for "text"
    "answers": ["iced latte"],  # normalized lowercase strings; supports multiple exact aliases
}
```

---

## 5. User Flow & Local Execution
1. **Start Local Server:** Run `python -m http.server 8000` in the project folder and open `http://localhost:8000` in a browser (required so WebAssembly/PyScript can load `main.py` without `file://` CORS blocks).
2. **Render:** PyScript executes `main.py` and populates all 20 question cards into `index.html`.
3. **Validate & Grade:** Clicking **Submit** checks that all 20 questions have a selected radio button or non-empty text input:
   - **If incomplete:** Displays a clear validation alert listing unanswered question numbers and halts grading.
   - **If complete:** Hides any validation warning, grades all 20 answers, and reveals the **Results Banner** with the score (`X / 20`), percentage, tier title, and tagline.