#!/usr/bin/env python3
"""A tiny trick-or-treat candy tracker."""


HOUSES = [
    {"name": "Pumpkin Manor", "candy": 24},
    {"name": "The Spooky Cottage", "candy": 0},
    {"name": "Witch's Hollow", "candy": 15},
    {"name": "Graveyard Gate", "candy": 31},
    {"name": "Batwing Bungalow", "candy": 8},
]


def total_candy(houses):
    """Return the total candy given by all houses."""
    return sum(house["candy"] for house in houses)


def average_candy(houses):
    """Return the average candy per house, or 0 for no houses."""
    if not houses:
        return 0
    return total_candy(houses) / len(houses)


def best_house(houses):
    """Return the house that gave the most candy, or None if empty."""
    if not houses:
        return None
    return max(houses, key=lambda house: house["candy"])


def report(houses):
    """Build a Halloween-themed report for the supplied houses."""
    lines = [
        "\n🎃 Trick-or-Treat Candy Report 🎃",
        f"Total candy: {total_candy(houses)} pieces",
        f"Average per house: {average_candy(houses):.1f} pieces",
    ]

    winner = best_house(houses)
    if winner is None:
        lines.append("Best house: No houses visited")
    else:
        lines.append(f"Best house: {winner['name']} ({winner['candy']} pieces)")

    if any(house["candy"] == 0 for house in houses):
        lines.append("This house is haunted!")

    return "\n".join(lines)


def main():
    print(report(HOUSES))


if __name__ == "__main__":
    main()
