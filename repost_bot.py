'''
EC4: Make your bot create new submission posts instead of just new comments.
You can easily automate this process by scanning the top posts in your favorite sub (e.g. /r/liberal or /r/conservative)
and posting them to the class sub. I recommend creating a separate python file for creating submissions and creating comments.

For full credit, you must have at least 200 submissions, some of which should be self posts and some link posts.
Duplicate submissions (i.e. submissions with the same title/selftext/url) do not count.

EC from this file: 2 points!!!
'''
import praw
import random
import time

reddit = praw.Reddit('csci040')
reddit.validate_on_submit = True

possible_reposts = []
old_reposts = []
subreddit = "democrats"

for i in range(15): #does this 400 times
    try:
        if i > 8:
            subreddit = "liberal" #just in case there aren't enough posts from r/democrats
        for submission in reddit.subreddit(subreddit).top("month"):
            if submission not in old_reposts:
                possible_reposts.append(submission)
        for j in range(25):
            repost = random.choice(possible_reposts)
            reddit.subreddit("BotTown_lives_on").submit(repost.title, url=repost.url) 
            possible_reposts.remove(repost)
            print("Just posted!")
            time.sleep(30) #waits 60 seconds to "take a breath"
    except praw.exceptions.RedditAPIException:
        time.sleep(1000) #waits 1000 sec before trying again
