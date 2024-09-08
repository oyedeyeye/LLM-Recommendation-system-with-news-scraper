# LLM Powered Recommendation System
Create a python's virtual environment to run the application on ubuntu or linux machine with python3 installed. run the following code

```
python3 -m venv .venv
source .venv/bin/Activate
```

## Key Components of the Project


### Data Flow
Redis (https://redis.io/) is employed as a local in-memory storage to handle the high volume of scraped data efficiently.

`docker pull redis/redis-stack`

After pulling the redis image, run it with the following command:

`docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest`

If all goes well, you should be able to access redis-stack (web interface) on https://localhost:8001

### Scraping
The application scrapes articles from Hacker News, ensuring an up-to-date repository of the latest tech news, using scrapy (https://scrapy.org/) library.

You need to install scrapy, langchain and other modules listed in the requirement document. Install using the following command.

`pip install -r requirements.txt`

### LLMs - LLAMA3.1:8b model using ollama
The LLAMA3 (https://llama.meta.com/llama3/) model processes user inputs and the scraped data to provide relevant article suggestions. 

LangChain(https://python.langchain.com/) used to integrate LLM in the application.

Download Ollama from https://ollama.com/download once done pull llama3.1:8b model

`ollama pull llama3.1:8b`

once done yoou should see it in list:
`ollama list`

You may need to serve the model with

`ollama serve`

### Prompting User Preferences
Users can express their preferences through prompts, allowing the system to tailor recommendations specifically to their interests.
You can create prompts using the `langchain.core.prompts chatPromptTemplate`

## Running the app
Use the command below to run the app

`python3 app.py`
