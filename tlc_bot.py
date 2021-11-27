'''
EC 6: Instead of having your bot reply randomly to posts,
make your bot reply to the most highly upvoted comment in a thread
that it hasn't already replied to. Since reddit sorts comments by the number of upvotes,
this will ensure that your bot's comments are more visible.
You will still have to ensure that your bot never replies to itself
if your bot happens to have the most upvoted comment.

Total EC from this file: 2 points!
'''
import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "[PROBLEM] is a [WEAKNESS] of our [NATION]. [AGENT] must stop [WASTING] and [ACT] to [END] it.",
    "[KAMALA] [THREATENS] our [VALUE] values. We need more [LEADERS] like [TRUMP], or else we'll be like [FOIL].",
    "[KAMALA] should not have [JOINED] [ADMINISTRATION]. What [WEAK] pick. I hope we find a better candidate in [ELECTION].",
    "[AFGHANISTAN] is the [WORST] [FAILURE] that we have seen from [ADMINISTRATION]. We need to [IMPEACH] [JOE] and [KAMALA] immediately.",
    "Assume that [JOE] doesn't run for [REELECTION]. [CANDIDATE] would be a [STRONGER] candidate in [ELECTION] than [KAMALA].",
    "[DEMS] strategy is clearly [FAILING]. I think that [WINNER], not [KAMALA], is [FUTURE] of [PARTY].",
    'How is [JOE] still in office? [AFGHANISTAN] showed just how weak he is. We need [LEADERS] like [TRUMP] in charge. [AGENT] could learn a thing or two.'
    ]

replacements = {
    'PROBLEM' : ['Gerrymandering', 'The filibuster', 'The deficit', 'Mass incarceration', 'The War on Drugs', 'Income inequality', 'Racism'],
    'WEAKNESS' : ['weakness', 'huge Achilles Heel', 'weakness', 'flaw', 'shortcoming', 'contradiction'],
    'NATION' : ['nation', 'great nation', 'republic', 'democracy', 'country', 'society', 'homeland'],
    'AGENT' : ['Congress', 'President Biden', 'The Democrats', 'Kamala Harris', 'Vice President Harris', 'Joe', 'Kamala'],
    'WASTING' : ['wasting time', 'holding back', 'sitting on the sidelines', 'doing nothing', "whatever they're doing", 'the Republican madness', 'letting the Republicans ruin everything', 'letting the GOP run amok', 'kissing up to the GQP'],
    'ACT' : ['act', 'fight', 'stand up', 'push'],
    'END'  : ['end', 'eliminate', 'reduce', 'destroy', 'defeat', 'knock down', 'finally defeat', 'put an end to', 'finally put an end to'],
    'THREATENS': ['threatens', 'endangers', 'betrays', 'defies', 'contradicts', 'rejects', 'challenges', 'undermines', 'opposes'],
    'VALUE' : ['Christian', 'capitalist', 'American', 'founding', 'fundamental', 'deepest', 'human', 'civilized', 'family', 'basic human', 'most basic'],
    'LEADERS': ['leaders', 'strong men', 'saviors', 'good Christians', 'real Americans', 'patriots', 'fighters', 'champions', 'conservatives', 'Republicans'],
    'TRUMP': ['Trump', 'Josh Mandel', 'Glenn Youngkin', 'Josh Hawley', 'Tom Cotton', 'Ron DeSantis', 'Greg Abbott', 'Larry Elder', 'Steve Bannon'],
    'FOIL' : ['Venezuela', 'China', 'Communist China', 'Cuba', 'Mexico', 'North Korea', 'Iran', 'Communist Russia', 'Nazi Germany', 'the Soviet Union'],
    'KAMALA': ['Kamala', 'Kamala Harris', 'the Vice President', 'our VP', 'the VP', 'VP Harris', 'Madame Vice President', 'Copmala Harris', 'Harris'],
    'JOINED' : ['been allowed into', 'entered', 'joined', 'been allowed anywhere near'],
    'ADMINISTRATION' : ["the Biden administration", "Biden's Cabinet", "the White House", "Biden's White House", "this administration"],
    'WEAK' : ['a weak', 'an incompetent', 'an uncharismatic', 'a divisive', 'a disappointing', 'an underwhelming', 'a meh', 'an uninspired'],
    'ELECTION' : ['2024', 'the 2024 primaries', 'the next few years', 'the next election', 'time', 'time for 2024'],
    'AFGHANISTAN' : ['Afghanistan', 'The fall of Kabul', 'The Taliban victory', 'Our retreat from Afghanistan', 'Our defeat in Afghanistan'],
    'WORST' : ['worst', 'greatest', 'most colossal', 'biggest', 'largest', 'most serious', 'deadliest', 'least acceptable', 'most disgusting', 'most reprehensible', 'hugest'],
    'FAILURE' : ['failure', 'screw-up', 'mistake', 'misstep', 'blunder', 'disaster', 'example of poor leadership'],
    'IMPEACH' : ['impeach', 'replace', 'campaign against', 'primary', 'punish', 'stop', 'fix', 'correct', 'ditch', 'reconsider', 'straighten out'],
    'JOE' : ['Biden', 'Joe Biden', 'the President', 'President Biden', 'Joe'],
    'REELECTION' : ['reelection', 'a second term', 'president in 2024'],
    'CANDIDATE' : ['Elizabeth Warren', 'Stacey Abrams', 'Mayor Pete', 'Pete Buttigieg', 'Secretary Pete', 'Pete', 'Buttigieg', 'Gavin Newsom', 'AOC', 'Sherrod Brown', 'Andy Beshear', 'Michelle Obama', 'A cardboard cutout of Obama'],
    'DEMS' : ["The Dems'", "Biden's", "Jaime Harrison's", "Joe Biden's", "The Democratic Party's", "The left's"],
    'FAILING' : ['failing', 'going nowhere', 'stupid', 'flawed', 'misguided', 'out of touch', 'idiotic', 'broken', 'is in disarray', 'screwing up'],
    'WINNER' : ['Michelle Wu', 'Eric Adams', 'Gavin Newsom', 'Pete Buttigieg', 'Stacey Abrams', 'Jon Ossoff', 'Mayor Pete', 'Secretary Pete'],
    'FUTURE' : ['the future', 'going to be responsible for the revival', 'the savior', 'the obvious leader', 'the best person to take charge', 'the right person to take charge', 'the correct symbol', 'the most promising leader'],
    'PARTY' : ['the Democrats', 'the left', 'the Party', 'the Democratic Party', 'the Dems', 'our party', 'our nation', 'progress'],
    'STRONGER' : ['stronger', 'bolder', 'fresher', 'better', 'superior', 'more logical', 'more progressive', 'more sensible']
    }

