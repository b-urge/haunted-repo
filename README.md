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
