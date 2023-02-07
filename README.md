<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">National AI Challenge 2023</h3>
  <p align="center">
    Sentiment Analysis API for chatbots 
    <br />
    <a href="https://www.youtube.com/watch?v=fD_s4pTPb5M">View Demo</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#technology">Technology</a></li>
      </ul>
    </li>
    <li>
      <a href="#installation">Installation</a>
      <ul>
        <li><a href="#frontend">Frontend</a></li>
        <li><a href="#backend">Backend</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a>
      <ul>
        <li><a href="#querying-rake-nltk-+-senticgcn-service">Querying RAKE-NLTK + SenticGCN service</a></li>
        <li><a href="#getting-output-history">Getting output history</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


## About

Recently, a therapy chatbot was set up by MOE to help teachers cope with their stress. However, it drew flak online for being <a href="https://www.todayonline.com/singapore/moe-chatbot-negative-reviews-1984976">unhelpful</a> to users.

We believe that there are insights to be gained from analyzing the sentiments found in conversations between teachers and the chatbot. As such, our group has trained a model which identifies keywords and classifies teachers' emotional response to those keywords. These insights are then displayed on our dashboard, hopefully allowing MOE to gain a better understanding of some of the common problems that have been plaguing the teachers and formulate a strategy to ease the workload of teachers.



### Technology

* React
* Django REST Framework
* Rapid Automatic Keyword Extraction + SenticGCN


## Installation
To set up the project locally, we need to host both the backend and frontend servers.

### Frontend

```bash
$ cd frontend/
$ npm i
$ npm start --port 3000
```

### Backend
```bash
$ pip install -r requirements.txt
```

```bash
$ cd backend/
$ python manage.py migrate
$ python manage.py runserver
```

## Usage

* Watch the <a href="https://www.youtube.com/watch?v=fD_s4pTPb5M">demo</a> here
* We provide endpoints to be consumed at `localhost:8000/api/sentiment/`
* Full documentation can be viewed at `localhost:8000/docs/`

### Querying RAKE-NLTK + SenticGCN service
Request Syntax:
```JSON
POST /api/sentiment/ HTTP/1.1
Content-type: application/json

{
    "user_input": "Seeing my students improve gives me a sense of satisfaction."
}
```

Example Response Syntax:

```JSON
HTTP/1.1 201
Content-type: application/json

[
  {
    "time": "2022-08-24T14:15:22ZZ",
    "history_data": [
      {
        "id": 0,
        "aspect": "students",
        "emotion": 1,
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
    "time": "2022-08-24T14:15:22Z",
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
    "time": "2022-08-25T17:11:05Z",
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

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.