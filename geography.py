#!/usr/bin/env python3
"""Geography Explorer: a beginner-friendly command-line geography project."""

COUNTRIES = {
    "India": {"capital": "New Delhi", "continent": "Asia", "population": "About 1.4 billion"},
    "Japan": {"capital": "Tokyo", "continent": "Asia", "population": "About 124 million"},
    "China": {"capital": "Beijing", "continent": "Asia", "population": "About 1.4 billion"},
    "France": {"capital": "Paris", "continent": "Europe", "population": "About 68 million"},
    "Germany": {"capital": "Berlin", "continent": "Europe", "population": "About 84 million"},
    "Brazil": {"capital": "Brasilia", "continent": "South America", "population": "About 203 million"},
    "Argentina": {"capital": "Buenos Aires", "continent": "South America", "population": "About 46 million"},
    "Egypt": {"capital": "Cairo", "continent": "Africa", "population": "About 113 million"},
    "Kenya": {"capital": "Nairobi", "continent": "Africa", "population": "About 55 million"},
    "Australia": {"capital": "Canberra", "continent": "Oceania", "population": "About 27 million"},
    "New Zealand": {"capital": "Wellington", "continent": "Oceania", "population": "About 5 million"},
    "Canada": {"capital": "Ottawa", "continent": "North America", "population": "About 41 million"},
    "United States": {"capital": "Washington, D.C.", "continent": "North America", "population": "About 340 million"},
}

def show_countries():
    print("\nCountries in the database:")
    for name in sorted(COUNTRIES):
        print(f" - {name}")

def search_country():
    name = input("\nEnter a country name: ").strip()
    # Case-insensitive lookup while preserving names with spaces.
    match = next((country for country in COUNTRIES if country.casefold() == name.casefold()), None)
    if not match:
        print("Country not found. Try option 1 to see available countries.")
        return
    details = COUNTRIES[match]
    print(f"\nCountry: {match}")
    print(f"Capital: {details['capital']}")
    print(f"Continent: {details['continent']}")
    print(f"Population: {details['population']}")
    print("\nNote: Population figures are approximate and included for learning purposes.")

def show_continents():
    continents = sorted({info["continent"] for info in COUNTRIES.values()})
    print("\nContinents represented in this project:")
    for continent in continents:
        count = sum(1 for info in COUNTRIES.values() if info["continent"] == continent)
        print(f" - {continent} ({count} countries)")

def geography_quiz():
    questions = [
        ("What is the capital of India?", "new delhi"),
        ("What is the capital of Japan?", "tokyo"),
        ("What is the capital of France?", "paris"),
        ("What is the capital of Egypt?", "cairo"),
        ("What is the capital of Canada?", "ottawa"),
    ]
    score = 0
    print("\nGeography Quiz — enter the capital city.")
    for question, answer in questions:
        guess = input(question + " ").strip().casefold()
        if guess == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. Answer: {answer.title()}")
    print(f"\nYour score: {score}/{len(questions)}")

def main():
    while True:
        print("\n" + "=" * 34)
        print("       GEOGRAPHY EXPLORER")
        print("=" * 34)
        print("1. Show all countries")
        print("2. Search for a country")
        print("3. Show continents")
        print("4. Take a geography quiz")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()
        if choice == "1":
            show_countries()
        elif choice == "2":
            search_country()
        elif choice == "3":
            show_continents()
        elif choice == "4":
            geography_quiz()
        elif choice == "5":
            print("Thanks for exploring geography. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram closed. Goodbye!")
