AUTHOR = 'George V. Reilly'
SITENAME = 'Today I Learned'
# SITEURL = 'https://www.georgevreilly.com/til'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = '/Users/georgevreilly/src/Casper2Pelican'

AUTHOR_PIC_URL="https://www.georgevreilly.com/content/binary/bloomsday2017hat.jpg"
AUTHOR_BIO="Irish-born software developer living in Seattle"
AUTHOR_LOCATION="Seattle, WA, USA"
SITE_DESCRIPTION="A mini-blog"
# SITE_LOGO = If used will show logo in top left corner / ograph tags.
DEFAULT_HEADER_IMAGE="images/aerlingus-bg.jpg"
ARCHIVE_HEADER_IMAGE="images/barge.jpg"
TWITTER_USERNAME="georgevreilly"

EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},
#   'extras/CNAME': {'path': 'CNAME'},
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
