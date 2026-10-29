# CSC 325 Module 8 — Four-stage CI/CD Pipeline

A small Django REST Framework project for a four-stage GitHub Actions demo.

## API endpoints

- `GET /api/health/` → `{"status": "ok"}`
- `GET /api/greeting/` → `{"message": "Hello from CSC 325!"}`

## Local setup (Windows PowerShell)

Run in the repository folder:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py test
python manage.py runserver
```

Then open `http://127.0.0.1:8000/api/health/` and `http://127.0.0.1:8000/api/greeting/`.

If you use another OS, create a virtual environment with `python3.12 -m venv .venv`, activate with `source .venv/bin/activate`, then run the same commands.

## Workflow

`.github/workflows/csc325_ci_cd.yml` automatically runs on pushes to `main` and `feature/**` and on pull requests to `main`. Four jobs execute sequentially:

1. **Setup** — checkout and Python setup.
2. **Dependencies** — install and check requirements.
3. **Test** — run Django tests; a failure blocks deployment.
4. **Deploy** — echo-only placeholder **on main pushes** after Test succeeds.

**Important:** The echo-only Deploy job does not host Django online or produce a public application URL. Hosting the API is an optional follow-up if a real deployed URL is required.

## Protected `main`

Configure a public repository ruleset under **Settings → Rules → Rulesets**. Target the default branch; require a pull request before merging and require the **Test** status check to pass (after a first CI run makes that check available). Do not require an approving reviewer if you have nobody available to review.

For the recorded demo, create `feature/api-version`, edit `api/views.py` and `api/tests.py` according to `VIDEO_CHANGE_GUIDE.md`, commit and push that feature branch, open a PR, then merge into `main` after checks pass. The merge triggers the final four-green-job run.

## Tutorial compatibility

The provided assignment references a Module 8 tutorial but its exact Python version and deployment provider were not included. This starter uses Python 3.12 and Django 5.2 LTS. Match the tutorial's Python version and deploy method if your instructor specifies different ones.
