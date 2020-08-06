import yaml

from Controller.ChooseFactory import WebChooser
from Driver.MailDriver import Mailer
from Driver.Mongo import Driver


class Manage():
    def __init__(self, enable_auto_send_resume=False):
        self._all_jobs = []
        self._websites = []
        self._num_of_jobs = 0
        self.__auto_send_resume = enable_auto_send_resume

    def get_websites(self):
        return self._websites

    def get_num_of_jobs(self):
        return self._numOfJobs

    def get_type(self, url):
        if "indeed" in url:
            return "indeed"
        elif "glassdoor" in url:
            return "glassdoor"
        elif "linkedin" in url:
            return "linkedin"

    def add_website(self, url):
        try:
            # Get MongoDB driver
            with open("./Driver/config.yml", "r") as yml:
                cfg = yaml.load(yml, Loader=yaml.FullLoader)
            database = Driver().instance[cfg["mongodb"]["database"]]
            collection = database[cfg["mongodb"]["collection"]]

            # Get the correct object by factory method
            type = self.get_type(url)
            website = WebChooser(type, url)

            # Get all the jobs for the current website
            website.get_jobs()
            jobs = website.get_all_jobs()
            self._websites.append(website)
            mail_driver = Mailer().server
            # Looping through all found jobs and check if already exist in the database
            for job in jobs:
                if self.is_job_exist(job, collection) is False:
                    self.add_new_job(job, collection)
                    Mailer().send_email(job, type, mail_driver)
                job.print_job()
            mail_driver.close()
        except Exception as e:
            print('An error occurred when tried to add a new website')
            print(e)

    def is_job_exist(self, job, collection):
        try:
            existence_status = collection.count_documents({'Job Title': job.get_description()}, limit=1)
            if existence_status > 0:
                # Job exist
                return True
            else:
                # Job does not exist
                return False
        except Exception as e:
            print('An error occurred when tried to find job existence status')
            print(e)

    def add_new_job(self, job, collection):
        try:
            jobDict = {"Job Title": job.get_description(),
                       "Company": job.get_company(),
                       "Link": job.get_link()}
            collection.insert_one(jobDict)
            print("NEW!!")
            self._all_jobs.append(job)
            self._num_of_jobs += 1
        except Exception as e:
            print("An error occurred when tried to add a new job to MongoDB Atlas")