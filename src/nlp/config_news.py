"""config_news.py.

(EDIT YOUR VERSION OF THIS FILE)

Purpose

  Store configuration values for the EVTL pipeline.

Analytical Questions

- What API endpoint should be used as the data source?
- What HTTP request headers are required?
- Where should raw and processed data be stored?

Edit your Python file to change:
- API URL (source of the JSON data),
- the HTTP Request Headers (to show your app name in the user-agent header)
- customize your output file name.
"""

import os
from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

MEDIASTACK_KEY: str = os.environ["MEDIASTACK_KEY"]

API_URL: str = (
    "https://api.apilayer.net/mediastack/v1/news"
    f"?access_key={MEDIASTACK_KEY}&limit=25&offset=0"
)

HTTP_REQUEST_HEADERS: dict[str, str] = {
    "User-Agent": "nlp-module-4-news/1.0",
    "Accept": "application/json",
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

# TODO: In your custom app, change the output file names from case_
# to something that represents YOUR custom project.
RAW_JSON_PATH: Path = RAW_PATH / "news_raw.json"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "news_processed.csv"
