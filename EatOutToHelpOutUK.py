import requests
import html
import csv

# The script will ask you to input your post code.
print("Please enter your post code.")
print("Please note that spacing is required.")
print("E.g. 'L39 4QP'\n")
print('Enter your post code:')
postcode = input()
postcode = str(postcode)

# This is to create a .csv file in the script's directory, with the file name being the post code specified.
f = open(postcode + '.csv', 'w', newline='')
csvwriter = csv.writer(f, delimiter=",")
f.write("Name, Address\n")

# The list of registered restaurants within 5 miles of the specified postcode will be obtained from the government website.
postcode = postcode.split(' ')
url = 'https://www.tax.service.gov.uk/eat-out-to-help-out/find-a-restaurant/results?postcode=' + \
    postcode[0] + '+' + postcode[1]

r = requests.get(url)
r = r.text

# The script will extract the site's data to obtain the restaurant's name and its corresponding address.
for line in r.splitlines():
    if '<h3 class="govuk-heading-m"' in line:
        y = line.split('>')[1]
        y = y.split('<')[0]
        y = html.unescape(y)
    if 'govuk-results-address govuk-body' in line:
        x = line.split('>')[1]
        x = x.split('<')[0]
        x = html.unescape(x)
        result = (y, x)
        print(result)
        csvwriter.writerow(result)
print('\n')
print(str(postcode[0] + ' '+postcode[1]) +
      '.csv has been created on your computer. You may now import the .csv file into google maps.')
print('If your .csv file is empty, please check if there are indeed participating restaurants in your area.')
f.close()
