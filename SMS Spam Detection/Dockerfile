# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt first
COPY requirements.txt /app/

# Upgrade pip first
RUN pip install --no-cache-dir --upgrade pip 

# Force reinstall the correct numpy version first
RUN pip install --no-cache-dir --force-reinstall numpy==1.26.4

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 

# Explicitly install Gunicorn separately
RUN pip install --no-cache-dir gunicorn 

# Copy all project files into the container
COPY . /app

# Ensure numpy is correctly installed inside the container
RUN python -c "import numpy; print('Numpy Version:', numpy.__version__)"

# Expose the correct port
EXPOSE 8080

# Run the Flask app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "App:app"]
