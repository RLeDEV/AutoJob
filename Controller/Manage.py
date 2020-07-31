from Controller.ChooseFactory import WebChooser

class Manage():
    def __init__(self):
        self._all_jobs = []
        self._websites = []
        self._num_of_jobs = 0

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
            # Get the correct object by factory method
            type = self.get_type(url)
            website = WebChooser(type, url)

            # Get all the jobs for the current website
            website.get_jobs()
            jobs = website.get_all_jobs()
            self._websites.append(website)
            # Looping through all found jobs and check if already exist in the database
            for job in jobs:
                if self.is_job_exist(job) is False:
                    self._num_of_jobs += 1
                    self._all_jobs.append(job)
        except Exception as e:
            print('An error occured when tried to add a new website')

    def is_job_exist(self, job):
        return False