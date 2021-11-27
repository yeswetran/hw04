'''
EC 7: Have your bot upvote any comment or submission that mentions your favorite candidate
(or downvote submission mentioning a candidate you do not like).
I recommend creating a separate python file for performing the upvotes,
and you must be able to upvote comments contained within any submission in the class subreddit.
You may earn an additional two points if you use the TextBlob sentiment analysis library to
determine the sentiment of all the posts that mention your favorite candidate.
If the comment/submission has positive sentiment, then upvote it.
If the comment/submission has a negative sentiment, then downvote it.

Since TextBlob analysis is quite time-consuming, I added it to my code
AFTER voting on over 100 submissions and 500 comments.

Total EC from this file: 4 points!
'''

from typing import Text
import praw
import random
import datetime
from textblob import TextBlob

# connect to reddit 
reddit = praw.Reddit('upvotebot2')

submission_url = 'https://old.reddit.com/r/BotTown2/comments/r1jinb/pete_buttigieg_congratulated_for_masterclass/'
submission = reddit.submission(url=submission_url)

while True:
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)
    
    blob = TextBlob(submission.title)
    polarity = blob.sentiment.polarity
    if "biden" in (submission.title).lower() or "harris" in (submission.title).lower() or "kamala" in (submission.title).lower():
        if polarity > 0:
            submission.downvote() #downvotes positive discussions of biden/harris
            print("Polarity =", str(polarity) + ".", "Submission downvoted!")
        else:
            submission.upvote()
            print("Polarity =", str(polarity) + ".", "Submission upvoted!")
    if "pete" in (submission.title).lower() or "buttigieg" in (submission.title).lower():
        if polarity > 0:
            submission.upvote() #upvotes positive discussions of buttigieg
            print("Polarity =", str(polarity) + ".", "Submission upvoted!")
        else:
            submission.downvote()
            print("Polarity =", str(polarity) + ".", "Submission downvoted!")

    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    print('len(all_comments) =', len(all_comments))
    
    upvotes = 0
    downvotes = 0
    
    for comment in all_comments:
        comment.refresh()
        try:
            if str(comment.author) != 'tranbot47':
                blob = TextBlob(comment.body)
                polarity = blob.sentiment.polarity
                if "biden" in (comment.body).lower() or "harris" in (comment.body).lower() or "kamala" in (comment.body).lower():
                    if polarity > 0:
                        comment.downvote()
                        downvotes += 1
                        #print("-1") #just my way of confirming that the analysis and voting are working
                    else:
                        comment.upvote()
                        upvotes += 1
                        #print("+1")
                if "pete" in (comment.body).lower() or "buttigieg" in (comment.body).lower():
                    if polarity > 0:
                        comment.upvote()
                        upvotes += 1
                        #print("+1")
                    else:
                        comment.downvote()
                        downvotes += 1
                        #print("-1")
            for reply in comment.replies:
                blob = TextBlob(reply.body)
                polarity = blob.sentiment.polarity
                if "biden" in (reply.body).lower() or "harris" in (reply.body).lower() or "kamala" in (reply.body).lower():
                    if polarity > 0:
                        reply.downvote()
                        downvotes += 1
                        #print("--1")
                    else:
                        reply.upvote()
                        upvotes += 1
                        #print("++1")
                if "pete" in (reply.body).lower() or "buttigieg" in (reply.body).lower():
                    if polarity > 0:
                        reply.upvote()
                        upvotes += 1
                        #print("++1")
                    else:
                        reply.downvote()
                        downvotes += 1
                        #print("--1")
        except(AttributeError, praw.exceptions.ClientException):
            pass
    print(upvotes, "comments upvoted.")
    print(downvotes, "comments downvoted.")
    
    possible_new_subs = []
    for submission in reddit.subreddit("BotTown2").hot(): #picks a random "hot" submission from the subreddit
        possible_new_subs.append(submission)
    submission = random.choice(possible_new_subs)
    submission.comments.replace_more()
    print()
