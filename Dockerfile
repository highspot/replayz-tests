FROM python:3.11
WORKDIR /app
COPY . /app
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
