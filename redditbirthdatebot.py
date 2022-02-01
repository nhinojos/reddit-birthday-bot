import praw
import time
from datetime import datetime

#Reddit API Information
reddit = praw.Reddit(
    client_id="", #omitted for privacy
    client_secret="", #omitted for privacy
    user_agent="my user agent", 
    username="robot-7777",
    password='' #omitted for privacy
)
#Choosing subreddit r/technology
subreddit=reddit.subreddit('technology')

#Present-Date Numerical Values
presentdate=datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
thisMonth=int(presentdate[5:7])
thisDay=int(presentdate[8:10])
thisYear=int(presentdate[0:4])

#Iterates through popular posts, and its comments. 
for post in subreddit.hot(limit=10):
    for comment in post.comments:
        if hasattr(comment,"author"):
            if hasattr(comment.author,"created_utc"):

                #Birthdate Numerical Values
                birthdate=datetime.utcfromtimestamp(comment.author.created_utc).strftime('%Y-%m-%d %H:%M:%S')
                theirYear=int(birthdate[0:4])
                theirMonth=int(birthdate[5:7])
                theirDay=int(birthdate[8:10])

                #Determine if today is the users birthday.
                if thisDay==theirDay and thisMonth==theirMonth:
                    
                    #Wishes the specific user happy birthday. 
                    username=comment.author
                    response='Happy Cake-Day, u/'+str(username)+'!'
                    
                    #Congratulates user based on their age. 
                    Age=int(thisYear)-(theirYear)
                    if Age==0:
                        response+=' You were born within the last 24 hours. Welcome to reddit!'
                    elif Age==1:
                        response+=' You are 1 year old today!'
                    elif Age>1:
                        response+=' You are ' +str(Age)+' years old today!'

                    #Wishes Happy birthday, then sleeps
                    comment.reply(response)
                    time.sleep(600)

