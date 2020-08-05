import requests
import html

# The script will ask you to input your post code.
print("Please enter your post code.")
print("Please note that spacing is required.")
print("E.g. 'L39 4QP'\n")
print('Enter your post code:')
postcode = input()
postcode = str(postcode)

# This is to create a .txt file in the script's directory, with the file name being the post code specified.
f = open(postcode + '.txt', 'w')

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
        print(y, ',', x, end="\n")
        f.write(f'{y} \ {x}\n')
f.close()
