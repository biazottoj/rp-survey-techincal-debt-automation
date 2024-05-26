import csv

def load_csv_dataset(filename, dialect='excel', delimiter = ','):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, dialect=dialect, delimiter=delimiter)
        return [row for row in reader]

    
def save_csv_dataset(filename, data, header=None):
    header = header if header else list(data[0].keys())
    with open(filename, 'w', encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=header)
        writer.writeheader()
        for d in data:
            writer.writerow(d)

def extract_respondents_id(code: str):
    """
    A function to link the practitioners to the requirements considering the indicators in the code that was used to elicitate de requirement
        
        Parameters
        ----------
        code: str
            the code (generated in open coding) that represents a requirement

    """

    # The symbol "â—‹" indicates the begining of a code, e.g., â—‹ 5-the bot is already providing too much info
    # The symbol "¶" indicates a quotation, e.g., 
    # 5:5 ¶ 6, in s1_r25 
    # Keeping track of tasks and specially technical debts can be hard sometimes,
    # In a quoatation, it is possible to find the respondent id, e.g., s1_r25, which is locate in the end of the line

    respondents = []
    with open("../data/codes-report-exported-from-atlasti.txt") as f:
        all_lines = f.readlines()
        
        # checks if the line contains a character that indicates code description
        # "i" represents the line index, while "l" is the line content
        lines_with_code_description = [line_index for line_index, line_content in enumerate(all_lines) if "â—‹" in line_content]

        # iterates over the line indexes
        for current_index_of_code_description_array, current_number_of_line_with_code_description in enumerate(lines_with_code_description):
            if code in all_lines[current_number_of_line_with_code_description]:

                if current_index_of_code_description_array == len(lines_with_code_description) - 1: # true if the script is checking the last index in the lines_with_code_description array
                    next_line_with_code_description = len(all_lines)
                else:
                    next_line_with_code_description = lines_with_code_description[current_index_of_code_description_array + 1]
                
                # sets the line_counter on the first line after the code descriptio
                line_index_counter = current_number_of_line_with_code_description + 1

                # check lines between one code description and the next one
                while line_index_counter < next_line_with_code_description:

                    # checks if the line contains a character that indicates quotation
                    if "¶" in all_lines[line_index_counter]:
                        # splits the line in each space, e.g., ['', '', '72:1', 'Â¶', '2,', 'in', 's4_r5\n']
                        # takes the last element of the array, which represents the respondent id
                        # removes the line break character character ("\n")
                        respondents.append(all_lines[line_index_counter].split(" ")[-1].replace("\n", ""))

                    # sets the line counter on the next line
                    line_index_counter += 1
                return respondents

requirements_dataset = load_csv_dataset("../data/requirements.csv")
respondents_dataset = load_csv_dataset("../data/respondents.csv", delimiter=';')
dataset = []

for r in requirements_dataset:
    respondents_per_code = list(set(extract_respondents_id(r['codes'])))
    
    for respondent in respondents_per_code:
        dataset.append({'scenario': r['scenario'], 
                        'category': r['category'], 
                        'complete-requirement': r['complete-requirement'], 
                        'code': r['codes'],
                        'respondent-id':respondent,
                        'respondent-role': [r1['role'] for r1 in respondents_dataset if r1['id'] == respondent][0],
                        'respondent-experience':[r1['experience'] for r1 in respondents_dataset if r1['id'] == respondent][0],
                        'respondent-education':[r1['education'] for r1 in respondents_dataset if r1['id'] == respondent][0]})
        
save_csv_dataset("../data/requirements-and-respondents.csv", dataset)

