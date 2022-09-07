#!/usr/bin/python3
# this bot was made by u/hananelroe on reddit
import thefuzz.fuzz as fuzz
import praw
import unicodedata

print("\u001b[31;1m" + str(praw.__version__))

Muck_list = ["depression", "!depressionhelp", "depressed", "empty", "numb", "!help"]
Blocked_users = []

# initialize with appropriate values
client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = "u/hananelroe's and u/norecap_bot's comment chains breaker bot modified by u/pkuba208 to help people suffering from depression and derealization"
comment_content = "100% Depression and derealization.

I had the same thing and got out of it, but I don't know if it will come back. Eminem's "Rock Bottom" still has me crying, because I can relate to it and describes my previous state. Seriously go listen to it. Anyways here are some tips:

Seek help. If you can't afford a therapist, call a helpline

Try to search for new interests, no matter how hard it may be. It's worth it

Educate your relatives about depression

Never lose hope. You'll get out of this shit. When I had depression I didn't seek help, because I didn't know, that I had it. I thought, that depression meant being sad all the time, when I couldn't feel anything and had the feeling of losing control of my life. I appeared functional from the outside, so nobody really knew. Eminem's songs saved me. This could be anything else for you. I was lucky enough to stumble across his songs and have relatives that love me. If you like, what I do, please say Good Bot and upvote this comment 
This is a fork of a bot made by u/hananelroe. Official Github: https://github.com/hananelroe/muck-chains-stopper-bot "
fixed_comment = ""

def noglyph(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

while True:
    # creating an authorized reddit instance
    reddit = praw.Reddit(client_id=fe6KECX2HrLJI48lovQVpw,
                         client_secret=gQeH7hRSjWIn-MEhfT2HJ3f70BdUtw,
                         username=NiceManBot,
                         password=PKC123!,
                         user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27)

    subreddit = reddit.subreddit("mentalhealth")
    print("\u001b[31;1monline\u001b[0m")

    try:
        for comment in subreddit.stream.comments(skip_existing=True):
            fixed_comment = noglyph("".join(dict.fromkeys(comment.body.lower())))
            print("\u001b[35;1m" + comment.body + "\u001b[34;1m\t" + com + " \u001b[0m" + str(fuzz.ratio(com, "muck") + "%"))
            print("u/\u001b[36;1m" + str(comment.author) + "\u001b[0m\n")

            if comment.parent().author.name == username and comment.body.lower() == "bad bot":
                comment.reply(why)
                break
            else:
                for item in Muck_list:
                    if fuzz.ratio(fixed_comment, item) > 80:
                        if str(comment.author) not in user:
                            comment.reply(comment_content)
                            break
    except KeyboardInterrupt:  # Ctrl-C - stop
        print("\u001b[31;1mBye!\u001b[0m")
        break
    except Exception as error:  # Any exception
        print(f"\u001b[31;1mError: {error}")
        print("Trying to restart...\u001b[0m")
