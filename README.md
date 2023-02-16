# Hello Rasa Chatbox

My first foray into Conversational AI. I am using the open source 
[Rasa Conversational Assistant](https://rasa.com/docs/rasa/)

This project consists of a React frontend UI writting in TypeScript, a Django and Django REST Framework backend,
a PostgreSQL database, and a Rasa Chat server.

If you have docker installed, you should be able to boot this up with:

```
$ docker compose up -d --build
```

Then you can have a rather rough interaction with the bot by visiting:

[http://localhost:8000/say?message=Hello](http://localhost:8000/say?message=Hello)

It's a WIP. :)
