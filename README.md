# InBetween Sets

**CSC 461 semester project. Track 1: Learn a New Language + Build an Application.**
Author: Nolan Gall

InBetween Sets is a workout logger and short-video feed combined in one app. After a set, you log the exercise, weight and reps with a few taps, and that starts a rest timer. While you rest you can scroll a vertical feed of short fitness clips. When the rest period ends, a "Rest over" banner appears without stopping the video, and one tap takes you back to the logger. The app also keeps your workout history and shows a progress chart for each exercise.

## Tech stack

| Purpose | Tool |
|---|---|
| Language | Python 3.12+ (new to me, which is the point of Track 1) |
| UI framework | [Flet](https://flet.dev/docs/) (desktop app, phone-sized window) |
| Storage | SQLite (Python's built-in `sqlite3` module) |
| Video clips | [Pexels API](https://www.pexels.com/api/) (free, licensed stock video) |
| HTTP | `requests` |
| Testing | `pytest` |

## How to run

```bash
# 1. Clone the repo and move into it
git clone https://github.com/<your-username>/inbetween-sets.git
cd inbetween-sets

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Pexels API key
copy .env.example .env         # Windows (use `cp` on macOS / Linux)
# then open .env and paste your key

# 5. Run the app
python main.py

# 6. Run the tests
pytest
```

## Project structure

```
inbetween-sets/
├── main.py              # Flet entry point: window setup and navigation
├── models.py            # Dataclasses: Exercise, WorkoutSet
├── db.py                # SQLite setup and queries
├── views/
│   ├── log_view.py      # Log a set (exercise, weight, reps)
│   ├── timer_view.py    # Rest timer
│   ├── feed_view.py     # Vertical short-video feed
│   └── history_view.py  # Workout history and progress charts
├── tests/               # pytest unit tests
├── docs/                # Wireframes, learning log, status reports
├── requirements.txt
└── .env.example         # Template for the Pexels API key (the real .env is not committed)
```

## Timeline

| Weeks | Milestone | Status |
|---|---|---|
| 1–2 | Learn Python basics, set up Flet, sketch the screens | In progress |
| 3–4 | Workout logger saved to SQLite | Not started |
| 5–6 | Rest timer with banner alert; video feed from Pexels | Not started |
| 7–8 | History and progress charts; pytest unit tests | Not started |
| 9–10 | Performance testing, usability study, final report | Not started |
