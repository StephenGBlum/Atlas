
import pprint
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

degree = input('Enter the degree you would like to explore: ')
 #use business for testing
program_index = 'https://bulletin.miami.edu/program-index/'
def get_program_links(program_index):
    data = requests.get(program_index)
    html = BeautifulSoup(data.text, 'html.parser')

    tables = html.find_all('table')
    table = html.find('table', class_='sorttable')

         #columns = row.find_all('td')

    rows =[]
    columns=[]
    links =[]
    for row in table.find_all('tr'):
        column = row.find_all('td')
        #lines=row.text.splitlines()
        columns.append(column)
        for link in row.find_all('a'):
            links.append(link.get('href'))
        #rows.append(lines[0])
    return links

def get_program_names(program_index):
    data = requests.get(program_index)
    html = BeautifulSoup(data.text, 'html.parser')

    tables = html.find_all('table')
    table = html.find('table', class_='sorttable')

    # columns = row.find_all('td')

    rows = []
    columns = []
    names =[]
    for row in table.find_all('tr'):
        column = row.find_all('td')[0].text
        names.append(column)
    return(names)

def get_program_type(prgram_index):
    data = requests.get(program_index)
    html = BeautifulSoup(data.text, 'html.parser')

    tables = html.find_all('table')
    table = html.find('table', class_='sorttable')

    # columns = row.find_all('td')

    rows = []
    columns = []
    types = []
    for row in table.find_all('tr'):
        column = row.find_all('td')[2].text
        types.append(column)
    return (types)


#print(len(get_program_names(program_index)))
#print(len(get_program_links(program_index)))
#print(len(get_program_type(program_index)))
all_courses = np.stack((get_program_names(program_index),get_program_type(program_index),get_program_links(program_index)),axis=1)
print(all_courses[0])
def majors_bus_students(degree):
    school_link = 'https://bulletin.miami.edu/undergraduate-academic-programs/' + str(degree) + '/#majorsminorstext'
    data = requests.get(school_link)
    # Check link is correct
    #print(school_link)
    # html Parser
    html = BeautifulSoup(data.text, 'html.parser')
    # Find data (table containing required text)
    all_data = html.find(id='majorsminorstextcontainer')
    # print(my_data)
    business_majors = all_data.find('h2' ,headerid="0")


    #print(business_majors)
    links=[]
    #for link in all_data.findAll('a'):
    #    links.append(link.get('href'))
    #print(links)

    majors_for_bus_students = []
    for nextSibling in business_majors.findNextSiblings():
        if nextSibling.name == 'h2':
            break
        else:
            for link in nextSibling.findAll('a'):
                links.append(link.get('href'))
            majors_for_bus_students.append(nextSibling.text)


    #majors_for_bus_students = majors_for_bus_students[0].split('\n')
    #while ("" in majors_for_bus_students):
    #   majors_for_bus_students.remove("")
    #print(links)
    return (links)

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
    #print(architecture_majors)
    majors_for_arc_students = []
    links =[]
    for nextSibling in architecture_majors.findNextSiblings():
        if nextSibling.name == 'h2':
            break
        else:
            for link in nextSibling.findAll('a'):
                links.append(link.get('href'))
            majors_for_arc_students.append(nextSibling.text)

    majors_for_arc_students = majors_for_arc_students[0].split('\n')
    while ("" in majors_for_arc_students):
        majors_for_arc_students.remove("")
    #print(majors_for_arc_students)
    return links

#print(architecture(degree))
if degree.lower() == 'business':
        bus_choice = int(input('Would you like to see: \n1. Majors for business students '
                       '\n2. Co-Majors for business students \n3. Minors for business students'
                        '\n4. Minors for Non-Business students\n'))
        if bus_choice == 1:
            print(majors_bus_students(degree))
        elif bus_choice == 2:
            print(co_majors_bus_students(degree))
        elif bus_choice == 3:
            print(minors_bus_students(degree))
        elif bus_choice == 4:
            print(minors_non_bus_students(degree))
        else:
            print('Please choose one of the above.')

# Get Majors in degree




 #Works

carriculum_link = "https://bulletin.miami.edu" #add link from array + #curriculumtext
def carriculum_parser(carriculum_link, degree_link, plan_of_study_ext = "#planofstudytext"):
    course_data_link = carriculum_link+degree_link+plan_of_study_ext
    data = requests.get(course_data_link)

    html = BeautifulSoup(data.text, 'html.parser')
    # Find data (table containing required text)
    tables = html.find_all('table')
    table = html.find('table', class_='sc_plangrid')
    print(table)
    rows=[]

    for row in table.find_all('tr'):


    #run for loop here for table rows

        #even_titles = table.find_all('tr')
        even = row.find('tr',class_='even')
        #print(even)
        codes = row.find_all('td')
        code = row.find('td',class_='codecol')
        lines = row.text.splitlines()
        rows.append(lines[0])
    new_list=[]
    positions =[]
    print(rows)
    for i in range(0,len(rows)):
        if 'Hours' in rows[i]:
            positions.append(i)

    new_list=[]
    temp =[]
    print(positions)
    for i in range(len(positions)-1):
        temp = rows[positions[i]:positions[i+1]]
        print(temp)
        new_list.append(temp)
        #temp.clear()

    print(new_list)





        #print(code)
    #print(titles)

        #print(even)


carriculum_parser(carriculum_link, all_courses[0][2], '#planofstudytext')
#print('Number of Majors in Degree: ',len(architecture(degree)))

#architecture(degree)








