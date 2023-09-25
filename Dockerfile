FROM python:3.8-alpine

# Copy the requirements file into the image
COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

# Install the dependencies specified in the requirements file
RUN pip install -r requirements.txt

# Copy app contents to the image
COPY app/ /app

ENTRYPOINT [ "python" ]

CMD ["app.py" ]

