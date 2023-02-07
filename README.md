# National AI Challenge 2023

## Testing our project

## React Framework Frontend

```bash
$ npm install
```
```bash
$ npm start
```

## Django REST Backend
```bash
$ pip install -r requirements.txt
```

```bash
$ python backend/manage.py runserver 
```

We provide endpoints to be consumed at `localhost:8000/api/sentiment/`
Full documentation can be viewed at `localhost:8000/docs/`

### Querying RAKE-NLTK + SenticGCN service
Request Syntax:
```JSON
POST /api/sentiment/ HTTP/1.1
Content-type: application/json

{
    "user_input": "This is an example of a natural language input!"
}
```

Example Response Syntax:

```JSON
HTTP/1.1 201
Content-type: application/json

[
  {
    "time": "2019-08-24T14:15:22Z",
    "history_data": [
      {
        "id": 0,
        "aspect": "string",
        "emotion": -1,
        "history": 0
      }
    ]
  }
]
```

### Getting output history

Request Syntax:
```JSON
GET /api/sentiment/ HTTP/1.1
```

Example Response Syntax:
```JSON
HTTP/1.1 201
Content-type: application/json

[
  {
    "time": "2019-08-24T14:15:22Z",
    "history_data": [
      {
        "id": 0,
        "aspect": "string",
        "emotion": -1,
        "history": 0
      }
    ]
  },
  {
    "time": "2019-08-25T17:11:05Z",
    "history_data": [
      {
        "id": 0,
        "aspect": "string",
        "emotion": 1,
        "history": 1
      }
    ]
  }
]
```
