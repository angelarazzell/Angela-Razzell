"""loads the json tweet messages, removes rate limiting messages"""
"""extracts the 2 necessary fields: "created_at", "hashtags" """
"""finally, loads the tweets extracted fields into a much smaller text file"""

import json
import sys
from datetime import datetime

class ExtractFields:
    def __init__(self, input_file, output_file):

        self.input_file = input_file
        self.output_file = output_file

    def jsonparse(self):

        with open(self.input_file,'r') as fin, \
             open(self.output_file,'w') as fout:
                
            for line in fin:
                tweet = json.loads(line)

                """if "limit" in tweet:"""
                """changed to "entities" to prevent other errors from bad line input"""
                if "entities" not in tweet:
                    continue
                
                ents = tweet.get("entities") 
                hashtags = ents.get("hashtags")

                """append only hashtags (text) from the hashtags field, ignore the indices"""
                hashlist = []
                for i, _ in enumerate(hashtags):
                    hashlist.append(hashtags[i]["text"])

                hashtag_data = {"created_at" : tweet.get("created_at"), "hashtags" : hashlist}

                """write only hashtags and created_at fields to tweets_extract in input file"""
                fout.write(json.dumps(hashtag_data)+'\n')
                

if __name__ == '__main__':
  runmodule = ExtractFields(sys.argv[1], sys.argv[2])
  start_time = datetime.now()
  tweetparse = runmodule.jsonparse()
  print 'total_time: ' + str(datetime.now() - start_time)
