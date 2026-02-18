# STEP 1: Choose base image
FROM python:3.9-slim

# STEP 2: Set working directory
WORKDIR /app

# STEP 3: Copy files
COPY . .

# STEP 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# STEP 5: Expose port
EXPOSE 5000

# STEP 6: Run app
CMD ["python", "app.py"]
