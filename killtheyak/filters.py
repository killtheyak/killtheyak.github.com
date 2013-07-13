# -*- coding: utf-8 -*-
from urlparse import urlparse
from flask import Markup
from bs4 import BeautifulSoup
from .main import app


@app.template_filter('fenced_code')
def fenced_code(html):
    '''Returns the html for all code on a page.'''
    soup = BeautifulSoup(html)
    # List of Tags containing code
    blocks = soup.find_all('div', class_='codehilite')
    # Now, as strings
    block_strs = [str(block) for block in blocks]
    joined = '\n'.join(block_strs)
    return Markup(joined)

@app.template_filter('github_urlize')
def github_urlize(strg):
    """Filters a github user url (string) and returns an <a> element with
    the href as url and the text as the username.

    If an url is not passed in, just returns the original string.
    """
    url = urlparse(strg)
    if url.netloc:
        username = url.path.lstrip('/')
        markup = '<a href="{}">{}</a>'.format(strg, username)
        return Markup(markup)
    else:
        return strg