FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.5.30 /uv /uvx /bin/

COPY . /app

WORKDIR /app
RUN uv sync --frozen

CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]