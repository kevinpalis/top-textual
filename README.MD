# TOP-TEXTUAL

A simple Textual-based app that mimics the Linux `top` command by displaying a table refreshed every 10 seconds with `ps aux` output.


## Features
- Refreshes every 10 seconds (customizable)
- Customizable data source
- Dark/light mode toggle
- Separate CSS styling

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Customize Refresh Interval or Data Source
Modify `app.py` or `process_table.py` to change the interval or plug in a different data source function.
