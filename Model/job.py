class Job:
    def __init__(self, description, link, company="No company initialized"):
        self._description = description
        self._link = link
        self._company = company

    def get_description(self):
        return self._description

    def get_link(self):
        return self._link

    def get_company(self):
        return self._company

    def set_description(self, description):
        self._description = description

    def set_link(self, link):
        self._link = link

    def set_company(self, company):
        self._company = company

    def print_job(self):
        print("Description: " + self.get_description() + "\nCompany: " + self.get_company() + '\nLink: ' +self.get_link())