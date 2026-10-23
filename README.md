# Meet Max — The 100-Year-Old Cat 🐱

A small website about Max, built with Python and Flask. It uses the supplied information only:

- Name: Max
- Age: 100 years
- Discovery: Scientists found out yesterday that Max lived 100 years.

## Run locally

1. Install Python.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the site:

   ```bash
   python app.py
   ```

4. Open http://127.0.0.1:5000 in your browser.

## Deployment

The included `Procfile` uses Gunicorn for hosts that support Flask apps. Add `gunicorn` to `requirements.txt` before deploying to such a host.
