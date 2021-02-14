from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


response = requests.get('https://www.southafrica.to/accommodation/Cape-Town/Cape-Town-hotels.php')

capetown_hotels = response.text

list_of_emails = []
email_list = []

soup = BeautifulSoup(capetown_hotels, 'html.parser')
text = soup.getText()
mail_tos = soup.select('a[href^=mailto]')
unfiltered_list = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", text)
# emails = soup.find_all(name='a')

# Extract emails
for i in mail_tos:
    if i.string != None:
        email_list.append(i.string.encode('utf-8').strip())

for email_link in unfiltered_list:
    # email_text = email_link.getText()
    list_of_emails.append(email_link)

print(list_of_emails)
print(len(list_of_emails))

print(len(email_list))
print(email_list)

df = pd.DataFrame(email_list, columns=["Email"])
dfw = pd.DataFrame(list_of_emails, columns=["Email"]) # replace with column name you prefer
df.to_csv('email.csv', index=False)
dfw.to_csv('email2.csv', index=False)
