from json import load
from os.path import isfile
import sys
import tweepy

class Twitter:

    """
        Base class which contains methods common to all sub-classes such as connecting
        to the twitter api, fetching tweets and deleting tweets.
    """

    def __init__(self, filename=None):
        """
            Initialize a new DeleteBot Object\n
            KEYWORD ARGUMENTS:\n
            filename -- Name of the file which has stored the credentials
            in the json format
        """
        try:
            # Validation
            if not isinstance(filename, str):
                raise Exception("Error: Invalid Filename passed")

            if not isfile(filename):
                raise Exception(
                    "Error: File '{}' does not exist".format(filename))

            self.filename = filename
            self.api = None

            self.connect()

        except Exception as e:
            print(str(e))
            sys.exit(0)

    def connect(self):
        """
        Function to connect to the Twitter API using OAuth based on the credentials
        given in the 'credentials.json' file.
            # Credentials.json should contain values for the following keys:
            # -consumer_key
            # -consumer_key_secret
            # -access_token
            # -access_token_secret
        """
        credentials = None
        try:
            # Read the credentials.json file into a python dictionary
            with open(self.filename, "r") as f:
                credentials = load(f)

            auth = tweepy.OAuthHandler(
                credentials['consumer_key'], credentials['consumer_key_secret'])
            auth.set_access_token(
                credentials['access_token'], credentials['access_token_secret'])
            self.api = tweepy.API(auth)

        except Exception as e:
            print(str(e))
            sys.exit(0)

        print("Status: Connection Established Successfully!")