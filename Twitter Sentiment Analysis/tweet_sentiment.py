import sys
import json

def hw():
    scores={}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
 
   
    for line in tweet_file:
	tweet = json.loads(line)
	if "text" in tweet.keys():
	    score = 0
	    tweet_content = tweet["text"].strip().split()
	    for i in tweet_content:
		if i in scores.keys():
		    score += scores[i]
	    print score
	else:
	    print 0

def lines(fp):
    print str(len(fp.readlines()))

def main():
    global sent_file, tweet_file
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()



