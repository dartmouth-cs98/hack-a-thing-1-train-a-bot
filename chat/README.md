# TRAIN A BOT

![screenshot](./screenshot.png)

For this hackathon I decided to tackle functional programming using Elixir. I set out thinking of ideas of what I could build in Elixir. Having some experience in web design, I thought it would be interesting to build a web app in Elixir. I've always wanted to write a chatbot, so I decided to write a realtime chat with a chatbot app. 

Train-A-Bot is a webapp that allows you to chat with a chatbot. Chats with the bot are saved and used to train it.

I followed the following tutorial to build the web app using Elixir and Phoenix: https://github.com/dwyl/phoenix-chat-example

This provided a detailed roadmap to using Phoenix as a web framework and using Elixir to power it. In addition, this tutorial uses PostgreSQL which I have not used before. I found it to be very intuitive and I'm a big fan of the pgAdmin dashboard.

I modified the program in several ways. I completely redesigned the front-end to have an iOS feel. I used https://codepen.io/samuelkraft/pen/Farhl as a base for the message bubbles, but modified them slightly to fit better with my design. I removed the "name" feature and made it a 1-1 chat with a bot vs. a live chat between many individuals. I also added code here to query the Python microservice that was running my chatbot. After receiving input from the front-end, the Elixir controller would insert the record into the DB (for training at a later time), echo the output to the chat, and would pass the input to the microservice, echoing the result when it is received. 


