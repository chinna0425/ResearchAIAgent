FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV HF_HOME=/root/.cache/huggingface

RUN python -c "from sentence_transformers import SentenceTransformer; print('Downloading model...'); SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2'); print('Model downloaded.')"

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
