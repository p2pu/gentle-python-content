import codecs
from datetime import datetime
import json

with open('./emails/emails.json', 'r') as inf:
    emails = json.load(inf)

[datetime.strptime(e['date_sent'], "%Y-%m-%dT%H:%M:%S.%f") for e in emails]

for email in emails:
    with codecs.open("./emails/" + email['date_sent'] + " " + email['subject'] + ".txt1", 'w', "utf-8") as outfile:
        outfile.write(email['text_body'])

