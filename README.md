# EuroCup Predictor ⚽️📊

**Author — David Carrascosa Victori**  
Full‑stack analytics platform that ingests detailed match statistics, persists them in a relational database, computes team performance aggregations, and exposes a Flask + Bootstrap UI (and JSON API) to explore data for Euro 2024 predictions.

---
## ⭐️ Core capabilities

| | |
|---|---|
| **Data ingestion** | Import raw match Python files (`/src/main/db/data/*.py`) with `insert_matches_data.py`; new matches are skipped automatically if already present. |
| **Relational model** | Normalised schema for **Matches**, **Teams**, and 6 granular stat tables (Key, Attacking, Distribution, Defending, Goalkeeping, Disciplinary). |
| **Stat engine** | Average calculators (`compute_average_stats`) and flexible aggregators (`get_team_data.py`) for any team. |
| **REST API** | `/teams`, `/team/<id>/stats`, `/team/<id>/match/<id>/stats` return JSON for front‑end or ML consumers. |
| **Web UI** | Single‑page Bootstrap interface (accordion tabs) to drill down from overall team averages ➜ individual match details. |

---
## 🗂 Repository layout

```text
futMagic/
├── src/
│   ├── main/
│   │   ├── analysis/
│   │   │   ├── get_team_data.py      # JSON summary per team
│   │   │   └── get_team_stats.py     # CLI summary printout
│   │   └── db/
│   │       ├── data/                 # raw match stat files (one module per match)
│   │       ├── insert_matches_data.py# ETL loader
│   │       ├── migrate.py            # creates tables
│   │       └── schema.py             # SQLAlchemy models
│   └── test/                         # pytest / notebooks
├── static/styles.css                 # UI styling
├── templates/index.html              # Bootstrap front end
├── app.py                            # Flask server & API routes
├── .env                              # DATABASE_URL=postgresql://…
└── requirements.txt                  # libs (SQLAlchemy, Flask, python‑dotenv…)
```

---
## 🚀 Quick start

### 1 — setup
```bash
git clone https://github.com/your‑org/eurocup‑predictor.git
cd eurocup‑predictor
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Create **.env** in project root:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/eurocup
```
Create a Postgres DB called `eurocup` (or adjust the URL).

### 2 — migrate & load sample data
```bash
python src/main/db/migrate.py               # creates tables
python src/main/db/insert_matches_data.py   # parses data/*.py ➜ inserts stats
```

### 3 — run the server
```bash
python app.py        # Flask dev server on http://127.0.0.1:5000
```
Open **http://127.0.0.1:5000** to interact with the UI.

---
## 🔌 API reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/teams` | GET | List all teams (`[{team_id, team_name}]`). |
| `/team/<team_id>/stats` | GET | Average + per‑match stats for the team. |
| `/team/<team_id>/match/<match_id>/stats` | GET | All stat categories for the team in one match. |

All responses are JSON; errors return `4xx` with `{"error": …}`.

---
## 🧮 Stat computation flow

1. **Raw rows** queried by `team_id` (and optionally `match_id`).
2. Each SQLAlchemy model → plain dict via `serialize_sqlalchemy_object`.
3. `compute_average_stats()` sums columns and divides by sample count.
4. Endpoint bundles `average_stats` and `individual_stats` into JSON.

For offline analysis, use `src/main/analysis/get_team_data.py` to obtain the same structure directly from Python.

---
## 🛠 Development tips

* **Logging** — all API routes use Python `logging`; raise to `INFO`/`DEBUG` as needed.
* **Hot reload** — `FLASK_ENV=development flask run` for auto‑reload.
* **Unit tests** — create fixtures with an in‑memory SQLite URI (`sqlite:///:memory:`) to test ETL and endpoint logic without Postgres.
* **Data updates** — drop new `*.py` files into `src/main/db/data/` and rerun `insert_matches_data.py`; duplicates are ignored.

---
## 🌍 Roadmap ideas

- xG (expected goals) and other advanced metrics tables.
- Predictive model endpoint (`/predict`) using scikit‑learn or TensorFlow.
- Caching layer (Redis) for heavy aggregate queries.
- Docker Compose with Postgres + app service.

---
## 📄 License

MIT © 2025 David Carrascosa Victori

