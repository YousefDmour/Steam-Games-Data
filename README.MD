# Steam Games Data

A small Python project that collects Steam game statistics from [SteamDB](https://steamdb.info/) and stores the results as CSV files.

## What it collects

The scripts in `scrapers/` target these SteamDB pages:

| Script | Source | Data collected |
| --- | --- | --- |
| `most_played_games.py` | Steam charts | Current players, 24-hour peak, and all-time peak |
| `hot_releases.py` | Game ratings | Ranked games, prices, discounts, ratings, release dates, followers, reviews, and peak players |
| `popular_releases.py` | Game ratings sorted by peak players | Ranked games, prices, discounts, ratings, release dates, followers, reviews, and peak players |
| `Trends_games.py` | Trending followers | Ranked games, prices, discounts, ratings, release dates, followers, and seven-day follower gain |

The current CSV snapshots are stored in `data/`.

## Requirements

- Python 3.10 or newer
- Google Chrome
- A compatible ChromeDriver. Recent Selenium versions can usually manage the driver automatically, but Chrome must be installed.
- Network access to SteamDB

## Setup

From the project root, create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running a scraper

Run commands from the project root so the relative `data/` paths resolve correctly:

```bash
python scrapers/most_played_games.py
python scrapers/hot_releases.py
python scrapers/popular_releases.py
python scrapers/Trends_games.py
```

The scripts open Chrome, load the relevant SteamDB page, select all available rows, and collect the visible table data. The exporting scripts write CSV files to `data/` using date-based filenames defined in each script. `Trends_games.py` currently builds its dataframe in memory without exporting a new CSV file; the existing trends snapshot is retained in `data/`.

Because the scripts use Selenium and live website selectors, they may need updates if SteamDB changes its page structure. SteamDB may also limit automated requests, so use the scrapers responsibly and follow the site's terms of use.

## Project structure

```text
.
├── data/                 # CSV snapshots
├── scrapers/             # SteamDB collection scripts
├── requirements.txt      # Python dependencies
└── README.MD
```
