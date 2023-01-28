# National AI Challenge 2023


## Django REST Backend
```bash
$ pip install -r requirements.txt
```

```bash
$ python backend/manage.py runserver 
```

## Usage
We provide endpoints to be consumed at `localhost:8000/api/sentiment/`

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