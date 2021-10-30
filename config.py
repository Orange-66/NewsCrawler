import spiders

prefix = "./dataset/"
postfix = "-data"
# language = "zh"
language = "en"
newspapers = ["FoxNews", "USAToday", "ABCNews", "LATimes", "CNN"]

switch_filter = {0: spiders.FoxNews,
                 1: spiders.USAToday,
                 2: spiders.ABCNews,
                 3: spiders.LATimes,
                 4: spiders.CNN}

switch_author = {0: spiders.FoxNews_getAuthor,
                 1: spiders.USAToday_getAuthor,
                 2: spiders.ABCNews_getAuthor,
                 3: spiders.LATimes_getAuthor,
                 4: spiders.CNN_getAuthor}

switch_date = {0: spiders.FoxNews_getPublishDate,
                 1: spiders.USAToday_getPublishDate,
                 2: spiders.ABCNews_getPublishDate,
                 3: spiders.LATimes_getPublishDate,
                 4: spiders.CNN_getPublishDate}

switch_category = {0: spiders.FoxNews_getCategory,
                 1: spiders.USAToday_getCategory,
                 2: spiders.ABCNews_getCategory,
                 3: spiders.LATimes_getCategory,
                 4: spiders.CNN_getCategory}

urls = ["https://www.foxnews.com/",
        "https://www.usatoday.com/",
        "https://abcnews.go.com/",
        "https://www.latimes.com/",
        "https://edition.cnn.com/"]

factor_min = 32
factor_mid = 64
factor_max = 128
