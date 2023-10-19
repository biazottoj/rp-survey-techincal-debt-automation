# Replication Package for "A survey on requirements for technical debt management automation"

##### Authors: Joao Paulo Biazotto, Daniel Feitosa, Paris Avgeriou, and Elisa Yumi Nakagawa

## Description of this study:

__Context__: Technical Debt (TD) refers to non-optimal decisions made in software projects
that may lead to short-term benefits, but potentially harm the system’s maintenance
and evolution in the long-term. Technical debt management (TDM) refers to a set of
activities that are performed to handle TD, e.g., identification, documentation, and
repayment of TD. These activities typically entail tasks such as code and architectural
analysis, which can be time-consuming if done manually. To address this, substantial
research work has focused on automating TDM tasks, such as automatic identification
of code smells and automatic refactoring of source code.

# __Problem and Motivation__: 

# __Objective__: 

# __Methods__: 

# __Results__: 

# __Conclusion__: 

## Structure of the replication package:

The replication package includes the datasets, the scripts for data analysis, and all the figures used in the manuscript.

```
├── data
│   ├── file1.csv
|   └── file.csv
├── scripts
│   ├── helpers.py 
|   └── file.py
├── figures
│   ├── figure1.pdf
│   └── figure2.pdf
├── LICENSE.txt
├── README.md
├── docker-compose.yaml
├── Dockerfile
└── env.yaml

```

## Description of each variable in ``selected-artifacts.csv``

| variable name                         | description                                                                                                                              |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| id                                    | ID of the artifact                                                                                                                       |

## Running the data analysis

1. Install Docker and docker-compose
2. Open a terminal (e.g., Windows Powershell) and navigate to the folder where replication package is saved
3. Run ``docker compose build``
4. After the environment is installed, run ``docker compose up``
5. Open a browser and access ``localhost:8888/lab``
6. Run the cells in the file ``examples.ipynb``, to generate the file ``example.json``.
7. After the exectution, it is possible to run the analysis contained in each of the scripts files, which are saved in the folder ``scripts``. Those scripts are organized by research question (e.g., ``rq2-examples.ipynb``). 


## Contact

- Please use the following email addresses if you have questions:
    - :email: <j.p.biazotto@rug.nl>
