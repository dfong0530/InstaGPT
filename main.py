from dotenv import load_dotenv
from instagram import *
from gpt import GetResponseFromChatGPT
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
insta_username = os.getenv("Insta_Username")
insta_password = os.getenv("Insta_Password")
media_url = os.getenv("Media_URL")

instagram = InstagramAccount(insta_username, insta_password)

instagram.changeMediaID(media_url)
comments = instagram.GetComments()

#Don't Repeat By Liking Commnets and only responding to one's that aren't liked and aren't you

for comment in comments:

    if comment.user.username != "dfong_chatbot" and not comment.has_liked:

        response = GetResponseFromChatGPT(api_key, comment.text)
        instagram.like_comment(comment.pk)
        instagram.RespondToComment(response, comment.pk)


