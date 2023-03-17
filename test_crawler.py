from crawler import Crawler

email = "your-email@example.com"
names = ["Gurke M"]
clr = Crawler(names, email)
clr.add_author(names[0])
