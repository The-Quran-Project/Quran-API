# Use the lightweight Node.js image as the base image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Install Git and Python3
RUN apk add --no-cache git python3

RUN git clone https://github.com/The-Quran-Project/Quran-API.git . --depth 1

RUN npm i --loglevel=error

RUN npm run build

RUN python3 public/main.py

RUN npm i -g serve

EXPOSE 3000

# Start the application using serve
CMD ["serve", "-s", "out"]
