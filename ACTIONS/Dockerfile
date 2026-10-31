FROM python:3.12.16-slim as builder

# Install uv using the official installer script
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /root/.local/bin/

# Add uv to the system path so we can call it directly
ENV PATH="/root/.local/bin/:$PATH"
ENV UV_PROJECT_ENVIRONMENT=/app/.venv

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev --no-install-project

FROM python:3.12.16-slim as runtime
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY . .

EXPOSE 8080
CMD ["/app/.venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]




