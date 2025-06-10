# TidalApiTools

Music archival tool to archive data from the tidal api using [`tidalapi`](https://github.com/tamland/python-tidal).

## Features

Extract album URLs from a playlist and save them to a text file  
Works with Python 3.11+  
Clean and simple CLI tool  
Uses OAuth login flow for TIDAL (no API keys required)

---

## Project Structure
TidalApiTools/
├── scripts/
│ └── playlistExtract.py # Main tool - extracts album URLs from a playlist
├── .gitignore
├── README.md
└── requirements.txt

---

## Setup

1. Clone the repository:
   
```
git clone https://github.com/v1sc3ra/TidalApiTools.git
cd TidalApiTools
```
2. Create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

Run the playlist extractor:
```
python3 -m scripts.playlistExtract
```
## Example Output
Example saved albums_from_playlist.txt:
```
https://tidal.com/album/123456789
https://tidal.com/album/987654321
```

## Future Plans

1. Add support for extracting artist URLs
2. Add Progress bar
3. Add support for exporting tracklists
4. Add batch album downloader integration (OrpheusDl, etc.)
5. Cache TIDAL login sessions for faster usage
