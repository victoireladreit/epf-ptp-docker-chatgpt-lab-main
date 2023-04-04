Chat GPT project
=========

This example shows a simple Flask GPT application.

## Requirements
- `python` 3.10
- `pip`
-  (maybe)`flask` (`sudo apt-get install flask`)

Running the application
-----------------------

To run this example follow these steps:

- `pip install -r requirements.txt`
- create an account on  https://platform.openai.com/ (if you can't ask the teacher for a api-key and go to the 4th step)
- create an api-key in https://platform.openai.com/account/api-keys
- set an environment variable with key `OPENAI_KEY` and value the key you got
- run the app with `flask --app hello run`
- generate a phrase for chagpt, parsed in url from https://www.urlencoder.io/
- test with `curl 127.0.0.1:5000/chatgpt?message=YOUR_MESSAGE_PARSED_FROM_LAST_STEP` 

example:
- my phrase -> `what do you think about policy?`
- parsed -> `what%20do%20you%20think%20about%20policy%3F`
- test -> `curl 127.0.0.1:5000/chatgpt?message=what%20do%20you%20think%20about%20policy%3F`


## Labs

### Lab1 

- make this lab work locally
- create a Docker image that can run this app


### Lab2
Modify the code in the `hello.py` to do the following:
1- add a new route that will allow you to **ask to chatgpt to do some code in some programing language**. it should use the following parameters: 
  - language: the programming language to use
  - content: the code that it has to generate

