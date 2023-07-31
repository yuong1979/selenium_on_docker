# Use an official Python runtime as a parent image
FROM python:3.9-alpine3.15

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Update packages and Install Chromium and Chromedriver
RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
        chromium \
        chromium-chromedriver \
        python3-dev \
        gcc \
        libc-dev \
        libffi-dev \
        openssl-dev \
        musl-dev \
        cargo

# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 3000

# # Define environment variable
# ENV NAME World

# # Run app.py when the container launches
CMD ["python", "index.py"]
# CMD python ./index.py
# CMD ["python", "-u", "index.py"]



# # sudo apt update && sudo apt -y upgrade && sudo apt -y autoremove
# # wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# # sudo apt -y install ./google-chrome-stable_current_amd64.deb






