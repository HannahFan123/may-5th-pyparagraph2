import os
import csv

#filepath = os.path.join("Resources", "employees.csv")
filepath = "employee_data1.csv"
filename = "new_employee_data.csv"
#filepath2 = "C:\\Users\\Hannah\\Desktop\\UT Data 2018 HW\May 5 Python\\employee_data2.csv"
#filename2 =  "employee_data2"

def reformat_date(yyyymmdd):
    date_parts = yyyymmdd.split("-")
    yyyy = date_parts[0]
    mm = date_parts[1]
    dd = date_parts[2]
    return mm + "/" + dd + "/" + yyyy 

def mask_ssn(social):
    return "***-**-" + social[-4:]

def get_abbreviation(full_state):
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
    return us_state_abbrev[full_state]

new_employee_data = []


with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row)
        full_name = row["Name"]
        name_parts = full_name.split(" ")
        first_name = name_parts[0]
        last_name = name_parts[1]
        new_employee_data.append({
            "Emp ID": row["Emp ID"],
            "DOB": reformat_date(row["DOB"]),
            "First Name": first_name,
            "Last Name": last_name,
            "SSN": mask_ssn(row["SSN"]),
            "State": get_abbreviation(row["State"])
        })
        print(new_employee_data)

# Grab the filename from the original path


# Write updated data to csv file
csvpath = os.path.join("output", filename)
with open(csvpath, "w") as csvfile:
    fieldnames = ["Emp ID", "First Name", "Last Name", "SSN", "DOB", "State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_data)
