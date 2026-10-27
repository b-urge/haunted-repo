# Haunted Repo

A tiny Python trick-or-treat tracker with a deliberately haunted history.

The app records how much candy each house gives out, calculates the total and average, identifies the best house, and reports whether any house gave out zero candy.

## What is Mel?

Mel is an AI coding assistant that works directly inside a terminal. It can inspect a project, read and modify files, run tests and commands, explain bugs, and help manage development workflows such as commits and GitHub repositories.

## How This Demo Works

This project demonstrates a multi-conversation software-development workflow:

1. **Mel built the initial app.**
2. **A second conversation planted three bugs** in the implementation.
3. **A third conversation investigated the haunted behavior**, ran the tests, identified the bugs, fixed them without changing the tests, and verified that the test suite passed.
4. The corrected implementation was committed as `exorcised version`.

The tests served as the specification: they described the expected behavior and exposed the deliberately introduced defects.

## The Three Bugs

### 1. Phantom candy in the total

**Bug:** `total_candy` added one extra piece of candy to every total, including an empty list.

**Fix:** Return the sum of the candy values exactly as provided.

```python
return sum(house["candy"] for house in houses)
```

### 2. The wrong best house

**Bug:** `best_house` used `min`, so it selected the house with the least candy instead of the house with the most.

**Fix:** Use `max` with the candy count as the key.

```python
return max(houses, key=lambda house: house["candy"])
```

### 3. Empty-house crash

**Bug:** Calling `best_house([])` raised an exception because `min` and `max` cannot select an item from an empty list.

**Fix:** Return `None` when there are no houses.

```python
if not houses:
    return None
```

The report uses this result to display:

```text
Best house: No houses visited
```

## Running the App

Requires Python 3.

From the project directory, run:

```bash
python3 candy.py
```

Example output:

```text
🎃 Trick-or-Treat Candy Report 🎃
Total candy: 78 pieces
Average per house: 15.6 pieces
Best house: Graveyard Gate (31 pieces)
This house is haunted!
```

## Running the Tests

Run the complete test suite with:

```bash
python3 -m unittest
```

The tests cover:

- Candy totals
- Average candy per house
- Best-house selection
- The zero-candy haunted warning
- Empty input handling

## Project Files

- `candy.py` — Application logic and command-line entry point
- `test_candy.py` — Unit tests

## Hackathon

This demo was made for the [Trick or Build hackathon](https://luma.com/wp7gehbn).

## The haunted house story

The haunted house story explains the metaphor used in this project. candy.py is the house, the bugs are ghosts, test_candy.py is the ghost detector, a fresh Mel conversation is the exorcist, and the Code review panel is the proof. The app also features a warning: "This house is haunted!" when a house gives zero candy.

## How the app works

- Houses are stored as a list of dictionaries in candy.py, each with a name and a candy count.
- Total candy is the sum of all candy values.
- Average candy per house is the total divided by the number of houses; if there are zero houses, the average is undefined and handled gracefully.
- Best house is the one with the maximum candy value.
- If any house has zero candy, the app prints a warning message: "This house is haunted!" for that house.
- If the list of houses is empty, the app handles it by returning None for best_house and showing a corresponding message.

Example of report output:

```text
🎃 Trick-or-Treat Candy Report 🎃
Total candy: 0 pieces
Average per house: 0.0 pieces
Best house: No houses visited
This house is haunted!
```

## The three ghosts

Below are the three bugs (the "ghosts"), what each did, why it was wrong, and the exact fix shown as a small before/after snippet pulled from the repository diff.

### Ghost 1 — Phantom candy in the total

What it did
- `total_candy` added one extra piece of candy to every total.

Why it was wrong
- The function should return the exact sum of candy values provided by the houses.

Before (haunted):

```python
def total_candy(houses):
    """Return the total candy given by all houses."""
-    return sum(house["candy"] for house in houses) + 1
```

After (exorcised):

```python
def total_candy(houses):
    """Return the total candy given by all houses."""
+    return sum(house["candy"] for house in houses)
```

---

### Ghost 2 & 3 — Wrong best house & Empty-house crash

What they did
- `best_house` used `min`, selecting the house with the least candy instead of the most, and crashed when called with an empty list.

Why it was wrong
- The best house must be the one with the maximum candy count. Also, selecting from an empty list raises an exception; the function should return `None` for empty input so the caller can handle it gracefully.

Before (haunted):

```python
def best_house(houses):
    """Return the house that gave the most candy, or None if empty."""
-    return min(houses, key=lambda house: house["candy"])
```

After (exorcised):

```python
def best_house(houses):
    """Return the house that gave the most candy, or None if empty."""
+    if not houses:
+        return None
+    return max(houses, key=lambda house: house["candy"])
```

---

## Why Mel is a standout tool for this

1) Mel investigated from a vague bug report instead of being told where the bugs were.
2) Mel used the tests to prove its fixes instead of guessing.
3) Mel asked for approval before every edit.
4) Mel showed every change in the Code review panel so a human can verify the work.
5) Mel kept the terminal, agent and review in one window.
6) Mel ran three separate conversations (build, haunt, exorcise) with memory turned off so the exorcist couldn’t cheat.

