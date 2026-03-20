# Instagram Follower Checker

A simple Python script that compares your Instagram followers and following to find who doesn't follow you back.

## How It Works

Loads your exported Instagram data from two JSON files, converts them to sets, and uses set difference to find accounts you follow that don't follow you back in O(n) time.

## Requirements

- Python 3.x
- Your Instagram data export (JSON format)
    - following.json
    - followers_1.json

## Getting Your Instagram Data

1. Go to **Instagram > Settings > Your activity > Export your information > Export to Device**
2. Set "Date Range" to **All time**
3. Select **JSON** as the format
4. Request the download and wait for the email
5. Extract the ZIP — you'll find `following.json` and `followers_1.json` inside the `connections/followers_and_following/` folder

For faster export, unselect all information except **Followers and Following** under **Connections**

## Usage

1. Place `following.json` and `followers_1.json` in the same directory as the script
2. Run:

```bash
python instagram.py
```
or on MacOS
```bash
python3 instagram.py
```

## Example Output

```
3 people don't follow you back:
f1
coldplay
lewishamilton
```

## File Structure

```
instagram-checker/
├── instagram.py
├── following.json
├── followers_1.json
└── README.md
```

## Notes

- The script reads `relationships_following` from `following.json` and `string_list_data[0].value` from `followers_1.json` — this matches Instagram's current export format, but may change if Instagram updates their data structure
- Deactivated or deleted accounts will show up as not following you back, since there's no way to distinguish them without hitting Instagram's API
