import requests
import os
import openai

class ChatBot:

    def __init__(self):
        pass

    def welcomemessage(self):
        self.art = """      #                                     #                             
      # # #####  #####  ###### #####        #   ##   #####  ###### #####  
      # # #    # #    # #      #    #       #  #  #  #    # #      #    # 
      # # #####  #####  #####  #    #       # #    # #####  #####  #    # 
#     # # #    # #    # #      #####  #     # ###### #    # #      #####  
#     # # #    # #    # #      #   #  #     # #    # #    # #      #   #  
 #####  # #####  #####  ###### #    #  #####  #    # #####  ###### #    # """
        print(self.art)
        print(f"\nAuthor:{self.author()}")
        print("Enter your query or type 'exit' to exit.")
        print("\n\nWelcome!\nHow can I help you today?")


    def author(self):
        return "Srijan Dutta"

    def bot(self, message):
        openai.api_key = os.environ('OPENAI_API_KEY')
        response = openai.Completion.create(model="text-davinci-003", prompt=message, temperature=1, max_tokens=15)
        return response
    
    def keep_running(self):
        message = input("==>")
        while not(message.lower() == "exit"):
            output = self.bot(message)
            print(output)
            message = input("==>")
        
if __name__ == "__main__":
    bot = ChatBot()
    bot.welcomemessage()
    bot.keep_running()
