weibo-export-py
===============

# Project abandoned

Hi, I've moved over to [easoncxz/weibo-export](https://github.com/easoncxz/weibo-export) for a rewrite of this project in Haskell. Please use that instead of this repo.

# About

A basic, shallow Weibo downloader.

The downloaded JSON format is almost entirely what `m.weibo.cn` endpoints
returns, only with boilerplate removed.  Refer to [open.weibo.com][api-docs]
for an idea of what each field means. This script uses the endpoint used by the
`m.weibo.cn` mobile web app instead of the API, because the API limits
responses to only 5 statuses.

This script is intended only for a basic, baseline download, to at least save
the text in your Weibo statuses. In particular, data like uploaded images,
comments, reposts etc. are no included in the downloaded data.

    $ python weibo_export.py --help

    Usage: weibo_export.py [OPTIONS] COOKIE

      Download Weibo statuses

      COOKIE should be the HTTP header value sent in the request, in URL-encoded
      form (RFC 3986).  This means it would contain information for all cookie
      key-value pairs.  Copying from the Chrome dev console's `cookie` field
      would work.

      Example COOKIE value:

          FOO=%5B%5D; BAR=1234

    Options:
      -s, --starting-page INTEGER  which page to start from, e.g. 5
      -d, --directory PATH         directory to save downloaded JSON files
      --help                       Show this message and exit.

Preparation for usage or development:

I'll assume you have `pip` installed, e.g. via

    $ brew install python
    ...
    $ which pip
    /usr/local/bin/pip

If you use virtualenv, activate one, e.g. in a directory `.venv`:

    $ virtualenv -p python3 .venv
    ...
    $ . .venv/bin/activate
    ...
    (.venv) $

Now install dependencies:

    (.venv) $ pip install -r requirements.txt

You're now ready to use the script:

    (.venv) $ python weibo_export.py --help


[api-docs]: http://open.weibo.com/wiki/%E5%B8%B8%E8%A7%81%E8%BF%94%E5%9B%9E%E5%AF%B9%E8%B1%A1%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84#.E7.94.A8.E6.88.B7.EF.BC.88user.EF.BC.89
