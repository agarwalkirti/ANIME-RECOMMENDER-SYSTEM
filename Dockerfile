## Parent image
FROM python:3.10-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Work directory inside the docker container
WORKDIR /app

## Installing system dependancies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first
COPY requirements.txt .
COPY setup.py .

## Run setup.py #--no-cache-dir for fresh start everytime no last time cache used
RUN pip install --no-cache-dir -e .
# Install Python packages
#RUN pip install --no-cache-dir -r requirements.txt

## Copying ur all contents from local to app[docker container]
COPY . .

# Used PORTS streamlit port is 8501
EXPOSE 8501

# Run the app #we can used any ip so server.address=0.0.0.0" this means run everywhere
# server.headless=true means no browser to be opened automatically
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0","--server.headless=true"]