FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY . .

RUN uv sync --no-dev

ENV PATH="/app/.venv/bin:$PATH"

CMD ["streamlit", "run", "app.py"]