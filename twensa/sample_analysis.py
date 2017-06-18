''' This file demonstrates how to review saved Twitter analyses.'''

from twensalyze import *

def main():
    ''' Load the latest assertions file.'''
    my_brain = load_brain([get_newest_assertion_file()])

    ''' You can also load a brain with the contents of all generated assertion files.  Use this instead:'''
    # my_brain = load_brain(get_all_assertion_files())

    ''' Print the major data for this brain's tweets. '''
    print_tweets(my_brain)

    ''' If you want to access each assertion in the brain, use get_assertions().  Here's an example: '''
    print " - - - CUSTOM RESULTS - - -"
    for a in my_brain.get_assertions():
        if a.rid_emotions > 0:
            print "This tweet has a nonzero RID emotional score of " + str(a.rid_emotions) + ": "
            print " - " + a.text + "\n"

    ''' You can also edit assertions.  For example, you can add your own tags: '''
    my_brain.edit_assertion(8,"tag",["ICCC"])

    ''' To find assertions with certain attributes, you can search by tag or by other search values.'''
    iccc_asserts = my_brain.get_assertions_with_tag(["ICCC"])
    print "\nThe following assertions are tagged with 'ICCC':"
    for ia in iccc_asserts:
        print " - " + ia["text"] + "\n"

    iccc_asserts2 = my_brain.get_assertions_with({"rid_primary":"0.0","hashtags":["iccc17"]})
    print "\nHere's another custom group of assertions:"
    for ia2 in iccc_asserts2:
        print " - " + ia2["text"] + "\n"

    ''' For more ideas about how to use Rensa, check out https://github.com/RensaProject/rensapy. '''

if __name__ == '__main__':
    main()
