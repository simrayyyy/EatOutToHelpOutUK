import requests
import html

#I will use L39 4QP as an example, there are only 2 lines of code that you need to change information in!

#This is to create a .txt file, change the text "L394QP" to any name of the .txt file that you would like to save the information in
f = open('L394QP.txt', 'w')

#Change the postcode to another one that you would like to use
url = 'https://www.tax.service.gov.uk/eat-out-to-help-out/find-a-restaurant/results?postcode=l39+4qp'
r = requests.get(url)
r = r.text

for line in r.splitlines():
    if '<h3 class="govuk-heading-m"' in line:
        y = line.split('>')[1]
        y = y.split('<')[0]
        y = html.unescape(y)
    if 'govuk-results-address govuk-body' in line:
        x = line.split('>')[1]
        x = x.split('<')[0]
        '''
        for lines in x:
            x = str(x)[1:-1]
            #x = x.replace(" ", "+")
        print(x, end="\n")
        '''
        x = html.unescape(x)
        print(y, ',', x, end="\n")
        f.write(f'{y} \ {x}\n')
f.close()
