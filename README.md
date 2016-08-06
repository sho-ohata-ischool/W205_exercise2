# W205_exercise2

This application will require a couple of quick setup steps. The environment should already have storm setup with a python version that has tweepy and psycopg2 packages installed, along with Postgres installed. Using the AMI “UCB W205 Spring Ex 2 Image - ami-4cf9f826” will make things much easier. Once the EC2 instance is up and running postgres should be started.

First execute delete_tweet_table.py. This script will ensure that the table tweetwordcount is completely clean.
Second execute create_tweet_table.py. This script will create tweetwordcount with the correct schema.

Once the above two scripts are executed change your directory to tweetwordcount and execute sparse run. This will start the streaming application. Once enough information is collected do a keyboard interrupt to stop the application.

The finalresults.py and histogram.py are two scripts that will query the table for data. 
  - finalresults.py will fetch the count of a word, i.e. python finalresults.py hello
  - finalresults.py executed alone will print out the full table
  - histogram.py will fetch the count of a word between two numbers provided, i.e. python histogram.py 2 4

**Note that this app will not work if you close a storm session and restart a new one.**
