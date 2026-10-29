# Video demonstration: make this change AFTER the initial project is pushed

The files in this zip contain the **before** version. Keep the following change uncommitted until you record your video.

## 1. After the first green baseline run, protect main

GitHub repo → Settings → Rules → Rulesets → New branch ruleset.
Set enforcement to Active, target default branch, require PR and a passing Test check. No reviewer required for a solo demo.

## 2. Create the demo branch before recording

```powershell
git switch -c feature/api-version
```

## 3. Edit `api/views.py` for the video

Change only the `return Response` in `greeting` from:

```python
return Response({"message": "Hello from CSC 325!"})
```

to:

```python
return Response({"message": "Hello from CSC 325!", "version": "2"})
```

## 4. Add this third test at the end of `ApiEndpointTests` in `api/tests.py`

```python
    def test_greeting_includes_version(self):
        response = self.client.get("/api/greeting/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["version"], "2")
```

Check indentation: method is inside the class, aligned with the other `def test_...` methods.

## 5. Record, test, commit, and push on camera

```powershell
python manage.py test
git add api/views.py api/tests.py
git commit -m "Add version field to greeting API"
git push -u origin feature/api-version
```

Open a pull request from `feature/api-version` to `main`. The branch push starts the workflow, but its Deploy stage is skipped by design. Once the PR checks pass, merge the PR into main on camera. That merge triggers the run with **all four jobs green**.

## 6. Suggested <=5-minute narrated sequence

- 0:00–0:30 — Introduce name and show GitHub repo URL.
- 0:30–1:10 — Open the YAML; point out triggers and four named jobs, including `needs: test`.
- 1:10–2:00 — Show/edit the API change and new test; run local tests (3 tests pass).
- 2:00–2:35 — Commit and push feature branch while recording.
- 2:35–3:10 — Show the triggered Actions run and PR; merge PR after the check passes.
- 3:10–4:20 — Cut out waiting; show new main run and open each job log, including Deploy.
- 4:20–5:00 — Show the deployed result. For the permitted echo-only option, show the Deploy log and explain it is a placeholder; it is not a public running Django URL.

**If a real application URL is required**, connect a hosting provider and replace Deploy with its actual deployment steps. The echo-only baseline won't meet a literal live-URL requirement.
