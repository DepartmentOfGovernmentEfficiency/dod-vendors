# DoD Vendor Vendor Fetcher

This Python script fetches and displays Department of Defense (DoD) vendors with contracts over $25,000 USD from the USASpending API in a colorful command-line interface (CLI). It retrieves data live, page by page, up to 50 pages (5,000 vendors), with 100 vendors per page.

## Features
- Fetches vendor data (name, award amount, award ID) in real-time.
- Filters awards to ensure they exceed $25,000 USD.
- Displays vendors with vibrant colors using `colorama`.
- Paginates through 50 pages with user input ('n' for next, 'q' to quit).

## Usage

Run the script:

```python3
python dod_vendors.py
```
Follow the prompts:

```bash
n: Fetch the next page of vendors.
q: Quit the script.
The script stops automatically after page 50 (5,000 vendors).
```
This is what the results should look like when running it: 

https://github.com/user-attachments/assets/1b378dc4-d7e6-48f6-9655-22ef8401cf6d

## Author 

_Michael Mendy (c) 2025._
