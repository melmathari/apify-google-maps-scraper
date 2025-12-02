# Use Apify's Python base image with Playwright
FROM apify/actor-python-playwright:3.11

# Copy requirements first for better Docker layer caching
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the actor code
COPY . ./

# Run the actor
CMD ["python", "main.py"]
