FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy metadata and source first
COPY pyproject.toml .
COPY src/ src/

# --- CHANGE 1: Add streamlit and requests to the install ---
RUN pip install . joblib scikit-learn streamlit requests

# --- GENERATE MODELS (Keep your working logic) ---
RUN mkdir -p models data/processed && \
    python -c "import joblib; from sklearn.ensemble import RandomForestClassifier; from sklearn.preprocessing import StandardScaler; joblib.dump(RandomForestClassifier().fit([[0,0,0,0,0]], [0]), 'models/model.pkl'); joblib.dump(StandardScaler().fit([[0,0,0,0,0]]), 'data/processed/preprocessor.pkl')"

# Copy the API and UI code
COPY api/ api/

# --- CHANGE 2: Expose both ports (API and UI) ---
EXPOSE 8080
EXPOSE 8501

# --- CHANGE 3: Run both services simultaneously ---
# We run FastAPI in the background (&) and Streamlit in the foreground
CMD ["sh", "-c", "uvicorn api.app:app --host 0.0.0.0 --port 8080 & streamlit run api/ui.py --server.port 8501 --server.address 0.0.0.0"]
