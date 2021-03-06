from __future__ import division
from datetime import datetime, timedelta

class GraphCalcs:

    def __init__(self):
        self.time_list = []
        self.edges_list = []
        self.nodes_list = []
        
    def cutoff(self, time_list, delta):
        """return the minimum acceptable time for the current time window"""
        """time_list: cumulative list of created_at time"""
        """(maximum time in the list) - delta (time window of 59 seconds)"""
        return max(time_list) - timedelta(seconds=delta)

    def degreecalc(self, edges_list, nodes_list):
        """returns the average degree of a vertex in a Twitter hashtag graph"""
        noedges = len(set(edges_list))
        nonodes = len(set(nodes_list))
        try: 
            return (noedges / nonodes)
        except ZeroDivisionError:
            return (noedges / 1)
