FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY core/ ./core/
COPY synapses/ ./synapses/
COPY engine.py .

CMD ["python", "engine.py"]
