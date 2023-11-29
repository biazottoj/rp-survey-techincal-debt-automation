import time
import fire

from mail import EmailBuilder, EmailSender


def send_emails(contacts_file, email_template, login_secret_file, sender_name, subject, interval=1, dry_run=True,
                email_server_smtp_address="smtp.gmail.com", email_server_smtp_port=587):
    """
    High-level function to send the emails.
    :param contacts_file: the file containing the contacts to send the emails to.
    :param email_template: the file containing the template string of the email body.
    :param login_secret_file: the file containing your credentials to login to the SMTP server.
    :param sender_name: the name of the sender to be displayed to the receiver.
    :param subject: the subject of the email as template string.
    :param interval: the time to wait between each email sent. This helps to avoid spamming! Set to 0 to not wait.
    :param dry_run: IMPORTANT! This parameter prevents from sending the emails involuntarily.
    Set to true (default) to run a dry-run of the script and ensure you set everything correctly.
    Set to false when you are ready to send the emails for real! Interval is ignored if this is set to true.
    :param email_server_smtp_address the server's SMTP address. Default is Google's one
    :param email_server_smtp_port the server's SMTP port. Default is Google's one
    """
    email_builder = EmailBuilder(contacts_file, email_template)
    emails = email_builder.create_emails(sender_name, subject)
    sender = EmailSender(host=email_server_smtp_address, smtp_port=email_server_smtp_port)
    sender.login_with_secret(login_secret_file)

    if not dry_run:
        print(f"You are about to send {len(emails)} from your '{sender_name}' address with subject '{subject}'.")
        reply = input("Do you wish to proceed? [yes/no] ")
        if reply != "yes":
            print("No emails will be sent.")
            exit(0)

    for i, email in enumerate(emails):
        print(f"Sending email {i+1} from {email.sender} to {email.to} with subject '{email.subject}'")
        if not dry_run:
            sender.send_email(email)
        if not dry_run:
            print(f"Waiting {interval} second(s)...")
            time.sleep(interval)
    print("Completed sending emails.")
    sender.close()


def test_email():
    """
    An example on how to use the APIs to send the emails.
    """
    email_template = 'data/email-template.txt'
    contacts_file = 'data/contacts.csv'
    email_builder = EmailBuilder(contacts_file, email_template)
    test_email = email_builder.create_emails("d.d.sas@rug.nl", "Test Email $project")[1]

    sender = EmailSender(host="smtp.gmail.com", smtp_port=587)
    sender.login_with_secret("data/login.secret")
    sender.send_email(test_email)
    print("Email sent")
    sender.close()


if __name__ == '__main__':
    fire.Fire()
