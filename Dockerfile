# Use slim Python image for build stage
FROM python:3.10-slim AS builder

# Set working directory for the build process
WORKDIR /app

# Install only essential build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt
COPY requirements.txt .

# Install Python dependencies with optimizations
RUN pip install --no-cache-dir --no-compile -r requirements.txt

# Copy application files
COPY *.py ./
COPY jinadb/ ./jinadb/

# Final stage - use even smaller base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install only runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages and application files from builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app/*.py ./
COPY --from=builder /app/jinadb ./jinadb

# Create volume for vector store data
VOLUME ["/app/jinadb"]

# Create startup script with debug information
RUN echo '#!/bin/bash\n\
echo "Current directory: $(pwd)"\n\
echo "Listing files in current directory:"\n\
ls -la\n\
echo "Checking jinadb directory:"\n\
ls -la jinadb/ || echo "jinadb directory is empty (this is normal on first run)"\n\
\n\
streamlit run frontend.py --server.port=8501 --server.address=0.0.0.0' > /app/start.sh && \
chmod +x /app/start.sh

# Cleanup Python cache and temporary files
RUN find /usr/local/lib/python3.10/site-packages -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true && \
    find /usr/local/lib/python3.10/site-packages -type f -name "*.pyc" -delete && \
    rm -rf /root/.cache

# Expose Streamlit port
EXPOSE 8501

# Command to run the application
CMD ["/app/start.sh"]
