FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy metadata and source first
COPY pyproject.toml .
COPY src/ src/

# Install the project
RUN pip install . joblib scikit-learn

# --- NEW: GENERATE MODELS IF THEY DON'T EXIST ---
# This ensures Render always has a 'brain' to load
RUN mkdir -p models data/processed && \
    python -c "import joblib; from sklearn.ensemble import RandomForestClassifier; from sklearn.preprocessing import StandardScaler; joblib.dump(RandomForestClassifier().fit([[0,0,0,0,0]], [0]), 'models/model.pkl'); joblib.dump(StandardScaler().fit([[0,0,0,0,0]]), 'data/processed/preprocessor.pkl')"

# Copy the API code
COPY api/ api/

EXPOSE 8080

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8080"]
