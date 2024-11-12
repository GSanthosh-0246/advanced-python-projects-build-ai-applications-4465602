# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob

intents_msg = {
    "hours" : {
        "keywords":['hours','open','close'],
        "response":'we are open from 9AM to 5PM, Monday to Friday'
    },

    "return":{
        "keywords":['refund','return','money back'],
        "response":"I'd be happy to help you with the return process. Let me transfer you to Live agent."
    }
}

def get_response(message):
    #convert the casing to lower
    message = message.lower()

    in_message = set(message.split())
    matching_words = in_message.intersection(set(intents_msg))
    
    if any(matching_words):
        return intents_msg[matching_words.pop()]["response"]
    
    analyzer = TextBlob(message)
    sentiment = analyzer.sentiment.polarity

    if sentiment > 0 :
        return("Thats's so great to hear")
    elif sentiment < 0:
        return("I'm sorry to hear that. How can I help")
    else:
        return("I see. can you tell me more about that?")

def chat():
    print("Chatbot: How can I help you?")

    # for x in intents_msg:
    #     print(type(x),intents_msg[x]["response"])

    while(user_msg := input("You: ").strip().lower()) not in ['exit','quit','bye']:
        print(f"\nChatbot: {get_response(user_msg)}")


# Defining the ChatBot class for interaction.

            # Analyzing the sentiment of the user's message.
            

            # Generating the chatbot's response based on sentiment.
            

            # Printing the chatbot's response and sentiment.
          


if __name__ == "__main__":

    chat()
    # Creating the chatbot and starting the chat loop.
    # chatbot = ChatBot()
    # chatbot.start_chat()
