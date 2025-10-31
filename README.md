# Flask + Docker + GitHub Actions + Dependabot

Simple Flask app that reads two environment variables:

- `APP_MESSAGE` (shown on `/`)
- `APP_HEALTH` (returned from `/health`)

## Run locally with Docker Compose

```bash
cp .env.example .env
docker compose up --build
```

Visit:
- Home: http://localhost:5000/ -> shows `APP_MESSAGE`
- Health: http://localhost:5000/health -> shows `APP_HEALTH`

## GitHub Actions

Workflow builds the image and runs the container. It also creates a `.env` file from GitHub secrets.
Required repo secrets:
- `APP_MESSAGE`
- `APP_HEALTH`

## Dependabot

Weekly checks for:
- `pip` (Python)
- `docker`
- `github-actions`
