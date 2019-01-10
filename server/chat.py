from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Chat:

    def __init__(self, trainflag=False):
        self.chatbot = ChatBot('chatty')

        if trainflag:
            self.trainer = ChatterBotCorpusTrainer(self.chatbot.storage)
            self.trainer.train("chatterbot.corpus.english")

    def get_response(self, question):
        response = self.chatbot.get_response(question)
        return response
