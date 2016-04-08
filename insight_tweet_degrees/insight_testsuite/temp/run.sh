#!/usr/bin/env bash

python ./src/tweets_extract_fields.py ./tweet_input/tweets.txt ./tweet_input/tweets_extract.txt

python ./src/average_degree.py ./tweet_input/tweets_extract.txt ./tweet_output/output.txt