def generate_comment():
    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace(('['+k+']'), random.choice(replacements[k]))
    return s

# FIXME:
# connect to reddit 
reddit = praw.Reddit('csci040')

# FIXME:
# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r1a9bj/san_francisco_mayor_closing_shopping_district_to/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:
    
    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions

    submission.comments.replace_more(limit=None)
    all_comments = []
    not_my_comments = []

    for comment in submission.comments.list():
        if str(comment.author) != 'None':
            all_comments.append(comment)
        if str(comment.author) != 'tranbot47':
            not_my_comments.append(comment)

    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not generated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    
    try:
        if len(not_my_comments) == len(all_comments):
            top_comment = not_my_comments[0]
            for tlc in submission.comments:
                if str(tlc.author) != 'tranbot47' and int(tlc.score) > top_comment.score:
                    top_comment = tlc
            text = generate_comment()
            top_comment.reply(text)

        else:
            comments_without_replies = []
            not_yet_commented = False
            for comment in not_my_comments:
                try:
                    comment.refresh()
                    for reply in comment.replies:
                        if str(reply.author) == 'tranbot47':
                            not_yet_commented = False
                            break
                        else:
                            not_yet_commented = True
                except(AttributeError, praw.exceptions.ClientException):
                    pass
                if not_yet_commented:
                    comments_without_replies.append(comment)
            print('len(comments_without_replies)=',len(comments_without_replies))

            if len(comments_without_replies) > 0:
                comment = random.choice(comments_without_replies)
                comment.reply(generate_comment())

        possible_new_subs = []
        for submission in reddit.subreddit("BotTown2").hot(limit=5):
            possible_new_subs.append(submission)
        submission = random.choice(possible_new_subs)
        while str(submission.author) == "imtherealcs40bot":
            submission = random.choice(possible_new_subs)
        submission.comments.replace_more()
    except praw.exceptions.RedditAPIException:
        time.sleep(100) #waits 100 sec before trying again
