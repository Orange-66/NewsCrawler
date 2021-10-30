import csv
import config
import os


def write_txt(filename, title, category, authors, publish_date, text):
    print("正在存储->" + title)
    path = config.prefix + filename + config.postfix + ".txt"
    with open(path, "a", encoding='utf-8') as f:
        f.write("[title]" + str(title) + "\n"
                "[category]" + str(category) + "\n"
                "[authors]" + str("_".join(authors)) + "\n"
                "[publish_date]" + str(publish_date) + "\n"
                "[text]" + str(text).replace('\n', '') + "\n")
        f.close()

    print("-" * 20)


def write_csv(filename, title, category, authors, publish_date, text):
    print("正在存储->" + title)
    path = config.prefix + filename + config.postfix + ".csv"
    with open(path, 'a+', encoding='utf-8-sig') as f:
        csv_write = csv.writer(f)
        data_row = [str(title), str(category), str("_".join(authors)), str(publish_date), str(text).replace('\n', '').replace('\r', '').replace('\t', '')]
        print(data_row)
        try:
            csv_write.writerow(data_row)
        except UnicodeEncodeError:
            print("保存失败！")

    print("-" * 50)


def create_csv(filename):
    print("正在创建->" + filename)
    path = config.prefix + filename + config.postfix + ".csv"
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8-sig') as f:
            csv_write = csv.writer(f)
            csv_head = ["title", "category", "authors", "publish_date", "text"]
            csv_write.writerow(csv_head)
