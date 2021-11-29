# HW 04: Reddit Bot!

I made a bot that helps Pete Buttigieg (albeit in a very roundabout way) as [a project for Mike Izbicki's CSCI040 course.](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_04)

To be clear, I'm not a Pete Pal by any measure. Still, I am extremely fascinated by [all the buzz that has grown around him over the past few weeks](https://www.google.com/search?q=pete+buttigieg&sxsrf=AOaemvImqJNb0FWe0SLu170dF2GJ2dHYrA:1638073371713&source=lnms&tbm=nws&sa=X&ved=2ahUKEwin8r7rmrr0AhWVKn0KHYuPB-YQ_AUoAXoECAEQAw&biw=1280&bih=609&dpr=1.5), especially in contrast to [the negative coverage surrounding Joe Biden and his heir apparent Kamala Harris](https://www.google.com/search?q=kamala+harris&biw=1280&bih=609&tbm=nws&sxsrf=AOaemvKQ8Mv6NkwiAibwM_kTAiyI2LCyug%3A1638073373973&ei=HQSjYfD4OoXA0PEPvbaIqAE&oq=kamala+harris&gs_l=psy-ab.3..0i433i131i67k1j0i433i67k1j0i512i433k1j0i67k1j0i3k1j0i512k1l2j0i3k1j0i512k1j0i433i67k1.216965.218312.0.218657.13.4.0.8.8.0.194.194.0j1.1.0....0...1c.1.64.psy-ab..4.9.260....0.dG7saiuEG6o).

If the 2020 primaries were any indication, Buttigieg sure knows how to work the political press; how else could a small-town mayor surge towards the top of the pack? I can't help but flirt with a very casual conspiracy theory: _what if Buttigieg's communications team was actively promoting negative coverage of Biden and Harris to make him appear more desirable for 2024?_

I don't believe that this is the case, at least not to the point of flooding the Web with #MayorPete stan bots, but such a move would be Machiavellian enough for _House of Cards_...

**As such, my bot attacks Biden, Harris, and the rest of the top Democratic leadership from both left-wing and right-wing perspectives, while boosting Buttigieg and a few other Democrats as alternatives to the Biden/Harris ticket.**

Running `bot_counter.py --username=tranbot47` gives the following output:
```
len(comments)= 1000
len(top_level_comments)= 362
len(replies)= 638
len(valid_top_level_comments)= 362
len(not_self_replies)= 638
len(valid_replies)= 638
========================================
valid_comments= 1000
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```
My extra credit count is as follows:
- Getting at least 1000 valid comments posted (+ 6)
- Make your bot create at least 200 new submission posts instead of just new comments. _See_ `repost_bot.py` (+ 2)
- Instead of having your bot reply randomly to posts, make your bot reply to the most highly upvoted comment in a thread that it hasn't already replied to. _See_ `tlc_bot.py` (+ 2)
- Have your bot upvote any comment or submission that mentions your favorite candidate (or downvote submission mentioning a candidate you do not like), especially by using TextBlob. _See_ `upvote_bot.py` (+ 4)

Since I completed all the tasks for `bot.py`, I believe that I should receive a total of **34 points**.

[My favorite thread](https://old.reddit.com/r/BotTown2/comments/r2771d/kim_jong_un_is_possibly_in_a_vegetative_state/hm3136x/?context=3) is pretty short, but I just love how it's just one non-sequitur after the other.
![image](https://user-images.githubusercontent.com/4709565/143723420-60142b4a-6783-4aad-a712-f744915374cc.png)

I also played with [RedditMetis](https://redditmetis.com/user/tranbot47) to get another look at my bot's behavior. I was really amused by their evaluation of my "wholesomeness."
![image](https://user-images.githubusercontent.com/4709565/143729364-2ab4ddce-0f05-4bb6-92f4-6503cb6aaee9.png)
