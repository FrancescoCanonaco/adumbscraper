# A DumbScraper

<img src="./images/Twitter-Gif.gif" width="150" height="150" />

## Introduction
A DumbScraper is a simple twitter scraper coded in python 3. Basically it is used to download and save tweets in a time period for a specified profile.


## Installation & Usage 

### Installation

the only requirement is selenium, for what concern both installation and configuration refer to the official documentation <a href="https://selenium-python.readthedocs.io/installation.html">Selenium official Doc</a>.

### Usage
Once you have installed Selenium you are ready to go:

<code>
<b>python3</b>  <i>dumb_scraper.py</i> <b>--username
</b> <i>matteosalvinimi</i> <b>--start_date</b> <i>2020-11-09T23:59:59</i> <b>--end_date</b> <i>2020-11-23T00:00:00</i>
</code>
<p>

>The "T" separator is used to separate day and time.

the command above generates a .csv file with all the tweets and some information such as: <b>comments</b>, <b>likes</b> and <b>retweets</b>.
</p>


Since this scraper is dumb, don't use it if you'd like to ingest a huge amount of data. :)