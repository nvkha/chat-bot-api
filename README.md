# Chatbot-api

#### This is project using flask to build a chat bot api.A api allow user request include a question, then
#### systeam wil resonse inlude a anwser if have. 

## Issue
- Current i having problems deploy it pulic. I will deploy it as as soon as possible

## Enpoint
- POST: /api/v1/question 
- Post data:
  - input: include question.
  - question: question wait for anwser.
- Example
```
{
    "input":{
      "question": "Ai là người giàu nhất Việt Nam"
    }
}
```

## Demo 
https://user-images.githubusercontent.com/90548693/153760241-0f4a59e6-7e44-4591-9043-78449bcadc7f.mp4




## Features
- Tells the current time and/or date
- Tells the weather
- Tells the daily news 
- Answer basic questions about knowledge
- Do basic calculations
- Tells food info

## How to install 


#### Install all package 
```
$ pip install -r requirement.txt
```



## How to run
```
$ python run.py 
```
