import praw
import math

r = praw.Reddit(user_agent="faker")
sub = r.get_subreddit("leagueoflegends")

print "sub " + str(sub.subscribers) # subs
print "online " + str(sub.accounts_active) # real amount

hots = sub.get_hot(limit=15)
votes_list = []
for i in range(15):
	elem = hots.next()
	votes_list += [elem.score]
print "max_vote " + str(max(votes_list))
print "min_vote " + str(min(votes_list))
print "avg_vote " + str(sum(votes_list) / float(len(votes_list)))
print "description " + sub.description


