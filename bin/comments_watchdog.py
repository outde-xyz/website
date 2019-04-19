#!/usr/bin/env python3

from imapclient import IMAPClient

server = IMAPClient('imappro.zoho.com', use_uid=True)
server.login('admin@outde.xyz', '1Nkd_Ps!Eu_S0a6J')

status, messages = mail.select('Comments')


if status != "OK": exit("Incorrect mail box")

# iterste over all messages
for i in range(1, int(messages[0])):
    _, msg = mail.fetch(str(i), '(RFC822)')
    for response in msg:
        if isinstance(response, tuple):
            msg2 = email.message_from_bytes(response[1])
            print (msg2["subject"])


# keep listening to mailbx;
# make sure to use app-specific password

# read in email

# convert to post

# write to destination

# commit and push to master (switch github ssh key)

# mark email as read
