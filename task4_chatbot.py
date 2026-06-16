# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 03:12:03 2026

@author: Administrator
"""

def chatbot():
    print("🤖 Chatbot: Hello! Mai CodeAlpha Bot hun. 'bye' likh kar exit kar sakte ho\n")
    
    while True:
        user = input("Aap: ").lower()
        
        if user == "hi" or user == "hello":
            print("Chatbot: Hello! Kya haal hai?")
        
        elif "name" in user:
            print("Chatbot: Mera naam CodeAlpha Bot hai. Aapka kya naam hai?")
        
        elif "how are you" in user:
            print("Chatbot: Mai bilkul theek! Aap sunao?")
        
        elif "python" in user:
            print("Chatbot: Python seekhna best decision hai. Loops aur functions pe focus karo.")
        
        elif "task" in user:
            print("Chatbot: Mai 3 tasks kar chuka: Hangman, Stock Tracker, aur mai khud Chatbot 😄")
        
        elif "bye" in user or "exit" in user:
            print("Chatbot: Theek hai, Allah Hafiz! Milte hain phir.")
            break
        
        else:
            print("Chatbot: Samajh nahi aaya. 'hi', 'name', 'how are you', 'python' try karo")

chatbot()