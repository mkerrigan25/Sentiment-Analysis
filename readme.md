# Sentiment analysis tool for online reviews

My final year project for college.

## How to use

There are four scripts used in this project.
 
ukrevpy and usrev.py convert all the US or UK reviews into a CSV file. The usrev.py script should be run before sentimet_analysis.py

The nltk installer should be used if nessary.
If it's the machines first time using nltk, un-comment nltk.download() on line 5 of sentiment_analysis.py and wait until download is complete before you run the script. 

If running python 2.7 use the Annaconda ide as it allows nltk to use numphy.
After running the sentiment_analysis.py script, look inside the us.csv or uk.csv files to view the results.
