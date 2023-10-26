# InstaGPT

https://github.com/dfong0530/UChat/assets/68403991/48dc4634-fb8c-4d14-b483-fedd74e1b974

### Demo Video: https://www.youtube.com/watch?v=fn0ehgdFOks&t=2s

###### Developer: David Fong

### What is it

This is a small project, where I used GPT-3.5, to respond instagram comments on a specified post.

### Why I created it

I wanted something fun to do for the weekend, and thought it would be cool way for non-programmers to interact with my project.

Currently the script is scheduled on crontab. I plan on letting my instagram followers mess with it until my account gets banned = ).

---

### How I built it

I built it with the Open AI API to get responses with chat gpt, and used the instagrapi wrapper to receive and post messages to instagram.

https://openai.com/blog/openai-api

https://github.com/subzeroid/instagrapi


---

### Installation

1. git clone

2. Navigate to source directory

3. Create virtual env and activate it

5. pip install -r requirements.txt

5. Create .env file and fill in the following secrets (Media_URL is the web page url of the instagram post, you would like to monitor)

OPENAI_API_KEY=
OPENAI_OrganizationID=
Insta_Username=
Insta_Password=
Media_URL=

6. Go into the blacklist.csv file and replace dfong_chatbot with your instagram's username.

7. python main.py