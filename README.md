# README
### California Elections 2020, Prop 17 DataLab Challenge
*This is the main directory for data and support files related to the Prop 17 DataLab Challenge.*

### Last Updated On: 
10/4/20

### Last Updated By: 
* Carlos, 
* Evan,
* Chenze


### Purpose and Motivation:
This repository contains example scripts for presenting prop 17 related illustrations. Replicating all statistical results require users to follow example readme instructions. 

**We hope to tackle these questions:**
* What is the population of parolees in CA? Who are they and what is the nature of their crimes? What are their demographics?
* Which communities by county would see the most impact by parolee voting? And what is the partisanship of these counties?
* What will the impact of parolees be on the vote if Proposition 17 passes? What is ratio between the number of parolees and the number of population in California? * How will the ratio change?
* How do people feel about Proposition 17? Do they support it or oppose it?
* Did parolee enfranchisement in other states have any impact on voter turnout in their elections?

**Description of approach:**
* Lots of Python (packages: Plotly, Numpy, Pandas, Mapbox, etc.)
* Lots of R (packages: ggplot2, dplyr, tidyr, readr, here)

### Directory Manifest

*  Folders:

	**Parent Folders**
	* /docs - contains image, html, and data directories.		
	* /examples - contain example scripts for data analysis
	
	**Sub Folders**
	* /docs/img - stores images
	* /docs/html - stores html instructions for website rendering
	* /docs/data - stores datasets used in our codes
	* /docs/data/Voter Turnout Raw Data - subfolder that stores .csv files used in voter_turnout.Rmd
	
	* /example/parolee_population_voting_registration_map - parolee population by county directory
	* /example/parolee_age_piechart - parolee age demographic pie chart directory
	* /example/parolee_agent_caseload_piechart - parolee agent caseload demographic pie chart directory
	* /example/parolee_ethnicity_piechart - parolee ethnicity demographic pie chart directory
	* /example/Voter_Turnout_in_RI_and_MD - subfolder that stores readme and voter_turnout.Rmd files

* Files:
	* /examples/parolee_population_voting_registration_map/ParolePartisanMap.py **(plot parole population and county partisanship on map)**
	* /examples/parolee_age_piechart/ParoleAge.py
	* /examples/parolee_agent_caseload_piechart/ParoleAgentCaseload.py
	* /examples/parolee_ethnicity_piechart/ParoleEthnicity.py
	* /example/Voter_Turnout_in_RI_and_MD/README.md - markdown file explaining how to load and run voter_turnout.Rmd
	* /example/Voter_Turnout_in_RI_and_MD/voter_turnout.Rmd - R markdown file containing code that was used to work with and visualize voter turnout data
	* /examples/ratio and absolute number of parolees in CA/ratio and absolute number of parolees in CA.py

### Personnel/Contributors
* Carlos Pereyra(lead) - twitter: AvocadoOnAToast
* Evan Roybal(lead) - email: earoybal@ucdavis.edu
* Chenze Li(lead)

### Project URLs - (for example: to data sources you used for the project)
* Rhode Island Voter Turnout Data: https://vote.sos.ri.gov/DataInformation/VoterTurnout 
* Maryland Voter Turnout Data: https://elections.maryland.gov/elections/2010/index.html 
* Rhode Island Parolee Enfranchisement Date: http://opendoorsri.org/righttovote 
* Maryland Parolee Enfranchisement Date: https://www.ncsl.org/research/elections-and-campaigns/felon-voting-rights.aspx 
*

### Project Repositories

* Main Repository: https://github.com/carlos-pereyra/Prop17DataLabChallenge
* Github-(web)page: https://github.com/carlos-pereyra/prop17.github.io



