# tumblr-likes-downloader

Repository created from https://gist.github.com/jeffaudi/89bba20e839d99e4afab

I had to make some changes to get this to work on my Ubuntu 16.10 system, so these are they.

## Install Steps
### 1. Create directory
I do not know enough Python to do this in the program.  So I manually create $directory wherever I need it.  

It throws an IOError exception if the directory does not exist.
### 2. Install packages
I had to manually install the following 3 packages.
1. `/usr/bin/python pip install pytumblr`
2. `/usr/bin/python pip install oauth2`
3. `/usr/bin/python pip install pprint`
### 3. Create API and OAuth keys
Go to https://www.tumblr.com/docs/en/api/v2 and follow the directions there.  

Click the 'Explore API' link to log in using your newly created application, get an OAuth token, and then view the 4 secrets you will need to replace in this script.  (CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
