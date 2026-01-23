# ---------- Builder Stage ----------
FROM python:3.11-slim AS builder

WORKDIR /app

# Install only dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------- Runtime Stage ----------
FROM python:3.11-slim

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy only installed packages from builder
COPY --from=builder /install /usr/local

# Copy only required app files
COPY --chown=appuser:appuser main.py .

# Switch to non-root user
USER appuser

EXPOSE 8080

# The application server engine
ENTRYPOINT ["uvicorn"]

# The specific app file and network settings
CMD ["main:app", "--host", "0.0.0.0", "--port", "8080"]
