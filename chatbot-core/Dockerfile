FROM python:3.13
WORKDIR /src
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]