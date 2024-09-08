from langchain_community.llms import Ollama


class Llama3_1Processor:
    def __init__(self):
        self.ollama = Ollama(model="llama3.1:8b")

    def process(self, text):
        return self.ollama.invoke(text)
