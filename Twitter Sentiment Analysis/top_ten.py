import sys
import json
from collections import Counter

def hw():

    word_list = list()
    for line in tweet_file:
        tweet = json.loads(line)        
        if "text" in tweet.keys():
            for i in tweet["entities"]["hashtags"]:
                word_list.append(i["text"])

    # get a dictionary with the unique words
    uniqueWords = sorted(set(word_list))    
    word_dict = dict()
    for word in uniqueWords:
        word_dict[word] = word_list.count(word)

    # print the 10 most frequent tags
    sorted_dict=  sorted(word_dict, key=word_dict.get, reverse=True)[:10]
    for i in range(len(sorted_dict)):
        print sorted_dict[i], word_dict[sorted_dict[i]]

def lines(fp):
    print str(len(fp.readlines()))

def main():
    global tweet_file
    tweet_file = open(sys.argv[1])
    hw()

if __name__ == '__main__':
    main()



