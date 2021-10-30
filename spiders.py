import newspaper
import util
import config
from bs4 import BeautifulSoup
import time
import re
import datetime


def to_publish_date(publish_time):
    if "mins" in publish_time:
        publish_date = time.strftime('%Y-%m-%d',
                                     time.localtime(time.time() - 60 * int(re.findall("\d+", publish_time)[0])))
    elif "hours" in publish_time:
        publish_date = time.strftime('%Y-%m-%d',
                                     time.localtime(time.time() - 3600 * int(re.findall("\d+", publish_time)[0])))
    else:
        publish_date = time.strftime('%Y-%m-%d',
                                     time.localtime(time.time() - 86400 * int(re.findall("\d+", publish_time)[0])))

    return publish_date


# -----------------------------------------------------------------------------------------------------------------------
# 1网页过滤-FoxNews
def FoxNews(searchers):
    searchers = [i for i in searchers if "-" in i.url]
    searchers = [i for i in searchers if "foxnews.com" in i.url]
    searchers = [i for i in searchers if "/video." not in i.url and "/radio." not in i.url]

    return searchers


# 1记者-FoxNews
def FoxNews_getAuthor(article):
    html = BeautifulSoup(article.html, 'lxml')
    authors = html.select("div.author-byline > span > span > a")
    authors = [author.text for author in authors]
    if len(authors) == 0:
        authors = html.select("div.author-byline > span > span")
        authors = [author.text for author in authors]

    return authors


# 1出版日期-FoxNews
def FoxNews_getPublishDate(article):
    html = BeautifulSoup(article.html, 'lxml')
    publish_time = html.select("div.article-date > time")
    publish_time = [T.text for T in publish_time]
    if len(publish_time) == 1:
        publish_date = to_publish_date(publish_time[0])
    else:
        publish_date = "None"

    return publish_date


# 1类型-FoxNews
def FoxNews_getCategory(article):
    html = BeautifulSoup(article.html, 'lxml')
    category = html.select("div.eyebrow > a")
    category = [T.text for T in category]
    if len(category) == 0:
        category = ["None"]

    return category[0]


# -----------------------------------------------------------------------------------------------------------------------
# 2网页过滤-USAToday
def USAToday(searchers):
    searchers = [i for i in searchers if "-" in i.url]
    searchers = [i for i in searchers if "usatoday.com" in i.url]
    searchers = [i for i in searchers if "usatoday.com/videos" not in i.url
                 and "usatoday.com/media" not in i.url
                 and "cm.usatoday.com" not in i.url
                 and "usatoday.com/picture-gallery" not in i.url]

    return searchers


# 2记者-USAToday
def USAToday_getAuthor(article):
    html = BeautifulSoup(article.html, 'lxml')
    authors = html.select("div.gnt_ar_by > a")
    if len(authors) > 0:
        authors = [author.text for author in authors]
    else:
        authors = html.select("div.gnt_ar_by")
        if len(authors) > 0:
            authors = [author.text for author in authors]
        else:
            authors = html.select("span.topper_byline")
            authors = [author.text for author in authors]
    if len(authors) > 0:
        author = authors[0]
        authors = author.replace(' and ', ',').split(',')
        return authors
    else:
        noAuthor = []
        return noAuthor


# 2出版日期-USAToday
def USAToday_getPublishDate(article):
    publish_date = article.publish_date
    if publish_date is None:
        return "None"

    return publish_date.strftime('%Y-%m-%d')


# 2类型-USAToday
def USAToday_getCategory(article):
    html = BeautifulSoup(article.html, 'lxml')
    category = html.select("div.gnt_ar_lbl > a")
    category = [T.text for T in category]
    if len(category) == 0:
        category = ["None"]

    return category[0]


# -----------------------------------------------------------------------------------------------------------------------
# 3网页过滤-ABCNews
def ABCNews(searchers):
    searchers = [i for i in searchers if "-" in i.url]
    searchers = [i for i in searchers if "abcnews.go.com" in i.url]
    searchers = [i for i in searchers if "/video/" not in i.url
                 and "/photos/" not in i.url
                 and "/photo/" not in i.url]

    return searchers


# 3记者-ABCNews
def ABCNews_getAuthor(article):
    html = BeautifulSoup(article.html, 'lxml')
    authors = html.select("div.Byline__Author")
    authors = [author.text for author in authors]
    print(authors)
    return authors


# 3出版日期-ABCNews
def ABCNews_getPublishDate(article):
    html = BeautifulSoup(article.html, 'lxml')
    publish_time = html.select("div.Byline__Meta.Byline__Meta--publishDate")
    publish_time = [T.text for T in publish_time]
    print(publish_time)
    if len(publish_time) == 1:
        try:
            publish_time1 = publish_time[0].split(",")[0].replace(" ", "")
            print(publish_time)
            publish_date = datetime.datetime.strptime(publish_time1, '%d%B%Y').strftime('%Y-%m-%d')
            print(publish_date)
        except ValueError:
            day_month = publish_time[0].split(",")[0]
            day = day_month.split(" ")[1]
            month = day_month.split(" ")[0]
            year = publish_time[0].split(",")[1].replace(" ", "")
            publish_date = datetime.datetime.strptime(day + month + year, '%d%B%Y').strftime('%Y-%m-%d')
            print(publish_date)
    else:
        publish_date = "None"

    print(publish_date)
    return publish_date


