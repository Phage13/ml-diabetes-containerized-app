# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies for scientific libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code, model, and templates from repo
COPY app.py ./app.py
COPY models ./models
COPY templates ./templates

# Expose Flask port (Heroku maps $PORT automatically)
EXPOSE 5000

# Run with gunicorn (production-ready)
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
