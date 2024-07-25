# Replication Package for "Understanding Practitioners' Reasoning and Requirements for Efficient Tool Support in Technical Debt Management"

##### Authors: Joao Paulo Biazotto, Daniel Feitosa, Paris Avgeriou, and Elisa Yumi Nakagawa

## Description of this study:
__Context__: Maintaining software projects over the long term requires controlling the accumulation of technical debt (TD). However, the time and cost associated with technical debt management (TDM) are often high, hindering practitioners from performing TDM tasks. Using tools for TDM has the potential to reduce the effort involved. Despite this, the adoption of such tools remains low, indicating a need for more efficient tool support.

__Objective__: This study aims to understand practitioners' perspectives on tool support for TDM, specifically regarding their selection and use of these tools. Additionally, we seek to identify potential requirements that could be implemented into existing or new TDM tools.

__Methods__: We surveyed practitioners, and received 103 answers, from which 100 valid answers were analyzed using both thematic analysis and descriptive statistics.

__Results__: Practitioners' decision-making processes regarding adopting tools are primarily driven by ten main concerns identified from practitioners' responses (e.g., the load of information provided by tools). Additionally, we elicited 46 requirements and classified them into two main categories ("Information to be provided" and "Tool Usage").

__Conclusion__: Practitioners aim to maintain control over tool execution and outputs. Therefore, our study highlights the necessity of human-centered approaches for TDM automation, i.e., not only tools are essential, but the interaction between tools and practitioners is critical for a more efficient TDM.

## Structure of the replication package:

The replication package includes the datasets (for answers, codes, and indicators), the scripts for data analysis, and all the figures used in the manuscript.

```
├── data
│   ├── answers
│   |   └── 103 files with the questions and answers.
|   ├── answers-highlighted
|   |   └── 103 files with indicators highlighted in the the answers
|   ├── questionnaires
|   |   ├── 0-invitation-letters-email.pdf
|   |   ├── 1-invitation-letters-social-media.pdf
|   |   ├── s1.pdf
|   |   ├── s2.pdf
|   |   ├── s3.pdf
|   |   ├── s4.pdf
|   |   └── s5.pdf
|   ├── scenario-designs
|   |   ├── s1-c4.png
|   |   ├── s1-mockup.JPG
|   |   ├── s2-c4.png
|   |   ├── s2-mockup.png
|   |   ├── s3-c4.png
|   |   ├── s3-mockup.png
|   |   ├── s4-c4.png
|   |   ├── s4-mockup.JPG
|   |   ├── s5-c4.png
|   |   └── s5-mockup.png
|   ├── atlas-bundle.atlasti
|   ├── codebook.xlsx
|   ├── pre-coding.xlsx
|   ├── quotations.csv
|   ├── requirements.csv
|   ├── respondents.csv
|   ├── s1-answers.xlsx
|   ├── s2-answers.xlsx
|   ├── s3-answers.xlsx
|   ├── s4-answers.xlsx
|   └── s5-answers.xlsx
├── figures
│   ├── helpers.py 
|   └── file.py
├── scripts
│   ├── helpers.py
│   ├── highlight-codes.py
│   ├── rq0-demographics.ipynb
│   ├── rq1-concerns.ipynb
│   ├── rq2-requirements.ipynb
│   └── rqn-correlation-between-requirements-and-profiles.ipynb
├── docker-compose.yaml
├── Dockerfile
├── env.yaml
├── LICENSE.txt
└── README.md

```

## Description of each variable in ``codebook.xlsx``

| variable name                         | description                                                                                                                              |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| code                                  | code used to represent indicators                                                                                                        |

## Description of each variable in ``pre-coding.xlsx``

| variable name                         | description                                                                                                                              |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| scenario                              | the scenario from which the answer was collected                                                                                         |
| question                              | the question from a scenario                                                                                                             |
| sample                                | a sample of answers related to the questions                                                                                             |
| coder 1-3                             | the codes assigned by each coder to the answer                                                                                           |
| agreement                             | codes that were agreed by at least two coders                                                                                            |
| single incident                       | codes that were assigned by a single coder                                                                                               |


