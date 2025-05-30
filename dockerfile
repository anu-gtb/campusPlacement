FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY backend.py /app/
COPY scaler/scaler.pkl /app/
COPY model/model.pkl /app/
COPY app.py /app/

EXPOSE 8501

CMD ["streamlit","run","app.py"]