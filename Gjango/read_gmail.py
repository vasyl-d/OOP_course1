from gmailconnector.read_email import ReadEmail

gmail_user = '911@profitag.ua'
gmail_pass = 'profitag911'

reader = ReadEmail(gmail_user, gmail_pass, folder='"[Gmail]/All Mail"')  # Folder defaults to inbox
response = reader.instantiate(category='UNSEEN')  # Search criteria defaults to UNSEEN
if response.ok:
    unread_emails = reader.read_email(response.body)
    for each_mail in list(unread_emails):
        print(each_mail)
else:
    print(response.body)