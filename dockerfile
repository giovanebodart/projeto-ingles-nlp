# ── Stage 1: dependências ────────────────────────────────────────────────────
FROM python:3.13-slim AS builder

WORKDIR /install

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --prefix=/install/deps --no-cache-dir -r requirements.txt

# ── Stage 2: runtime ─────────────────────────────────────────────────────────
FROM python:3.13-slim

WORKDIR /app

ENV PYTHONPATH=/app

# Usuário não-root
RUN addgroup --system nlp && adduser --system --ingroup nlp nlp

# Copia dependências instaladas do stage anterior
COPY --from=builder /install/deps /usr/local

# Copia o código da aplicação
COPY . .

# Baixa o modelo spaCy em build time — evita download em runtime
RUN python -m spacy download en_core_web_sm

USER nlp

EXPOSE 8000

# Workers = (2 x CPU) + 1  — ajuste conforme o host
CMD ["uvicorn", "main:app", \
     "--host", "0.0.0.0", \
     "--port", "8000", \
     "--workers", "1" ]