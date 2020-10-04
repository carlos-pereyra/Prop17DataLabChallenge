## To run the code the programming language R must be installed, it is also recommended that you download the IDE R Studio as it's easier to use
### In an R script use the install.packages() function included in base R to install the necessary packages
```{r}
install.packages('ggplot2')
install.packages('dplyr')
install.packages('tidyr')
install.packages('readr')
install.packages('here')
```
### The packages can also be installed with tidyverse but this downloads other unnecessary packages
```{r}
install.packages('tidyverse')
install.packages('here')
```
### Once packages are installed import the .csv files located in the Voter Turnout Folder in data into the folder containing the R script
### After .csv files have been imported, import the R markdown file voter_turnout.Rmd, open it in R, and run all code
