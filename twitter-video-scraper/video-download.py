#!/home/anomalia/anaconda3/bin/python3

# Scraping of Twitter account to download daily video

import twint
import re
import sh

# User search variables
username = "angelmartin_nc"
search = "informativo matinal"
download_dir = '/tmp/angel_martin/'
archive = download_dir + 'download_archive.txt'


# Configure
tweets = []
c = twint.Config()
c.Username = username
c.Search = search
c.Hide_output = True
c.Store_object = True
c.Store_object_tweets_list = tweets

# Run
twint.run.Search(c)

# Extract link from every tweet
capture_pattern = r'(https\:\/\/.*)'
links = []

# Pass if tweet has no link
for tweet in tweets:
    try:
        link = re.search(capture_pattern, tweet.tweet)
        links.append(link.group())
    except:
        pass

# Delete duplicated links
video_links = list(dict.fromkeys(links))

# Download videos using youtube-dl flags
open(archive, "a").close()

for link in video_links:
    print("Downloading link: " + link)
    sh.youtube_dl("-o", download_dir + "Informativo_matinal_%(upload_date)s.%(ext)s", "--download-archive", archive, link)