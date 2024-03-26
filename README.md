# Quran API

This is a simple API that provides the verses of the Quran. Unlike other APIs, this API doesn't require any authentication. It's free and open for everyone without any rate limits.

## Documentation

The documentation for this API can be found [here](https://quranapi.pages.dev/docs).

## How it works

This API serves static JSON files that contain the verses of the Quran. The data is taken from [Quran.com](https://quran.com). The `/api/` folder is generated at build time using a python script in `public/main.py`.
