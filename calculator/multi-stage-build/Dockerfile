#### Build stage ####
FROM ubuntu AS build

WORKDIR /app

COPY calculator.py /app

RUN apt update && apt install -y python3 python3-pip

#### Final stage ####
FROM python:3-slim

# Ensure that /app directory exists in the final image
WORKDIR /app

# Copy the Python script from the build stage
COPY --from=build /app/calculator.py /app/

# Set the ENTRYPOINT and CMD to run the Python script
ENTRYPOINT ["python3"]
CMD ["calculator.py"]

