# This is a python script to populate the course descriptions from Lou's list
# Usage:
# python lou_course_descriptions.py  > ../_data/courses.yml

current_semester = "Fall 2017"
lou_url = "https://rabi.phys.virginia.edu/mySIS/CC2/Mathematics.html"

from bs4 import BeautifulSoup
import urllib2
import csv

html = urllib2.urlopen(lou_url).read()
soup = BeautifulSoup(html, "lxml")
table = soup.select("table")[1]

data = []

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

print "# List of all courses, generated by the Python script scripts/lou_course_descriptions.py"
print "# all fields are self-explanatory; if the course is graduate this should be indicated"
print ""
print "# There is a list of courses that will not be shown, in file masked_courses.yml"
print ""
print "# There is a number of courses which must be added manually because they are not in Lou's list."
print "# They are in courses_added_manually.yml"
print ""
print "# Some courses are renamed, hardcoded in the script"
print ""

for i in range(1, len(data)):
    if i%2 :
        # renames and redo descriptions
        # if data[i][0].replace("MATH ", "", 1) == "4210":
        #     print "- name: \"", "Mathematics for Physics (3.00)", "\""
        # elif data[i][0].replace("MATH ", "", 1) == "1190":
        #     print "- name: \"", "A Survey of Calculus I with Algebra (4.00)", "\""
        # elif data[i][0].replace("MATH ", "", 1) == "1210":
        #     print "- name: \"", " A survey of Calculus I (3.00)", "\""
        # elif data[i][0].replace("MATH ", "", 1) == "1220":
        #     print "- name: \"", " A survey of Calculus II (3.00)", "\""
        # else :
        print "- name: \"", data[i][1], "\""
        print "  number:", data[i][0].replace("MATH ", "", 1)
        if int( data[i][0].replace("MATH ", "", 1) ) >= 5000 :
            print "  graduate: true"
    else :
        if data[i][0] == "Offered" + current_semester :
            # if data[i-1][0].replace("MATH ", "", 1) != "8700":
            #somehow 8700 is offered on Lou's list but not in reality
            print "  offered: " + current_semester
            # redo descriptions
            # if data[i-1][0].replace("MATH ", "", 1) == "4900":
            #     print "  descr: \"", "This course provides a framework for the completion of a Distinguished Major Thesis, a treatise containing an exposition of a chosen mathematical topic.  A faculty advisor guides a student through the beginning phases of the process of research and writing.  Prerequisite: Acceptance into the Distinguished Major Program.", "\""
            # elif data[i-1][0].replace("MATH ", "", 1) == "4901":
            #     print "  descr: \"", "This is the second semester of a two semester sequence for the purpose of the completion of a Distinguished Major Thesis. A faculty member guides the student through all phases of the process which culminates in an open presentation of the thesis to an audience including a faculty evaluation committee.  Prerequisite: MATH 4900.", "\""
            # else:
            print "  descr: \"", data[i][1].encode('utf-8').split("Course was offered", 1)[0], "\""
        else:
            # redo descriptions
            # if data[i-1][0].replace("MATH ", "", 1) == "4900":
            #     print "  descr: \"", "This course provides a framework for the completion of a Distinguished Major Thesis, a treatise containing an exposition of a chosen mathematical topic.  A faculty advisor guides a student through the beginning phases of the process of research and writing.  Prerequisite: Acceptance into the Distinguished Major Program.", "\""
            # elif data[i-1][0].replace("MATH ", "", 1) == "4901":
                # print "  descr: \"", "This is the second semester of a two semester sequence for the purpose of the completion of a Distinguished Major Thesis. A faculty member guides the student through all phases of the process which culminates in an open presentation of the thesis to an audience including a faculty evaluation committee.  Prerequisite: MATH 4900.", "\""
            # else:
            print "  descr: \"", data[i][0].encode('utf-8').split("Course was offered", 1)[0], "\""
        print ""
