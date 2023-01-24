
import pprint
from bs4 import BeautifulSoup
import requests
import numpy as np

degree = input('Enter the degree you would like to explore: ')
 #use business for testing



def majors_bus_students(degree):
    school_link = 'https://bulletin.miami.edu/undergraduate-academic-programs/' + str(degree) + '/#majorsminorstext'
    data = requests.get(school_link)
    # Check link is correct
    print(school_link)
    # html Parser
    html = BeautifulSoup(data.text, 'html.parser')
    # Find data (table containing required text)
    all_data = html.find(id='majorsminorstextcontainer')
    # print(my_data)
    business_majors = all_data.find('h2', headerid="0")

    print(business_majors)
    majors_for_bus_students = []
    for nextSibling in business_majors.findNextSiblings():
        if nextSibling.name == 'h2':
            break
        else:
            majors_for_bus_students.append(nextSibling.text)

    majors_for_bus_students = majors_for_bus_students[0].split('\n')
    while ("" in majors_for_bus_students):
        majors_for_bus_students.remove("")
    return (majors_for_bus_students)

def co_majors_bus_students(degree):
    school_link = 'https://bulletin.miami.edu/undergraduate-academic-programs/' + str(degree) + '/#majorsminorstext'
    data = requests.get(school_link)
    # Check link is correct
    print(school_link)
    # html Parser
    html = BeautifulSoup(data.text, 'html.parser')
    # Find data (table containing required text)
    all_data = html.find(id='majorsminorstextcontainer')
    # print(my_data)
    business_majors = all_data.find('h2', headerid="1")
    print(business_majors)
    co_majors_for_bus_students = []
    for nextSibling in business_majors.findNextSiblings():
        if nextSibling.name == 'h2':
            break
        else:
            co_majors_for_bus_students.append(nextSibling.text)

    co_majors_for_bus_students = co_majors_for_bus_students[0].split('\n')
    while ("" in co_majors_for_bus_students):
        co_majors_for_bus_students.remove("")
    return (co_majors_for_bus_students)
def minors_bus_students(degree):
    school_link = 'https://bulletin.miami.edu/undergraduate-academic-programs/' + str(degree) + '/#majorsminorstext'
    data = requests.get(school_link)
    # Check link is correct
    print(school_link)
    # html Parser
    html = BeautifulSoup(data.text, 'html.parser')
    # Find data (table containing required text)
    all_data = html.find(id='majorsminorstextcontainer')
    # print(my_data)
    business_minors = all_data.find('h2', headerid="2")
    print(business_minors)
    minors_for_bus_students = []
    for nextSibling in business_minors.findNextSiblings():
        if nextSibling.name == 'h2':
            break
        else:
            minors_for_bus_students.append(nextSibling.text)

    minors_for_bus_students = minors_for_bus_students[0].split('\n')
    while ("" in minors_for_bus_students):
        minors_for_bus_students.remove("")
    minors_for_bus_students = [w.replace('\xa0', ' ') for w in minors_for_bus_students]
    return minors_for_bus_students
def minors_non_bus_students(degree):
    school_link = 'https://bulletin.miami.edu/undergraduate-academic-programs/' + str(degree) + '/#majorsminorstext'
    data = requests.get(school_link)
    # Check link is correct
    print(school_link)
    # html Parser
    html = BeautifulSoup(data.text, 'html.parser')
    # Find data (table containing required text)
    all_data = html.find(id='majorsminorstextcontainer')
    # print(my_data)
    business_minors = all_data.find('h2', headerid="3")
    print(business_minors)
    minors_for_non_bus_students = []
    for nextSibling in business_minors.findNextSiblings():
        if nextSibling.name == 'h2':
            break
        else:
            minors_for_non_bus_students.append(nextSibling.text)

    minors_for_non_bus_students = minors_for_non_bus_students[0].split('\n')
    while ("" in minors_for_non_bus_students):
        minors_for_non_bus_students.remove("")
    minors_for_non_bus_students = [w.replace('\xa0', ' ') for w in minors_for_non_bus_students]
    return minors_for_non_bus_students
def architecture(degree):
    school_link = 'https://bulletin.miami.edu/undergraduate-academic-programs/' + str(degree) + '/#majorstext'
    data = requests.get(school_link)
    # Check link is correct
    print(school_link)
    # html Parser
    html = BeautifulSoup(data.text, 'html.parser')
    # Find data (table containing required text)
    all_data = html.find(id='majorstextcontainer')
    # print(my_data)
    architecture_majors = all_data.find('h2')
    print(architecture_majors)
    majors_for_arc_students = []
    for nextSibling in architecture_majors.findNextSiblings():
        if nextSibling.name == 'h2':
            break
        else:
            majors_for_arc_students.append(nextSibling.text)

    majors_for_arc_students = majors_for_arc_students[0].split('\n')
    while ("" in majors_for_arc_students):
        majors_for_arc_students.remove("")
    print(majors_for_arc_students)


if degree.lower() == 'business':
        bus_choice = int(input('Would you like to see: \n1. Majors for business students '
                       '\n2. Co-Majors for business students \n3. Minors for business students'
                        '\n4. Minors for Non-Business students\n'))

# Get Majors in degree


if bus_choice == 1:
    print(majors_bus_students(degree))
elif bus_choice ==2:
    print(co_majors_bus_students(degree))
elif bus_choice == 3:
    print(minors_bus_students(degree))
elif bus_choice == 4:
    print(minors_non_bus_students(degree))
else:
    print('Please choose one of the above.')

 #Works

#def bs_accounting_finance():


#architecture(degree)



user_input = input('Enter a search keyword: ')

my_table = soup.find("table", class_='sc_courselist')
td_tags = my_table.find_all('td')
print(td_tags)
code =[]
even_class=[]
odd_class=[]

for idx, item in enumerate(codecol):
    code.append(codecol[idx].getText())

for idx, item in enumerate(even):
    even_class.append(even[idx].getText())


print(even_class)
print(odd_class)
new_title =[]


sub =[]
c_num =[]
new_code=[]
for i in range(len(code)):
    sub.append(code[i][0:3])
    c_num.append(code[i][4:])

new_code = sub

for i in range(len(code)):
    new_code[i] = new_code[i]+(c_num[i])


new_code = [x for x in new_code if 'ARC' in x or 'WRS' in x or 'MTH' in x or 'PHY' in x or 'CAE' in x]
new_code=np.array(new_code)

print(new_code.shape)
sugg_classes = []
print('classes that might interest you: ')
for i in range(len(odd_class)):
    if user_input in odd_class[i]:
        sugg_classes.append(odd_class[i])
print(sugg_classes) #Works
print(new_code) #Works







