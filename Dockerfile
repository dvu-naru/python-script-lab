# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    vim \
    build-essential \
    qtbase5-dev \
    libqt5gui5 \
    libqt5widgets5 \
    libqt5core5a \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better cache)
COPY scripts/requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run the script
CMD ["python", "scripts/main.py"]