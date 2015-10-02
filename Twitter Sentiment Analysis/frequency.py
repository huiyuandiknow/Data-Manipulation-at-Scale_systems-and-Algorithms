import sys
import json
from collections import Counter

def hw():

    word_list = list()
    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet.keys():
            tweet_content = tweet["text"].strip().split()
            for i in tweet_content:
                word_list.append(i)

    uniqueWords = sorted(set(word_list))
    for word in uniqueWords:
        print word, word_list.count(word)*1.0/len(word_list)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    global tweet_file
    tweet_file = open(sys.argv[1])
    hw()

if __name__ == '__main__':
    main()



