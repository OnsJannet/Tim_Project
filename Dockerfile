# Use a multi-stage build to reduce final image size
FROM python:3.9.19-slim-bookworm

# Set build-time environment variables
ENV DEBIAN_FRONTEND="noninteractive" \
    PYTHONUNBUFFERED="true" \
    TOKENIZERS_PARALLELISM="true" \
    FLASK_DEBUG="false" \
     FLASK_APP=TIM_Flask/app.py \
     FLASK_SKIP_DOTENV="true"

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ git gfortran gnupg2 wget ca-certificates \
    rsync libffi-dev \
    libmagickwand-dev libpq-dev pkg-config poppler-utils \
    tesseract-ocr ffmpeg libsm6 libxext6 \
    apt-transport-https curl && \
    # Clean up
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Create app directory and install Python dependencies
WORKDIR /app
COPY TIM_Flask/requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Copy application code
COPY . .
# Expose port
EXPOSE 5000
WORKDIR /app/TIM_Flask
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
#CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]
