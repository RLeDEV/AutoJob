from Controller.Manage import Manage
from Driver.Mongo import Driver

if __name__ == '__main__':
    firefox_instance = Driver().instance

    manage = Manage()
    print("Indeed")
    manage.add_website("https://il.indeed.com/jobs?q=student+developer&l=%D7%99%D7%A9%D7%A8%D7%90%D7%9C")
    print("\n\nGlassdoor")
    manage.add_website("https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=Student+Software&locT=N&locId=119&jobType=&context=Jobs&sc.keyword=Student+Software&dropdown=0")

    firefox_instance.close()
