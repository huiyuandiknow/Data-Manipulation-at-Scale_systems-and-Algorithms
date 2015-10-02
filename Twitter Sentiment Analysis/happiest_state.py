import sys
import json
#from geopy.geocoders import Nominatim

def hw():
    scores={}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    state_list = {"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL",
                  "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
                  "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE",
                  "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
                  "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT",
                  "VA", "WA", "WV", "WI", "WY"}
    happy = {}
    k=0
    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet.keys() and "lang" in tweet.keys():
            if tweet["lang"] == "en":
                score = 0.
                count = 0.
                tweet_content = tweet["text"].strip().split()
                for i in tweet_content:
                    if i in scores.keys():
                        score += scores[i]
                        count +=1
                if score ==0:
                    avg_score = 0
                else:
                    avg_score = score/count

                location= tweet["user"]["location"].split(' ')
                for i in state_list: 
                    if i in location:
                        if i not in happy.keys():
                            happy[i] = avg_score
                        else:
                            if happy[i] < avg_score:
                                happy[i] = avg_score
                            
    print happy
                                        

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



