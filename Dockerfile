FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 1. Copy the metadata and the source folder FIRST 
# (This fixes the 'src does not exist' error)
COPY pyproject.toml .
COPY src/ src/

# 2. Now install the project
RUN pip install .

# 3. Copy the rest of the application
COPY models/ models/
COPY data/processed/preprocessor.pkl data/processed/preprocessor.pkl
COPY api/ api/

EXPOSE 8080

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8080"]
