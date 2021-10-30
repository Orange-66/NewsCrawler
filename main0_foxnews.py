import config
import spiders


def spider():
    print("请选择爬虫网址：")
    for i in range(0, len(config.newspapers)):
        print((i + 1), "-", config.newspapers[i])
    # site = int(input()) - 1
    site = 0

    print("请选择保存文件格式：\n"
          "1.txt格式\n"
          "2.csv格式")
    # save_type = int(input()) - 1
    save_type = 1

    spiders.spider(site, save_type)


if __name__ == '__main__':
    spider()
