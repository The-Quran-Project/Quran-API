<p align="center">
  <img src="https://github.com/The-Quran-Project/Quran-API/assets/85403795/db6214cb-9c8b-4513-ba1e-429031a6a767" width="250px"/>
</p>

# Quran API

This is a simple API that provides the verses of the Quran. Unlike other APIs, this API doesn't require any authentication. It's free and open for everyone without any rate limits.

## Documentation

The documentation for this API can be found [here](https://quranapi.pages.dev/docs).

## Host it yourself

### Node.js

```bash
git clone https://github.com/The-Quran-Project/Quran-API/ --depth 1
cd Quran-API
npm i --loglevel=error
npm run build
python public/main.py
npx -y serve@latest out
```

One line command:

```bash
git clone https://github.com/The-Quran-Project/Quran-API/ --depth 1 && cd Quran-API && npm i --loglevel=error && npm run build && python public/main.py && npx -y serve@latest out
```

### Docker

```bash
docker build -t quran-api .
docker run -p 3000:3000 quran-api
```

> One line command

```bash
docker build -t quran-api . && docker run -p 3000:3000 quran-api
```

## How it works

This API serves static JSON files that contain the verses of the Quran. `/api/` folder is generated at build time.

The data is taken from [Quran.com](https://quran.com).
