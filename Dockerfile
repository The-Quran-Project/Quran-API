# Use the lightweight Node.js image as the base image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /

# Install Git for cloning the repository
RUN apk add --no-cache git

# Clone the repository
RUN git clone https://github.com/The-Quran-Project/Quran-API.git --depth 1 .

# Install dependencies
RUN npm install

# Build the project
RUN npm run build

# Install serve globally to use it directly
RUN npm install -g serve

# Expose the port that the application will run on
EXPOSE 3000

# Start the application using serve
CMD ["serve", "-s", "out"]
