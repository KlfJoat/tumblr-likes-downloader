import os
import code
import oauth2 as oauth
from pprint import pprint
import json
import urllib
import pytumblr

# Number of likes to fetch in one request
limit = 20

# Directory where to save the images
directory = "tumblr-likes"

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'CONSUMER_KEY',
  'CONSUMER_SECRET',
  'OAUTH_TOKEN',
  'OAUTH_TOKEN_SECRET'
)

# Get the info on the user
info = client.info()

# Get the content
name = info["user"]["name"]
number = int(info["user"]["likes"])
pages = number // limit

# Print the number of likes
print "Tumblr user {0} has {1} likes".format(name, number)
print "{0} pages will be fecthed".format(pages)

posts = 0
total = 0
for page in xrange(0, pages):

  # Get the likes
  offset = page * limit
  likes = client.likes({'offset': offset, 'limit': limit})["liked_posts"]

  # Print the content
  #pprint(likes)
  #f = open('likes.json', 'w')
  #json.dump(likes, f)

  # Parse the likes
  for liked in likes:
    photos = liked["photos"]
    count = 0
    for photo in photos:
      url = photo["original_size"]["url"]
      imgname = url.split('/')[-1]
      filename = directory + "/" + str(liked["timestamp"]) + "-" + liked["blog_name"] + "-"
      if count > 0:
        filename += str(count) + "-"
      filename += imgname
      print filename
      if (os.path.isfile(filename)):
        print "File already exists"
      else:
        urllib.urlretrieve(url, filename)
      count += 1
    posts += 1
    total += count

print "Total posts liked : " + str(posts)
print "Total images downloaded : " + str(total)

