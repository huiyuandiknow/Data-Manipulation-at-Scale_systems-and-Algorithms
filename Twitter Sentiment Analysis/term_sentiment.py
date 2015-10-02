import sys
import json

def hw():
    scores= {}
    for line in sent_file:
	term, score = line.split("\t")
	scores[term] = int(score)

    for line in tweet_file:
	tweet = json.loads(line)
	if "text" in tweet.keys():
	    score_list = list()
	    tweet_content = tweet["text"].strip().split()

	    # store sentiment score, or 0 if non-sentiment
	    for i in range(len(tweet_content)):
		if tweet_content[i] in scores.keys():
		    score_list.append(scores[tweet_content[i]])
		else:
		    score_list.append(0)

	    # update all 0 scores
            for i in range(len(score_list)):
		if score_list[i]==0:
		    # at front of list
                    if i == 0:
			score_list[i] = add_weighted_scores(1, len(tweet_content), score_list, 1)
	            # at end of list
		    elif i == len(tweet_content)-1:
			score_list[i] = add_weighted_scores(len(tweet_content)-2, -1, score_list, -1)
	            else:
			score_list[i] = add_weighted_scores(i+1, len(tweet_content),score_list,1)+add_weighted_scores(i-1, -1, score_list,-1) 	

	    # print result
	    for i in range(len(tweet_content)):
		print tweet_content[i], ' ', score_list[i]

def add_weighted_scores(begin, end, score_list, order):
    score = 0
    for i in range(begin, end, order):
	score += score_list[i]/(abs(i-begin)+1)
    return score 			    
			
def lines(fp):
    print str(len(fp.readlines()))

def main():
    global sent_file, tweet_file
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()

if __name__ == '__main__':
    main()
