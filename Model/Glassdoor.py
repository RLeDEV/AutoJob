from Model.job import Job
from Model.website import Website
from Driver.WebDriver import WebDriver

class Glassdoor(Website):
    def __init__(self, url):
        self._url = url
        self._classname = "(//div[@class='jobContainer'])"
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
            allJobEle = driver.find_elements_by_xpath(self._classname)

            # Looping through elements and making Job objects for new jobs.
            for jobEle in allJobEle:
                jobArr = jobEle.text.split('\n')
                linkEle = jobEle.find_element_by_tag_name("a")
                link = linkEle.get_attribute("href")
                company = jobArr[0]
                description = jobArr[1]
                if ("Student" in description or "student" in description):
                    job = Job(description, link, company)
                    final_jobs.append(job)
                    job.print_job()

            self._jobs = final_jobs
            return final_jobs
        except Exception as e:
            print('An error occured while tried to get Glassdoor jobs')
            print(e)