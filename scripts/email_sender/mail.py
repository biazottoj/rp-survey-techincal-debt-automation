from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from typing import List, Tuple
import csv
import os.path
import smtplib

@dataclass
class Email:
    """
        Models an email.
    """

    sender: str
    to: str
    subject: str
    message: str

    def to_mime(self) -> MIMEMultipart:
        mime = MIMEMultipart()
        mime['From'] = self.sender
        mime['To'] = self.to
        mime['Subject'] = self.subject
        mime.attach(MIMEText(self.message, 'plain'))
        return mime


class EmailSender:
    """
        Connects to a SMPT server and allows to send emails.
    """

    def __init__(self, host: str, smtp_port: int):
        """

        :param host:
        :param smtp_port:
        """
        self.s = smtplib.SMTP(host=host, port=smtp_port)
        self.s.starttls()

    def login_with_secret(self, secret_file_path):
        """
        Login to the SMTP server using username and password contained in the given file.
        :param secret_file_path: a file containing on the first line the username to use for login and
        on the second line the password.
        """
        with open(secret_file_path, 'r') as secret:
            lines = secret.readlines()
        if len(lines) != 2:
            raise ValueError("Secret file does not contain exactly two lines. One line for username and one for password.")
        self.login(lines[0], lines[1])

    def login(self, username: str, password: str):
        """
        Logins to the SMTP server with the given username and password
        """
        self.s.login(username, password)

    def send_email(self, email: Email):
        """
        Sends the provided email.
        """
        self.s.send_message(email.to_mime())

    def close(self):
        self.s.close()


class EmailBuilder:
    """
    Constructs emails starting from a CSV file containing the contacts and a template file containing
    the template of the email.
    """

    def __init__(self, contacts_csv_file, template_file):
        """
        Initializes this builder.
        :param contacts_csv_file: the CSV containing the email contacts
        :param template_file: a file containing the body of the email as a template string.
        For more info on template strings go to https://docs.python.org/3/library/string.html#template-strings
        """
        self.contacts = EmailBuilder.__read_contacts__(contacts_csv_file)
        self.template = EmailBuilder.__read_email_template__(template_file)

    def create_emails(self, sender, subject: str):
        """
        Builds the Email objects.
        :param sender: The name of the sender. This is not your email, but rather the name you want to be displayed
        as Sender to the receiver. Typically, this should be your name.
        :param subject: A template string to use as subject to your emails.
        :return:
        """
        emails = []
        subj_temp = Template(subject)
        for c in self.contacts:
            custom_subject = subj_temp.substitute(project=c[0], name=c[1], email=c[2])
            message = self.template.substitute(project=c[1], name=c[3], email=c[2], owner=c[0])
            emails.append(Email(sender, c[2], custom_subject, message))
        return emails

    @staticmethod
    def __read_contacts__(csv_file: str):
        """
        
        Reads the CSV file containing the contacts
        """
        contacts_list = []
        with open(csv_file, mode='r', encoding='utf-8') as contacts:
            for contact in csv.DictReader(contacts):
                contacts_list.append((contact["owner"],contact["project"],contact["email"],contact["first-name"]))
        return contacts_list

    @staticmethod
    def __read_email_template__(file: str) -> Template:
        """
        Reads the file containing the email body template..
        :param file:
        :return:
        """
        with open(file, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)
