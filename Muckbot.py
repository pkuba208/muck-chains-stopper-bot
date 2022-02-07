# this bot was made by u/hananelroe on reddit
# import needed libraries
import thefuzz.fuzz as fuzz
import praw
import unicodedata
import time
import random
import sys
import DA_SECRETS

# print the version
print("\u001b[31;1m praw: v" + str(praw.__version__))

# every m*** to get checked with the comments
Muck_list = ["muck", "muck.", "muck!", "muck?", "mֳ¼ck", "mֳ¼ck.", "mֳ¼ck!", "mukc", "mֳ¼ck?", "m\*ck",
             "kcum", "׀¼uck", "much", "mcuk"]

# list of blocked users to skip checking them
Blocked_users = []  # to use you need to write the user name without the "u/"
Enable_Blocking = False  # make it True to enable blocking users

# bot information:
client_id = DA_SECRETS.client_id
client_secret = DA_SECRETS.client_secret
username = DA_SECRETS.username
password = DA_SECRETS.password
user_agent = "u/hananelroe's and u/HoseanRC's comment chains breaker bot"

# detials about the bot to send after every comment
credit = "\n______\n ^(I'm just a simple bot that wants to stop muck chains, [here is my github page](https://github.com/hananelroe/muck-chains-stopper-bot)\
, you can see my source code and submit my issues there)\n\n ^(I'm a collaboration between [Hananelroe](https://www.reddit.com/u/Hananelroe) and [HoseanRC]\
(https://www.reddit.com/u/HoseanRC))\n\n^([visit my website](https://www.reddit.com/r/Damnthatsinteresting/comments/ovp6t1/never_gonna_give_you_up_by_rick_astley_remastered))"

# comment to send for every comment it receives
shut = "#**SHUT**"  # shut comment for m***
bad_bot = "WHY?"  # WHY? comment for "bad bot"
good_bot = "thanks! :)"  # thanks comment for "good bot"

fixed_comment = ""  # fixing comments to get better muck results

mucks = 0  # number of mucks

reduceComments = False

class Empty():  # Empty class for parent function
    def __init__(self):
        self.body = None  # a fake "body" attribute
    pass     # ignore being empty


def parent(child_comment):  # gets comment's parent (aka the comment it replied to)
    # and returns a fake empty comment if it didn't find one

    parent_comment = Empty()  # create empty object for the fake comment
    parent_comment.author = Empty()  # add empty object for name for the author of the fake comment
    parent_comment.author.name = ""  # add the fake comment's author name
    try:
        if str(type(
                child_comment.parent())) == "<class 'praw.models.reddit.comment.Comment'>":  # check if it's a comment
            parent_comment = child_comment.parent()  # if it did find the comment, it will
            # save it, otherwise it will raise error
    finally:
        return parent_comment  # at the end returns the same output as comment.parent()
        # but it will return empty comment instead of any error


def noglyph(s):  # removes any glyph from a character (ex. ý -> y, Ŕ -> R)
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def printComment(comment, fixed_comment, authorName):
    print("\u001b[35;1m" + comment  # prints the original comment, the fixed one,
          + "\u001b[34;1m\t" + fixed_comment  # and the fixed comment similarity to "muck"
          + " \u001b[0m" + str(fuzz.ratio(fixed_comment, "muck")) + "%"
          + f"\nu/\033[36;1m{authorName}\033[0m")


def reply(comment, content, credit):  # replies with/without credit according to the chain's length
    try:
        # check if the comment have more than 4 parents:
        comment.parent().parent().parent().parent()
    except:
        # if the comment does have more than 4 parents:
        comment.reply(content + credit)
    else:
        comment.reply(content)  # else than comment bad_bot without credit


if __name__ == '__main__':
    while True:
        # creating an authorized reddit instance from the given data
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             username=username,
                             password=password,
                             user_agent=user_agent)

        # selects the subreddit to read the comments from
        subreddit = reddit.subreddit(DA_SECRETS.subreddit_name)
        print("\033[92m online\u001b[0m")  # prints green "online"

        try:
            # for every new comment:
            for comment in subreddit.stream.comments(skip_existing=True):

                # removing glyghps, spaces and new lines:
                fixed_comment = noglyph("".join(dict.fromkeys(comment.body.lower()))).replace(" ", "").replace("\n", "")

                # print comment details:
                printComment(comment.body, fixed_comment, comment.author.name)

                # skip the comment check if the commenter is the bot or the user is blocked:
                if comment.author.name == username or comment.author.name in Blocked_users:
                    continue

                # if the comment replied to the bot:
                if parent(comment).author.name == username:
                    if comment.body.lower() == "bad bot:":
                        print("\033[92m bad bot MATCH! replying...\033[0m\n")
                        reply(comment, bad_bot, credit)
                    elif comment.body.lower() == "good bot":
                        print("\033[92m good bot MATCH! replying...\033[0m\n")
                        reply(comment, good_bot, credit)
                else:
                    for item in Muck_list:
                        # if the comment is >74% "muck" and starts/ends with "m"/"k":
                        if fuzz.ratio(fixed_comment, item) > 74 and fixed_comment[0] in "mk":
                            if reduceComments:
                                if random.randrange(1, 5) == 1:  # roughly 1 out of 5 comments:
                                    print("\033[92m MUCK detected! replying...\u001b[0m\n")
                                    reply(comment, shut, credit)
                            else:
                                print("\033[92m MUCK detected! replying...\u001b[0m\n")
                                reply(comment, shut, credit)
                            break
                    continue
        except KeyboardInterrupt:  # Ctrl-C - stop
            print("\u001b[31;1mBye!\u001b[0m")
            break
        except Exception as error:  # Any exception
            print(
                f"\u001b[31;1mError in line {sys.exc_info()[-1].tb_lineno}: {error}")  # prints error line and the error itself
            print("Trying to restart...\u001b[0m")