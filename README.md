
Calculating the average degree of a vertex of a Twitter hashtag graph.

tweets_extract_fields.py extracts the necessary fields (hashtags, created_at), removes rate limiting messages and saves to a file ./tweet_input/tweets_extract.txt

average_degree.py iterates over the input and appends valid information as lists and tuples, for the twitter vertex graph.
- the entry must have at least two hashtags
- the created_at time must be within the 1 minute window from the maximum created_at entry

The nodes are the distinct hashtags within the window of time, the edges for hashtags mentioned within the same tweet are calculated using itertools permutations, to calculate the tuples of connected hashtags.