# 3类型-ABCNews
def ABCNews_getCategory(article):
    category = article.url.replace("//", "").split("/")[1]

    return category


# -----------------------------------------------------------------------------------------------------------------------
# 4网页过滤-LATimes
def LATimes(searchers):
    searchers = [i for i in searchers if "-" in i.url]
    searchers = [i for i in searchers if "latimes.com" in i.url]
    searchers = [i for i in searchers if "marketplace.latimes.com" not in i.url
                 and "placeanad.latimes.com" not in i.url]

    return searchers


# 4记者-LATimes
def LATimes_getAuthor(article):
    html = BeautifulSoup(article.html, 'lxml')
    authors = html.select("div.ArticlePage-authorName > a > span")
    authors = [author.text for author in authors]
    if len(authors) == 0:
        authors = html.select("div.ArticlePage-BylineText")
        authors = [author.text for author in authors]
    if len(authors) == 0:
        authors = html.select("div.ArticlePage-bylineText")
        authors = [author.text for author in authors]
    if len(authors) == 0:
        authors = ["None"]

    return authors


# 4出版日期-LATimes
def LATimes_getPublishDate(article):
    publish_date = article.publish_date
    if publish_date is None:
        return "None"

    return publish_date.strftime('%Y-%m-%d')


# 4类型-LATimes
def LATimes_getCategory(article):
    html = BeautifulSoup(article.html, 'lxml')
    category = html.select("div.ArticlePage-breadcrumbs > a")
    category = [T.text for T in category]
    if len(category) == 0:
        category = html.select("div.StoryStackPage-breadcrumbs > a")
        category = [T.text for T in category]
        if len(category) == 0:
            category = ["None"]

    return category[0]


# -----------------------------------------------------------------------------------------------------------------------
# 5网页过滤-CNN
def CNN(searchers):
    searchers = [i for i in searchers if "-" in i.url]
    searchers = [i for i in searchers if "cnn.com" in i.url]
    searchers = [i for i in searchers if "cnn.com/video" not in i.url
                 and "cnn.com/style" not in i.url
                 and "cnn.com/travel" not in i.url
                 and "cnn.com/interactive" not in i.url
                 and "cnn.com/weather" not in i.url
                 and "cnn.com/specials" not in i.url
                 and "cnnespanol.cnn.com" not in i.url
                 and "bleacherreport.com" not in i.url
                 and "comparecards.com" not in i.url
                 and "arabic.cnn.com" not in i.url]

    return searchers


# 5记者-CNN
def CNN_getAuthor(article):
    authors = article.authors
    if authors is None or authors == []:
        return "None"

    return authors


# 5出版日期-CNN
def CNN_getPublishDate(article):
    publish_date = article.publish_date
    if publish_date is None:
        return "None"

    return publish_date.strftime('%Y-%m-%d')


# 5类型-CNN
def CNN_getCategory(article):
    category = article.url.replace("//", "").split("/")[4]
    print(category)
    return category


# -----------------------------------------------------------------------------------------------------------------------
# 构建新闻源
def build_source(url):
    print("website:", url)

    return newspaper.build(url, language=config.language, memoize_articles=False)


# 展示新闻源
def display_source(searchers):
    print("length:", len(searchers))
    for i in searchers:
        print(i.url)


def spider(site, save_type):
    # 构建新闻源
    news_paper = build_source(config.urls[site])

    # 文件名
    filename = config.newspapers[site]
    # 如果是保存csv格式 需要提前创建文件
    if save_type:  # 表示存储的是csv文件
        util.create_csv(filename)

    # 展示现状
    searchers = config.switch_filter[site](news_paper.articles)
    display_source(searchers)

    # 如果searchers有元素就一直爬下去
    while len(searchers) > 0:
        article = searchers[0]
        print(article.url)
        try:
            print("尝试下载！")
            article.download()
            article.parse()

            # article.nlp()
            # print("keywords", article.keywords)
            # print("summary", article.summary)

            # 写入文件
            if article.text != "":
                print("有东西！")
                authors = config.switch_author[site](article)
                publish_date = config.switch_date[site](article)
                category = config.switch_category[site](article)
                print(publish_date)
                if publish_date != "None":
                    if save_type:
                        util.write_csv(filename, article.title, category, authors, publish_date, article.text)
                    else:
                        util.write_txt(filename, article.title, category, authors, publish_date, article.text)

            #   查看是否需要新增资源
            if len(searchers) > 1000:
                factor = config.factor_max
            elif len(searchers) > 500:
                factor = config.factor_mid
            else:
                factor = config.factor_min

            if len(searchers) < factor and len(searchers) % factor == 1:
                news_paper = build_source(article.url)
                new_searchers = config.switch_filter[site](news_paper.articles)
                if len(news_paper.articles):
                    searchers += new_searchers
                    print(len(new_searchers), "->", len(searchers))

        except newspaper.article.ArticleException:
            print("Exception!")
            continue
        finally:
            searchers.pop(0)
            print("----searchers->", len(searchers))
