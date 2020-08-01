import smtplib

import yaml


class Mailer:
    def __init__(self):
        with open("./Driver/config.yml", "r") as yml:
            cfg = yaml.load(yml, Loader=yaml.FullLoader)
        self._gmail_user = cfg["mail"]["username"]
        self._gmail_password = cfg["mail"]["password"]
        self._destination = "gmail@gmail.com"

    def send_email(self, job):
        sent_from = self._gmail_user
        to = self._destination
        subject = "New job has been published!"
        body = "Job Description: " + job.get_description() + "\n Company: " + job.get_company() + "\n Link: " + job.get_link()

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self._gmail_user, self._gmail_password)
            server.sendmail(sent_from, self._destination, email_text)
            server.close()
            print('Email sent!')
        except Exception as e:
            print(e)
