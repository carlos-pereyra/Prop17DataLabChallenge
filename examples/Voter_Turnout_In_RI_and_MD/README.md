### To run the code the programming language R must be installed, it is also recommended that you download the IDE R Studio as it's easier to use
### In an R script use the install.packages() function included in base R to install the necessary packages
```{r}
install.packages('ggplot2')
install.packages('dplyr')
install.packages('tidyr')
install.packages('readr')
install.packages('here')
```
### The packages can also be installed with tidyverse but this would download unnecessary packages
```{r}
install.packages('tidyverse')
install.packages('here')
```
### Once packages are installed import the "Voter Turnout Raw Data" subfolder in the "Data" folder. Note: the "Voter Turnout Raw Data" folder must be located within another folder titled "Voter Turnout" for the .csv files to be located and read by the code
### After .csv files have been imported, import the R markdown file voter_turnout.Rmd into the "Voter Turnout" Folder, open it in R or R Studio and run all code
