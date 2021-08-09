FROM python:3.9.1
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install -r requirements.txt --no-cache-dir
COPY . .
