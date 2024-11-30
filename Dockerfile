# Use the lightweight Node.js image as the base image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Install Git for cloning the repository
RUN apk add --no-cache git

RUN git clone https://github.com/The-Quran-Project/Quran-API.git . --depth 1

RUN npm i --loglevel=error

RUN npm run build

RUN npm i -g serve

EXPOSE 3000

# Start the application using serve
CMD ["serve", "-s", "out"]
