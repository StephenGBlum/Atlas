
import pprint
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

degree = input('Enter a keyword of a program you would like to explore: ')
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

def get_program_level(program_index):
    data = requests.get(program_index)
    html = BeautifulSoup(data.text, 'html.parser')

    tables = html.find_all('table')
    table = html.find('table', class_='sorttable')

    # columns = row.find_all('td')

    rows = []
    columns = []
    levels = []
    for row in table.find_all('tr'):
        column = row.find_all('td')[3].text
        levels.append(column)
    return (levels)
#print(len(get_program_names(program_index)))
#print(len(get_program_links(program_index)))
#print(len(get_program_type(program_index)))
all_courses = np.stack((get_program_names(program_index),get_program_type(program_index),get_program_level(program_index),get_program_links(program_index)),axis=1)
#Name is index 0, Undergrad/grad is index 1, major/minor is index 2, link is index 3
def search_list(degree, all_courses):
    search_results =[]
    search_count =0
    for i in range (len(all_courses)):
        if degree in all_courses[i][0]:
            search_results.append(all_courses[i])
            search_count += 1


    return search_results


def filter_search(search_list, search_term):


    filtered_results = []

    search_count = 0
    if search_term == 'Undergraduate':
        for i in range(len(search_list)):
            if 'Undergraduate' in search_list[i][1]:
                filtered_results.append(search_list[i])
                search_count += 1

        return filtered_results

    elif search_term == 'Graduate':
        for i in range(len(search_list)):
            if 'Graduate' in search_list[i][1]:
                filtered_results.append(search_list[i])
                search_count += 1

        return filtered_results

    elif search_term == 'Major':
        for i in range(len(search_list)):
            if 'Major' in search_list[i][2]:
                filtered_results.append(search_list[i])
                search_count += 1

        return filtered_results

    elif search_term == 'Minor':
        for i in range(len(search_list)):
            if 'Minor' in search_list[i][2]:
                filtered_results.append(search_list[i])
                search_count += 1

        return filtered_results

    elif search_term == 'Certificate':
        for i in range (len(search_list)):
            if 'Certificate' in search_list[i][2]:
                filtered_results.append(search_list[i])
                search_count += 1

        return filtered_results




print(search_list(degree,all_courses))
print(len(search_list(degree,all_courses)),' Courses Found')
search_term = ''
filter_bool = input('Would you like to filter these search results?\n')

if filter_bool == 'Yes':
    filter_options = int(input('Filter search result: '
                               '\n1. By program level (graduate/undergraduate)'
                               '\n2. By program type (Major/Minor/Certificate)\n'))

    if filter_options == 1:
        search_term = input('Would you like to search for Undergraduate or Graduate programs?\n')
    elif filter_options == 2:
        search_term = input('Would you like to search for a Major, Minor, or Certificate?\n')

    print(filter_search(search_list(degree,all_courses),search_term))
    print(len(filter_search(search_list(degree, all_courses),search_term)),' Courses Found')
else:
    print('')



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

 #Works

carriculum_link = "https://bulletin.miami.edu" #add link from array + #curriculumtext
def carriculum_parser(carriculum_link, degree_link, plan_of_study_ext = "#planofstudytext"):
    course_data_link = carriculum_link+degree_link+plan_of_study_ext
    data = requests.get(course_data_link)

    html = BeautifulSoup(data.text, 'html.parser')
    # Find data (table containing required text)
    tables = html.find_all('table')
    table = html.find('table', class_='sc_plangrid')
    #print(table)
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
    #print(rows)
    for i in range(0,len(rows)):
        if 'Hours' in rows[i]:
            positions.append(i)

    new_list=[]
    temp =[]
    #print(positions)
    for i in range(len(positions)-1):
        temp = rows[positions[i]:positions[i+1]]
        #print(temp)
        new_list.append(temp)
        #temp.clear()

    return new_list





        #print(code)
    #print(titles)

        #print(even)

select_program = int(input('Enter the index of the selected program'))
print(carriculum_parser(carriculum_link, filter_search(search_list(degree,all_courses),search_term)[select_program][3], '#planofstudytext'))
#print('Number of Majors in Degree: ',len(architecture(degree)))

#architecture(degree)








