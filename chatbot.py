

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
        print("\n\nWelcome!\nHow can I help you today?")

    def author(self):
        return "Srijan Dutta"