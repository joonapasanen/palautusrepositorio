# Project Guidelines

- This is a `uv` project. Run commands as `uv run ...`; synchronize dependencies with `uv sync`.
- Start the Flask app from this directory with `uv run python src/index.py`. It runs on port 5001.
- Run Robot Framework tests with `uv run robot src/tests`. The app must be running during tests. Use `--variable HEADLESS:true` for headless runs or target a suite/test file when narrowing the run.
- The Flask routes are in `src/app.py`; templates are in `src/templates/`.
- User validation and login credential checks are in `UserService.validate` and `UserService.check_credentials` in `src/services/user_service.py`.
- User storage is an in-memory singleton in `src/repositories/user_repository.py`. Tests reset it through `POST /tests/reset`, exposed via `src/AppLibrary.py`.
- Robot Framework Browser tests are in `src/tests/`; `resource.robot` contains shared browser keywords and setup.
- Preserve user-facing validation messages and template page titles because Robot tests assert them.
