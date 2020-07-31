from Model.job import Job
from Model.website import Website
from Driver.WebDriver import WebDriver

class Indeed(Website):
    def __init__(self, url):
        self._url = url
        self._classname = "jobtitle"
        self._jobs = []

    def get_all_jobs(self):
        return self._jobs

    def get_jobs(self):
        final_jobs = []

        # Getting into the requested jobs page
        driver = WebDriver().driver
        driver.get(self._url)
        try:
            # Getting the elements
            all_jobs_elements = driver.find_elements_by_class_name(self._classname)
            all_jobs_company = driver.find_elements_by_class_name("company")

            # Looping through elements and making Job objects for new jobs.
            for (description, company) in zip(all_jobs_elements, all_jobs_company):
                link = description.get_attribute("href")
                if "Student" in description.text or "student" in description.text:
                    job = Job(description.text, link, company.text)
                    final_jobs.append(job)
                    job.print_job()

            self._jobs = final_jobs
            return final_jobs
        except Exception as e:
            print('An error occured while tried to get indeed jobs')
            print(e)
