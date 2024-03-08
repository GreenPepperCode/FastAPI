# API Documentation

This API provides endpoints to fetch jokes and quotes.

## Endpoints

### Home

- `GET /`: Return a welcome message.

### Greetings

- `GET /hello/{name}`: Return a personalized greeting message.

### Jokes

- `GET /jokes`: Return a list of jokes.

### Quotes

- `GET /quotes`: Return a list of inspiring quotes.

## Models

### Joke

- `setup`: The setup of the joke.
- `punchline`: The punchline of the joke.

### Quote

- `author`: The author of the quote.
- `text`: The text of the quote.

## Example Responses

### Jokes

- `GET /jokes`