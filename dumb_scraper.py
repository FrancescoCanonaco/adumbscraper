from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import argparse

def get_content(driver):
    #getting text from the page
    text = driver.find_elements_by_xpath('.//div[@class = "css-901oao r-jwli3a r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"]')
    #getting like retweets and number of comments
    info = driver.find_elements_by_xpath('.//div[@class = "css-1dbjc4n r-18u37iz r-1wtj0ep r-156q2ks r-1mdbhws"]')
    #getting post's date of pubblication
    time = driver.find_elements_by_tag_name("time")
    return text, info, time

def timetagvalue_to_datetime(time_value):
    time_string_clean = time_value.split("T")
    time_string_clean[1] = time_string_clean[1].split(".")[0]
    time_string_clean = " ".join(time_string_clean)
    return string_to_datetime(time_string_clean) 

def string_to_datetime(time_string):
    return datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')


def show_animation(i):
    animation = [
        "[        ]",
        "[=       ]",
        "[===     ]",
        "[====    ]",
        "[=====   ]",
        "[======  ]",
        "[======= ]",
        "[========]",
        "[ =======]",
        "[  ======]",
        "[   =====]",
        "[    ====]",
        "[     ===]",
        "[      ==]",
        "[       =]",
        "[        ]",
        "[        ]"]
    print("Scraping: "+animation[i % len(animation)], end='\r')


def get_tweets(user = "matteosalvinimi", start_date_scraping = "2020-11-09 23:59:59", end_date_scraping = "2020-11-23 00:00:00", time_sleep=10):
    driver = webdriver.Firefox()
    driver.get("https://twitter.com/"+user)
    time.sleep(time_sleep)
    elem = driver.find_element_by_tag_name("body")
    start_date = string_to_datetime(start_date_scraping)
    end_date = string_to_datetime(end_date_scraping)
    scraped_tweets = []
    scrolling = True
    last_date = string_to_datetime(end_date_scraping)
    i=0
    while scrolling:
        show_animation(i)
        i += 1
        time.sleep(1)
        text, info, time_tag = get_content(driver)
        number_of_element = len(text)
        for i in range(0, number_of_element):
            time_ith_datetime = timetagvalue_to_datetime(time_tag[i].get_attribute("datetime"))
            if time_ith_datetime < start_date:
                scrolling = False
                print("Done!")  
                break
            if time_ith_datetime >= start_date and time_ith_datetime <= end_date:
                if time_ith_datetime < last_date:
                    time_conv = time_tag[i].get_attribute("datetime")
                    split_info = info[i].text.split("\n")
                    valid_tweet = {'text':text[i].text, 'comments':split_info[0], 'retweets':split_info[1], 'likes':split_info[2], 'date':time_conv}
                    scraped_tweets.append(valid_tweet)
        last_date = timetagvalue_to_datetime(time_tag[number_of_element-1].get_attribute("datetime"))
        elem.send_keys(Keys.PAGE_DOWN)
        elem.send_keys(Keys.PAGE_DOWN)

    return scraped_tweets   
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scraper Parameter')
    parser.add_argument('--username', dest='username', type=str, help='Profile name')
    parser.add_argument('--end_date', dest='end_date', type=str, help='the upper bound date, i.e. 2020-11-23T00:00:00')
    parser.add_argument('--start_date', dest='start_date', type=str, help='the lower bound date, i.e. 2020-11-09 23:59:59')
    args = parser.parse_args()
    #get all tweets
    tweets = get_tweets(args.username, " ".join(args.start_date.split("T")), " ".join(args.end_date.split("T")))