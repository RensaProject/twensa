# Twensa

## Overview
Twensa provides some simple functions for analyzing tweets using the Rensa framework.  

If you use this repository, please cite:

```
@phdthesis{harmon2017narrative,
  title={Narrative Encoding for Computational Reasoning and Adaptation},
  author={Harmon, Sarah M},
  year={2017},
  school={University of California, Santa Cruz}
}
```

## Requirements
Twensa is currently compatible with Python 2.7.  You will need tweepy, nodebox_linguistics_extended, and rensabrain as dependencies.

You can install tweepy with pip:
```
pip install tweepy
```

You can install nodebox_linguistics_extended and rensabrain using their respective setup files:

```
python setup.py install
```

Download this repository as well into the same directory.

## Setup
Head over to the [Twitter Application Management website](http://apps.twitter.com/) to generate your consumer key, consumer secret, access token, and access secret.  Add these details to config.py.

## Usage
### Customize your configuration
Inside config.py, find the string variable named *query*.  This is the string representing the search terms that Twensa will use to search Twitter.  You can edit this to be any search query you like. The default string is "computational creativity".  

You can also edit the number of tweets extracted (*num_tweets*).  The default number is 10.

### Run your analysis
In the command line, type:
```
python twensa.py
```
This will run the query and generate a file containing Rensa assertions in the *assertions* folder.  Each assertion represents a tweet and its associated data.

In the command line, you will see a prompt that says
```
This will delete all generated assertion files except for the most recent one.  Do you wish to continue (Y\N)?
```

Type "y" if you want to delete previous assertion files and only save the latest file.  If you would like to save previous assertion files, type "n" instead.

### Check out the results
An example of how to load the generated assertion files into brains, print out the results, and edit the results is inside sample_analysis.py.  Run this demo with:
```
python sample_analysis.py
```

Generally, all results are stored in the *assertions* folder.  Each assertion contains data as follows:

Name | Description
--- | ---
`text` | The text of the tweet.
`user_name` | The username for the person who wrote the tweet.
`screen_name` | The screen name of the person who wrote the tweet.
`user_id` | The Twitter ID for the user who wrote the tweet.
`favorite_count` | How many favorites this tweet received.
`retweet_count` | How many retweets this tweet received.
`created_at` | When this tweet was written.
`hashtags` | The hashtags used in the text of the tweet.
`keywords` | Major category words that are used in the text of the tweet.
`rid_primary` | A score representing primary process thoughts (free-form associative thinking involved in dreams and fantasy) according to the Regressive Imagery Dictionary.  
`rid_secondary` | A score representing secondary process thoughts (logical, reality-based and focused on problem solving) according to the Regressive Imagery Dictionary.  
`rid_emotions` | A score representing emotional process thoughts (expressions of fear, sadness, hate, affection, etc.) according to the Regressive Imagery Dictionary.  
