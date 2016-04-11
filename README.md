
Calculating the average degree of a vertex of a Twitter hashtag graph.

tweets_extract_fields.py extracts the necessary fields (hashtags, created_at), removes rate limiting messages and saves to a smaller sized file ./tweet_input/tweets_extract.txt

average_degree.py iterates over the input and appends valid information (as per the below), at the most recent iteration point, to a list of tuples for the twitter vertex graph:
- the entry must have at least two hashtags
- the created_at time must be within the 1 minute window from the maximum created_at entry

graphcalcs.py is imported into average_degree.py. graphcalcs.py contains a function to calculate the cutoff time, by which tweets from before this time are ignored; another function calculates the average degree from the list of nodes and edges. 

The nodes are the distinct hashtags within the 1 minute window of time, the edges for hashtags mentioned within the same tweet are calculated using itertools permutations, to calculate the tuples of connected hashtags.

The structure of this repo is as follows:

├── README.md 
├── run.sh
├── src
│   |── average_degree.py
│   |── graphcalcs.py
│   |── graphcalcs.pyc
│   └── tweets_extract_fields.py 
├── tweet_input

│   |── tweets.txt

│   └── tweets_extract.txt

├── tweet_output

│   └── output.txt

└── insight_testsuite

    ├── run_tests.sh
    
    └── tests
    
        └── test-2-tweets-all-distinct
        
            ├── tweet_input
            
            │   └── tweets.txt
            
            └── tweet_output
            
                └── output.txt


