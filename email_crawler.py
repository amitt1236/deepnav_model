"""
Email crawler script
go Through all of the unseen massages and saves their attachments if exist.
marks all of the unseen massages as seen.
"""

import imaplib, getpass
import email
import datetime

output_dir = "/Users/amitaflalo/Desktop/deepnav/data/email"


def crawl(email_address):
    num = 0
    M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    M.login(email_address, getpass.getpass())
    M.select("Inbox")
    (retcode, messages) = M.search(None, '(UNSEEN)')
    if retcode == 'OK':
        for massage in messages[0].split():
            num = num + 1
            print("processing " + str(num))
            downloadAttachment(M, massage, output_dir)
            M.store(messages[0], '+FLAGS', '\Seen')
    if num == 0:
        print("No new messages")
    M.close()
    M.logout()


def downloadAttachment(M, massage, output_dir):
    resp, data = M.fetch(massage, "(BODY.PEEK[])")
    massage_body = data[0][1]
    mail = email.message_from_bytes(massage_body)
    if mail.get_content_maintype() != 'multipart':
        return
    for part in mail.walk():
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            open(output_dir + '/' + str(datetime.datetime.now()) + ".csv", 'wb').write(part.get_payload(decode=True))


if __name__ == "__main__":
    crawl("deep.nav.data@gmail.com")
