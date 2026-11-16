# Build Roadmap: "All About Me" Browser Quiz (V1)

A step-by-step checklist for building your local, browser-based quiz using only **HTML** and **Python** (via PyScript).

## Step 1: Set Up Project Workspace & Local Server ✅

* [x] Create a dedicated project folder containing `plan.md`, `roadmap.md`, `index.html`, and `main.py`.
* [x] Open a terminal in that directory and verify Python's built-in server runs cleanly (`python -m http.server 8000`).
* [x] Confirm `http://localhost:8000` loads in your browser without `file://` CORS restrictions.

## Step 2: Build the HTML Skeleton & PyScript Wiring (`index.html`) ✅

* [x] Add standard HTML5 boilerplate (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`).
* [x] Include the official PyScript CDN stylesheet and script tags in `<head>`.
* [x] Connect your external Python file using `<script type="py" src="./main.py"></script>`.
* [x] Create semantic containers in `<body>`:
  * Quiz header/title
  * `<form id="quiz-form">` with a `<div id="quiz-questions"></div>` container
  * Validation alert box (`<div id="validation-message" hidden></div>`)
  * Submit button (`<button type="submit">Submit Quiz</button>`)
  * Hidden results banner (`<div id="results-banner" hidden></div>`)
* [x] Load `http://localhost:8000` and confirm PyScript initializes with zero console errors.

## Step 3: Apply Minimal Embedded Styling (`index.html`) ✅

* [x] Add a lightweight `<style>` block inside `<head>` (no external CSS frameworks needed).
* [x] Style a clean, centered single-column layout (`max-width`, readable system font, comfortable line height).
* [x] Add visual card separation between the 20 questions so radio options and text boxes are easy to scan.
* [x] Style distinct visual states for `#validation-message` (warning banner) and `#results-banner` (final score and friendship tier card).

## Step 4: Define Friendship Tiers & Placeholder Questions (`main.py`) ✅

* [x] Create a `TIERS` list at the top of `main.py` with **4 friendship tiers** ordered from highest percentage threshold to lowest (`85%+`, `60%+`, `35%+`, `0%+`).
* [x] Create a `QUESTIONS` list with **20 clean placeholder questions** mixing `"choice"` (multiple-choice) and `"text"` (fill-in-the-blank) formats.
* [x] Store acceptable answers in normalized lowercase strings so future edits are quick and error-free.

## Step 5: Implement the Dynamic Question Renderer (`main.py`) ✅

* [x] Write a startup function that loops through `QUESTIONS` on page load.
* [x] For `"choice"` items, render numbered question prompts with grouped `<input type="radio">` elements.
* [x] For `"text"` items, render numbered question prompts with `<input type="text">` fields.
* [x] Inject all 20 rendered question blocks into `#quiz-questions`.

## Step 6: Build Submission Validation & Exact-Match Grading (`main.py`) ✅

* [x] Attach a Python event handler to `#quiz-form`'s submit event (preventing default page reload).
* [x] **Completeness Check:** Verify every question has either a selected radio button or a non-empty text input:
  * [x] If any question is blank, block grading and show `#validation-message` listing the unanswered question numbers.
  * [x] If all 20 are answered, hide `#validation-message` and proceed to grading.
* [x] **Exact-Match Grading:**
  * [x] Compare selected radio values directly against the stored answer.
  * [x] Normalize typed text answers (`.strip().lower()`) and check for an exact match against the question's acceptable answer list.
* [x] **Tier Calculation & Display:**
  * [x] Tally total correct answers out of 20 and compute the percentage.
  * [x] Match the percentage to the corresponding tier in `TIERS`.
  * [x] Populate and unhide `#results-banner` with the score, percentage, tier title, and tagline.

## Step 7: Test Edge Cases & Swap In Personal Content

* [ ] Test submitting with blank questions to confirm submission is blocked and the missing question numbers display accurately.
* [ ] Test text inputs with extra leading/trailing spaces and mixed capitalization (e.g., `"  IcEd LaTtE  "`) to verify exact-match normalization works.
* [ ] Test score boundaries across all **4 friendship tiers** (`0/20`, `7/20`, `12/20`, `17/20`, `20/20`).
* [ ] Replace the 20 placeholder questions and 4 tier titles in `main.py` with your real details.