import csv
from nameparser import HumanName

names = [name.strip() for name in open('raw_name.txt', 'r').readlines()]
emails = [email.strip() for email in open('raw_emails.txt', 'r').readlines()]

writer = csv.writer(open('data.csv', 'a'))
row_name = ['prefix', 'firstname', 'middlename', 'lastname', 'email']
writer.writerow(row_name)

for name, email in zip(names, emails):
    hn = HumanName(name)
    row = [hn.title, hn.first, hn.middle, hn.last, email]
    print(row)
    writer.writerow(row)
