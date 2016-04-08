from __future__ import division

import json
import sys

from datetime import datetime, timedelta
from dateutil.parser import parse
from itertools import permutations
from graphcalcs import *

class AverageDegree:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.graphcalcs = GraphCalcs()

    def averagedegree(self):
        
        delta = 59
        tweet = {}
        time_list = []
        httuple_list = []
        
        with open(self.input_file,'r') as fin, \
             open(self.output_file,'w') as fout:
                
            for line in fin:
                tweet[line] = json.loads(line)

                hashtag_tweet = tweet[line].get("hashtags")
                time = parse(tweet[line].get("created_at"))

                """append tuples and calculate running cutoff for time window"""
                httuple_list.append((time, hashtag_tweet))
                time_list.append(time)
                mintime = self.graphcalcs.cutoff(time_list, delta)
                
                """ignores hashtag lists with 0 or 1 hashtags"""
                """ignores entries if created_at time < cutoff time"""
                """appends the rest of the hashtags to a list"""
                hashtags_slider = []
                for (t,h) in httuple_list:
                    if len(h) < 2:
                        continue
                    elif t < mintime:
                        continue
                    hashtags_slider.append(h)

                """for graph nodes: each unique hashtag per tweet"""
                """for graph edges: permutate the hashtags per tweet into tuples"""
                """for each tweet within the time window, concatenate the above"""
                allnodes = []
                alledges = []
                for i, _ in enumerate(hashtags_slider):
                    allnodes.extend(hashtags_slider[i])
                
                    hashtag_tuples = permutations(hashtags_slider[i], 2)            
                    alledges.extend(tuple(hashtag_tuples))

                average_degree = self.graphcalcs.degreecalc(alledges,allnodes)
                
                fout.write("%.2f" % average_degree + "\n")


if __name__ == '__main__':
  runmodule = AverageDegree(sys.argv[1], sys.argv[2])
  start_time = datetime.now()
  avgdegree = runmodule.averagedegree()
  print 'total_time: ' + str(datetime.now() - start_time)
