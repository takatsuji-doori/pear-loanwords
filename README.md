# PearEditor

Loanword dictionary and romaji override editor for [Pear](https://github.com/th-ch/youtube-music) YouTube Music romanization plugin.

## What this does

- Converts katakana loanwords to their original language spelling in romanized lyrics
- Allows manual override of katakana words, romaji spacing, and Japanese phrases
- Collects unknown words for manual review via a web UI

## Files

- `pear-server.py` — Local API server (runs on localhost:8765)
- `pear-unknown-viewer.html` — Web UI for reviewing and editing overrides
- `pear-data.json` — Override dictionary (community-maintained)
- `generate_patch.py` — Patch generator for youtube-music.iife.js

## Setup

1. Install [YouTube Music Desktop App](https://github.com/th-ch/youtube-music)
2. Set your Gemini API key: `export GEMINI_API_KEY="(YOUR_GEMINI_API_KEY)"`
3. Run `python3 pear-server.py`
4. Open `http://localhost:8765/pear-unknown-viewer.html`

## Data sources

- [JMdict](https://www.edrdg.org/jmdict/j_jmdict.html) — Japanese dictionary (CC BY-SA 4.0)
- [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) — English loanwords in Japanese
- [google-ime-user-dictionary-ja-en](https://github.com/tokuhirom/google-ime-user-dictionary-ja-en) — Google IME katakana dictionary

## License

MIT
