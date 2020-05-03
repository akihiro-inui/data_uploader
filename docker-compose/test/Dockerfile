# Use latest ubuntu
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install python3 python3-pip -y

RUN apt-get clean \
    && apt-get -y update

# Environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1
ENV DEPLOYMENT 'test'

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# COPY stuff, directory path setting
COPY . .
WORKDIR .
ENV PYTHONPATH .

# Port forward
EXPOSE 8000