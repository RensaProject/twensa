from rensabrain.Brain import *
import glob
import sys

''' Prints out the major data for a brain containing tweet assertions. '''
def print_tweets(my_brain):
    print "\n - - - RESULTS - - - \n"
    for a in my_brain.get_assertions():
        print a.user_name + " (@"+a.screen_name+"): " + a.text
        print " - created at: " + a.created_at
        print " - favorites: " + str(a.favorite_count)
        print " - retweets: " + str(a.retweet_count)
        sys.stdout.write(" - keywords: ")
        for kw in a.keywords:
            print kw[1] ,
        if a.hashtags:
            sys.stdout.write("\n - hashtags: ")
            for ht in a.hashtags:
                print ht ,
        print "\n - rid_primary: " + str(a.rid_primary)
        print " - rid_secondary: " + str(a.rid_secondary)
        print " - rid_emotions: " + str(a.rid_emotions)
        print "\n"
'''
Finds the most recent filename in the assertions directory.
'''
def get_newest_assertion_file():
  dates = get_assertion_filenames()
  return "assertions/assertions-" + max(dates) + ".json"

'''
Returns a list of the names of all files in the assertions directory.
'''
def get_all_assertion_files():
  files = []
  dates = get_assertion_filenames()
  for date in dates:
      files.append("assertions/assertions-" + date + ".json")
  return files

'''
Returns a list of dates that correspond to filenames
in the assertions directory.  This is a helper function for
get_newest_assertion_file and get_all_assertion_files.
'''
def get_assertion_filenames():
  dates = []
  for fn in glob.glob("assertions/*.json"):
    if fn.find("assertions-") != -1:
      date = fn[fn.find("assertions-")+11:-5]
      dates.append(date)
  return dates
