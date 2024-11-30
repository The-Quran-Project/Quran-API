FROM node:18-alpine

RUN apk add --no-cache git python3

WORKDIR /app

RUN git clone https://github.com/The-Quran-Project/Quran-API . --depth 1

RUN npm i --loglevel=error
RUN npm i serve -g --loglevel=error
RUN python3 public/main.py
RUN npm run build

EXPOSE 3000

# Start the application using serve
CMD ["serve", "out"]