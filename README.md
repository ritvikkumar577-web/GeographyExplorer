# 🌍 Geography Explorer (CLI)

A beginner-friendly Python command-line project for exploring countries, capitals, continents, approximate population figures, and testing geography knowledge with a short quiz.

## Features

- List all countries included in the local dataset
- Search by country name (case-insensitive)
- Display capital, continent, and approximate population
- List continents represented in the dataset
- Play a five-question geography quiz
- Runs locally; no internet connection or third-party packages required

## Requirements

- Python 3.9 or newer
- Command Prompt, PowerShell, Terminal, or a Linux shell

## Run on Windows

1. Download or clone this repository.
2. Open Command Prompt in the project folder.
3. Run:

```bash
python geography.py
```

If `python` is not recognized, try:

```bash
py geography.py
```

## Run on Linux or macOS

```bash
python3 geography.py
```

## Example

```text
==================================
       GEOGRAPHY EXPLORER
==================================
1. Show all countries
2. Search for a country
3. Show continents
4. Take a geography quiz
5. Exit

Choose an option (1-5): 2

Enter a country name: India

Country: India
Capital: New Delhi
Continent: Asia
Population: About 1.4 billion
```

## Project structure

```text
GeographyExplorer/
├── geography.py
├── README.md
├── .gitignore
└── LICENSE
```

## Dataset note

The country list is a small sample for educational practice, not a complete world database. Population values are approximate and should not be used as official or current statistics.

## Learning outcomes

This project practices Python dictionaries, loops, functions, conditionals, user input, case-insensitive searching, and basic CLI usage.

## Future improvements

- Add more countries
- Store country data in JSON or CSV
- Add country flags and area information
- Add a high-score feature to the quiz
- Write automated tests

## License

This project is shared under the MIT License. See `LICENSE`.