## Description of each variable in ``quotations.csv``

| variable name                         | description                                                                                                                              |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| id                                    | the identifier for a quotation, generated by Atlas.ti                                                                                    |
| document                              | the identifier of a response in the survey, indicated the scenario and the respondent (e.g., s1_r2)                                      |
| content                               | the text of a quoatation                                                                                                                 |
| codes                                 | a list of codes associated with the quotations (e.g., 1-generic td label is not useful for prioritization)                               |

## Description of each variable in ``requirements.csv``

| variable name                         | description                                                                                                                              |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| id                                    | the identifier of a requirement, based on the category of a requirement (e.g., INF01)                                                    |
| scenario                              | the scenario from which the requirements was extracted                                                                                   | 
| system                                | indicates the tool presented in the scenario from which the requirement was extracted (e.g., code review bot)                            |
| verb                                  | the verb that is used in the requirement, i.e., will                                                                                     |
| process                               | refers to the core of each requirement, i.e., the functionality that it specifies (e.g., present, enable, notify, etc.)                  |
| object                                | what and where a process will be executed (e.g., what information will be presented in a dashboard)                                      | 
| category                              | the category of a requirement (e.g., information to be provided)                                                                         |
| complete-requirement                  | the requirements phrased with all fields (e.g., process and object)                                                                      |
| code                                  | the code used to elicit the requirement                                                                                                  |


## Description of each variable in ``respondents.csv``

| variable name                         | description                                                                                                                              |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| id                                    | the identifier of a respondent, based on the scenario (e.g., s2_r18)                                                                     |
| scenario	                            | the scenario in answered by the respondent (e.g., s4)                                                                                    |
| education                             | the education level of a respondent (e.g., Master)                                                                                       |
| experience                            | the time of experience of a respondent (e.g., 1-5 years)                                                                                 |
| role                                  | the current role of a respondent (e.g., software developer)                                                                              |
| valid                                 | a boolean that indicate if the answer was considered for the data analysis                                                               |

## Description of each variable in ``sX-answers.xlsx`` (i.e., files that were uploaded to Atlas.ti)

| variable name                         | description                                                                                                                              |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| !id                                   | the identifier of a respondent, based on the scenario (e.g., s2_r18)                                                                     |
| :scenario	                            | the scenario in answered by the respondent (e.g., s4)                                                                                    |
| :education                            | the education level of a respondent (e.g., Master)                                                                                       |
| :experience                           | the time of experience of a respondent (e.g., 1-5 years)                                                                                 |
| :role                                 | the current role of a respondent (e.g., software developer)                                                                              |
| :usefulness                           | the preceived usefulness of a scenario                                                                                                   |
| sX_qX::XXXXX                          | variables with this format represents answers for a certain question (q) in a scenario (s), e.g., s1_q1::Would such a label be useful to prioritize the issues that should be addressed? Please justify your answer.                                                                                                                                      |

## Running the data analysis

1. Install Docker and docker-compose
2. Open a terminal (e.g., Windows Powershell) and navigate to the folder where replication package is saved
3. Run ``docker compose build``
4. After the environment is installed, run ``docker compose up``
5. Open a browser and access ``localhost:8888/lab``
7. Run the analysis contained in each of the scripts files, which are saved in the folder ``scripts``. Those scripts are organized by research question (e.g., ``rq2-requirements.ipynb``). 

## Paper

Latest version available on [arXiv]()

If you use this dataset to support your research and publish a paper, we encourage you to cite the following paper in your publication:

```
@article{Biazotto2024,
   title={Understanding Practitioners' Reasoning and Requirements for Efficient Tool Support in Technical Debt Management},
   ISSN={},
   url={},
   DOI={},
   author={Biazotto, João Paulo and Feitosa, Daniel and Avgeriou, Paris and Nakagawa, Elisa Yumi},
   year={2024},
   month=jul, 
   pages={} 
}
```

## Contact

- Please use the following email addresses if you have questions:
    - :email: <j.p.biazotto@rug.nl>
