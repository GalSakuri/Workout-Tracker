# Workout Tracker

- A Python code that turns natural‑language exercise descriptions into 
logged workout rows in a Google Sheet 
- via **Nutritionix API** and **Sheety API**.

---


## What it does

1. Prompts you in the terminal — “Which exercises did you do?”
2. Sends that sentence to **Nutritionix**’s `natural/exercise` API.
3. Parses the response (duration, calories, etc.).
4. Adds one row per exercise to your personal workout sheet through **Sheety**.

The result: a timestamped workout journal without any manual data entry.

---

## Demo

```bash
$ python  v.py
Which exercises did you do? : i ran 3 km and walked 20 minutes
# Two new rows appear in your Google Sheet
```

## Quick Setup

1. **Clone & install**

```bash
git clone https://github.com/<your‑user>/workout-tracker.git
cd  Workout Tracker main.py
pip install requests
```
# Fill
- GENDER
- WEIGHT_KG
- HEIGHT_CM
- AGE

# Nutritionix
- export EXERCISE_API_ID=XXXX
  - 'XXXX' = YOUR_API_ID, in a secured env
- export EXERCISE_API_KEY=YYYY
  - 'YYYY' = YOUR_API_KEY, in a secured env
# Sheety
1. export SHEET_ENDPOINT=https://api.sheety.co/<...>/workouts
2. export SHEET_USERNAME=yourUser
3. export SHEET_PASSWORD=yourPass
- your credintals in secured env
  
python "Workout Tracker main.py"
```
prompt:  Which exercises did you do? :  i cycled 15km and did 30 min yoga
```

--- 

MIT License


