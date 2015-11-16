---
title: "Introduction to R via data wrangling"
author: "Luke Johnston"
date: "July 23, 2015"
layout: page
visible: true
output: 
  html_document: 
    highlight: tango
    number_sections: yes
    theme: readable
    toc: yes
    
---

 - **Authors**: Luke W. Johnston
 - **Research field**: Nutritional Sciences (epidemiology)
 - **Lesson topic**: Intro to R and data wrangling
 - **Lesson content URL**: <https://github.com/UofTCoders/studyGroup/tree/gh-pages/lessons/introR>

This is a brief introduction to R, focussing on data wrangling using
`dplyr` and `tidyr` packages and generating reproducible documents
using `knitr` and `rmarkdown` packages.

You **don't need to read all of this** for the session.  It's more of
a **resource and reference**.

R is a statistical computing environment to analyze data and write
programs.  The strength of R comes from:

* It being developed by statisticians to do statistical analysis
* Its graphic capacities are top-quality
* It has excellent resources for creating reproducible documents.
* Its extensive and active community of users for doing statistical
  work:
    - R is the top tag in the
      [StackExchange CrossValidated site](stats.stackexchange.com/tags)
      for statistical questions
    - There are more than 6000 packages on
      [CRAN](https://cran.r-project.org/web/packages/) that stores all
      R packages (and installing these packages is straight-forward),
      from the obscure and cutting-edge statistical techniques to
      plotting to data wrangling.

I should mention a quick caveat.  While R is a general-purpose
programming language, it works a bit differently from other languages
such as Python (it was developed by statisticians after all!).  As
such, programming in R may not be as intuitive, powerful, or easy as
it may be in Python (though it can be done), especially if you come
from a computer science background.  If your work involves a lot of
programming, I would recommend Python as your main tool.  *However*,
it never hurts to learn more than one language, especially as R is
great for data analysis and plotting.

Ok, firstly, I've made this session with some assumptions (see the
[slides.html](./slides.html)) file.  Briefly I'm assuming you want to
use R for statistical analysis, plotting, and/or writing up reports.
I'm using R Markdown to show how to write up documents with R code and
since getting the data into an analyzable form is the hardest part of
an analysis, I'm using packages specific to that task.

While you can create functions in R, I won't be going over them.  A
great resource for R functions is
[this page from Hadley Wickham's 'Advanced R' book](http://adv-r.had.co.nz/Functions.html)

# R Markdown #

An `.Rmd` or [R Markdown](http://rmarkdown.rstudio.com/) file is a
[markdown](https://en.wikipedia.org/wiki/Markdown) file that contains
R code chunks that can be processed to output the results of the R
code into a generated `.md` file.  This is an incredible (and recent)
strength of using R, as this then allows you to create html, pdf, or
Word doc files from the `.md` file using the `rmarkdown` package
(which relies on [pandoc](pandoc.org)).

On the top of each `.Rmd` file is the
[YAML](https://en.wikipedia.org/wiki/YAML) front matter, which looks
like:

~~~
---
title: "Introduction to R"
author: "Luke Johnston"
date: "July 23, 2015"
output: 
  html_document: 
    highlight: tango
    number_sections: yes
    theme: readable
    toc: yes
    
---
~~~

Note the starting and ending `---` 'tags'.  This starts the YAML
block.

Markdown syntax for formatting is used in `.Rmd`.  Check out the
[R Markdown documentation](http://rmarkdown.rstudio.com/) for a quick
tutorial on the syntax.

# Import/export your data #

You'll need to import your data into R to analyze it.  I'm assuming
the data is already cleaned and ready for analysis.  If at any time
you need help with a command, use the `?` command, appended with the
command of interest (eg. `?write.csv`).  R comes with many internal
datasets that you can practice on.  The one I'm going to use is the
`swiss` dataset.


~~~r
write.csv(swiss, file = 'swiss.csv') # Export
ds <- read.csv('swiss.csv') # Import
~~~

# Viewing your data #

R has several very useful and easy tools for quickly viewing your
data.  `head()` shows the first few rows of a data.frame (a structure
for storing data that can include numbers, integers, factors, strings,
etc).  `names()` shows the column names.  `str()` shows the structure,
such as what the object is, and its contents.  `summary()` shows a
quick description of the summary statistics (means, median, frequency)
for each of your columns.  `class()` is like `str()` but only shows
the top level name of the object, so eg. while a data.frame contains
multiple columns that `str()` would show, `class()` would only show
that the object is a "data.frame".


~~~r
head(ds)
~~~

~~~
##              X Fertility Agriculture Examination Education Catholic
## 1   Courtelary      80.2        17.0          15        12     9.96
## 2     Delemont      83.1        45.1           6         9    84.84
## 3 Franches-Mnt      92.5        39.7           5         5    93.40
## 4      Moutier      85.8        36.5          12         7    33.77
## 5   Neuveville      76.9        43.5          17        15     5.16
## 6   Porrentruy      76.1        35.3           9         7    90.57
##   Infant.Mortality
## 1             22.2
## 2             22.2
## 3             20.2
## 4             20.3
## 5             20.6
## 6             26.6
~~~

~~~r
names(ds)
~~~

~~~
## [1] "X"                "Fertility"        "Agriculture"     
## [4] "Examination"      "Education"        "Catholic"        
## [7] "Infant.Mortality"
~~~

~~~r
str(ds)
~~~

~~~
## 'data.frame':	47 obs. of  7 variables:
##  $ X               : Factor w/ 47 levels "Aigle","Aubonne",..: 8 9 12 26 28 34 5 13 15 38 ...
##  $ Fertility       : num  80.2 83.1 92.5 85.8 76.9 76.1 83.8 92.4 82.4 82.9 ...
##  $ Agriculture     : num  17 45.1 39.7 36.5 43.5 35.3 70.2 67.8 53.3 45.2 ...
##  $ Examination     : int  15 6 5 12 17 9 16 14 12 16 ...
##  $ Education       : int  12 9 5 7 15 7 7 8 7 13 ...
##  $ Catholic        : num  9.96 84.84 93.4 33.77 5.16 ...
##  $ Infant.Mortality: num  22.2 22.2 20.2 20.3 20.6 26.6 23.6 24.9 21 24.4 ...
~~~

~~~r
summary(ds)
~~~

~~~
##         X        Fertility      Agriculture     Examination   
##  Aigle   : 1   Min.   :35.00   Min.   : 1.20   Min.   : 3.00  
##  Aubonne : 1   1st Qu.:64.70   1st Qu.:35.90   1st Qu.:12.00  
##  Avenches: 1   Median :70.40   Median :54.10   Median :16.00  
##  Boudry  : 1   Mean   :70.14   Mean   :50.66   Mean   :16.49  
##  Broye   : 1   3rd Qu.:78.45   3rd Qu.:67.65   3rd Qu.:22.00  
##  Conthey : 1   Max.   :92.50   Max.   :89.70   Max.   :37.00  
##  (Other) :41                                                  
##    Education        Catholic       Infant.Mortality
##  Min.   : 1.00   Min.   :  2.150   Min.   :10.80   
##  1st Qu.: 6.00   1st Qu.:  5.195   1st Qu.:18.15   
##  Median : 8.00   Median : 15.140   Median :20.00   
##  Mean   :10.98   Mean   : 41.144   Mean   :19.94   
##  3rd Qu.:12.00   3rd Qu.: 93.125   3rd Qu.:21.70   
##  Max.   :53.00   Max.   :100.000   Max.   :26.60   
## 
~~~

~~~r
class(ds)
~~~

~~~
## [1] "data.frame"
~~~

# Wrangling your data #

Data wrangling is a bit tedious in base R.  So I'm using two packages
designed to make this easier.  Load packages by using the `library()`
function.  `dplyr` comes with a `%>%` pipe function (via the
`magrittr` package), which works similar to how the Bash shell `|`
pipe works.  The command on the right-hand side takes the output from
the command on the left-hand side, just like how a plumbing pipe works
for water.

The four lines of code below using `tbl_df` are all the same.  The `.`
object represents the output from the pipe, but it doesn't have to be
used as using `%>%` implies also using `.`.  `tbl_df` makes the object
into a `tbl` class, making printing of the output nicer.


~~~r
library(dplyr)
~~~

~~~
## 
## Attaching package: 'dplyr'
## 
## The following objects are masked from 'package:stats':
## 
##     filter, lag
## 
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
~~~

~~~r
tbl_df(ds)
~~~

~~~
## Source: local data frame [47 x 7]
## 
##               X Fertility Agriculture Examination Education Catholic
## 1    Courtelary      80.2        17.0          15        12     9.96
## 2      Delemont      83.1        45.1           6         9    84.84
## 3  Franches-Mnt      92.5        39.7           5         5    93.40
## 4       Moutier      85.8        36.5          12         7    33.77
## 5    Neuveville      76.9        43.5          17        15     5.16
## 6    Porrentruy      76.1        35.3           9         7    90.57
## 7         Broye      83.8        70.2          16         7    92.85
## 8         Glane      92.4        67.8          14         8    97.16
## 9       Gruyere      82.4        53.3          12         7    97.67
## 10       Sarine      82.9        45.2          16        13    91.38
## ..          ...       ...         ...         ...       ...      ...
## Variables not shown: Infant.Mortality (dbl)
~~~

~~~r
ds %>% tbl_df()
~~~

~~~
## Source: local data frame [47 x 7]
## 
##               X Fertility Agriculture Examination Education Catholic
## 1    Courtelary      80.2        17.0          15        12     9.96
## 2      Delemont      83.1        45.1           6         9    84.84
## 3  Franches-Mnt      92.5        39.7           5         5    93.40
## 4       Moutier      85.8        36.5          12         7    33.77
## 5    Neuveville      76.9        43.5          17        15     5.16
## 6    Porrentruy      76.1        35.3           9         7    90.57
## 7         Broye      83.8        70.2          16         7    92.85
## 8         Glane      92.4        67.8          14         8    97.16
## 9       Gruyere      82.4        53.3          12         7    97.67
## 10       Sarine      82.9        45.2          16        13    91.38
## ..          ...       ...         ...         ...       ...      ...
## Variables not shown: Infant.Mortality (dbl)
~~~

~~~r
ds %>% tbl_df
~~~

~~~
## Source: local data frame [47 x 7]
## 
##               X Fertility Agriculture Examination Education Catholic
## 1    Courtelary      80.2        17.0          15        12     9.96
## 2      Delemont      83.1        45.1           6         9    84.84
## 3  Franches-Mnt      92.5        39.7           5         5    93.40
## 4       Moutier      85.8        36.5          12         7    33.77
## 5    Neuveville      76.9        43.5          17        15     5.16
## 6    Porrentruy      76.1        35.3           9         7    90.57
## 7         Broye      83.8        70.2          16         7    92.85
## 8         Glane      92.4        67.8          14         8    97.16
## 9       Gruyere      82.4        53.3          12         7    97.67
## 10       Sarine      82.9        45.2          16        13    91.38
## ..          ...       ...         ...         ...       ...      ...
## Variables not shown: Infant.Mortality (dbl)
~~~

~~~r
ds %>% tbl_df(.)
~~~

~~~
## Source: local data frame [47 x 7]
## 
##               X Fertility Agriculture Examination Education Catholic
## 1    Courtelary      80.2        17.0          15        12     9.96
## 2      Delemont      83.1        45.1           6         9    84.84
## 3  Franches-Mnt      92.5        39.7           5         5    93.40
## 4       Moutier      85.8        36.5          12         7    33.77
## 5    Neuveville      76.9        43.5          17        15     5.16
## 6    Porrentruy      76.1        35.3           9         7    90.57
## 7         Broye      83.8        70.2          16         7    92.85
## 8         Glane      92.4        67.8          14         8    97.16
## 9       Gruyere      82.4        53.3          12         7    97.67
## 10       Sarine      82.9        45.2          16        13    91.38
## ..          ...       ...         ...         ...       ...      ...
## Variables not shown: Infant.Mortality (dbl)
~~~

~~~r
## Let's put it into a new object
ds2 <- tbl_df(ds)
~~~

Again, these next lines are the same. `select` does as it says: select
the column from the dataset.


~~~r
select(ds2, Education, Catholic, Fertility)
~~~

~~~
## Source: local data frame [47 x 3]
## 
##    Education Catholic Fertility
## 1         12     9.96      80.2
## 2          9    84.84      83.1
## 3          5    93.40      92.5
## 4          7    33.77      85.8
## 5         15     5.16      76.9
## 6          7    90.57      76.1
## 7          7    92.85      83.8
## 8          8    97.16      92.4
## 9          7    97.67      82.4
## 10        13    91.38      82.9
## ..       ...      ...       ...
~~~

~~~r
ds2 %>% select(Education, Catholic, Fertility)
~~~

~~~
## Source: local data frame [47 x 3]
## 
##    Education Catholic Fertility
## 1         12     9.96      80.2
## 2          9    84.84      83.1
## 3          5    93.40      92.5
## 4          7    33.77      85.8
## 5         15     5.16      76.9
## 6          7    90.57      76.1
## 7          7    92.85      83.8
## 8          8    97.16      92.4
## 9          7    97.67      82.4
## 10        13    91.38      82.9
## ..       ...      ...       ...
~~~

~~~r
ds2 %>% select(., Education, Catholic, Fertility)
~~~

~~~
## Source: local data frame [47 x 3]
## 
##    Education Catholic Fertility
## 1         12     9.96      80.2
## 2          9    84.84      83.1
## 3          5    93.40      92.5
## 4          7    33.77      85.8
## 5         15     5.16      76.9
## 6          7    90.57      76.1
## 7          7    92.85      83.8
## 8          8    97.16      92.4
## 9          7    97.67      82.4
## 10        13    91.38      82.9
## ..       ...      ...       ...
~~~

You can rename columns either using `rename` or `select` (the new name
is on the left hand side, so `newname = oldname`).  However, with the
`select` command, only that column gets selected, while `rename`
selects all columns.


~~~r
ds2 %>% rename(County = X)
~~~

~~~
## Source: local data frame [47 x 7]
## 
##          County Fertility Agriculture Examination Education Catholic
## 1    Courtelary      80.2        17.0          15        12     9.96
## 2      Delemont      83.1        45.1           6         9    84.84
## 3  Franches-Mnt      92.5        39.7           5         5    93.40
## 4       Moutier      85.8        36.5          12         7    33.77
## 5    Neuveville      76.9        43.5          17        15     5.16
## 6    Porrentruy      76.1        35.3           9         7    90.57
## 7         Broye      83.8        70.2          16         7    92.85
## 8         Glane      92.4        67.8          14         8    97.16
## 9       Gruyere      82.4        53.3          12         7    97.67
## 10       Sarine      82.9        45.2          16        13    91.38
## ..          ...       ...         ...         ...       ...      ...
## Variables not shown: Infant.Mortality (dbl)
~~~

~~~r
ds2 %>% select(County = X)
~~~

~~~
## Source: local data frame [47 x 1]
## 
##          County
## 1    Courtelary
## 2      Delemont
## 3  Franches-Mnt
## 4       Moutier
## 5    Neuveville
## 6    Porrentruy
## 7         Broye
## 8         Glane
## 9       Gruyere
## 10       Sarine
## ..          ...
~~~

You can subset the dataset using `filter`.  Note the double equal sign
`==` for testing if 'Examination' is equal to 15.  A single `=` is
used for something else (assigning things to objects).


~~~r
filter(ds2, Catholic < 20, Examination == 15)
~~~

~~~
## Source: local data frame [3 x 7]
## 
##            X Fertility Agriculture Examination Education Catholic
## 1 Courtelary      80.2        17.0          15        12     9.96
## 2    Yverdon      65.4        49.5          15         8     6.10
## 3 Val de Ruz      77.6        37.6          15         7     4.97
## Variables not shown: Infant.Mortality (dbl)
~~~

~~~r
ds2 %>% filter(Catholic < 20, Examination == 15)
~~~

~~~
## Source: local data frame [3 x 7]
## 
##            X Fertility Agriculture Examination Education Catholic
## 1 Courtelary      80.2        17.0          15        12     9.96
## 2    Yverdon      65.4        49.5          15         8     6.10
## 3 Val de Ruz      77.6        37.6          15         7     4.97
## Variables not shown: Infant.Mortality (dbl)
~~~

~~~r
ds2 %>% filter(., Catholic < 20, Examination == 15)
~~~

~~~
## Source: local data frame [3 x 7]
## 
##            X Fertility Agriculture Examination Education Catholic
## 1 Courtelary      80.2        17.0          15        12     9.96
## 2    Yverdon      65.4        49.5          15         8     6.10
## 3 Val de Ruz      77.6        37.6          15         7     4.97
## Variables not shown: Infant.Mortality (dbl)
~~~

~~~r
## For string/factor variables
ds2 %>% filter(X == 'Aigle')
~~~

~~~
## Source: local data frame [1 x 7]
## 
##       X Fertility Agriculture Examination Education Catholic
## 1 Aigle      64.1          62          21        12     8.52
## Variables not shown: Infant.Mortality (dbl)
~~~

We can start chaining these commands together using the `%>%` command.
There is no limit to how long a chain can be.  `arrange`
sorts/orders/re-arranges the column Education in ascending
order. `mutate` creates a new column.


~~~r
ds2 %>%
  filter(Catholic > 20) %>%
  select(Education, Fertility) 
~~~

~~~
## Source: local data frame [21 x 2]
## 
##    Education Fertility
## 1          9      83.1
## 2          5      92.5
## 3          7      85.8
## 4          7      76.1
## 5          7      83.8
## 6          8      92.4
## 7          7      82.4
## 8         13      82.9
## 9          6      87.1
## 10         2      68.3
## ..       ...       ...
~~~

~~~r
ds2 %>%
  filter(Catholic > 20) %>%
  select(County = X, Education, Fertility, Agriculture) %>%
  arrange(Education) %>%
  mutate(infertile = ifelse(Fertility < 50, 'yes', 'no'),
         testing = 'Yes' ## Create a testing column to show how mutate works.
         )
~~~

~~~
## Source: local data frame [21 x 6]
## 
##          County Education Fertility Agriculture infertile testing
## 1     Echallens         2      68.3        72.6        no     Yes
## 2       Conthey         2      75.5        85.9        no     Yes
## 3        Herens         2      77.3        89.7        no     Yes
## 4       Monthey         3      79.4        64.9        no     Yes
## 5        Sierre         3      92.2        84.6        no     Yes
## 6  Franches-Mnt         5      92.5        39.7        no     Yes
## 7       Veveyse         6      87.1        64.5        no     Yes
## 8     Entremont         6      69.3        84.9        no     Yes
## 9      Martigwy         6      70.5        78.2        no     Yes
## 10      Moutier         7      85.8        36.5        no     Yes
## ..          ...       ...       ...         ...       ...     ...
~~~

To get the data into a nicer and more analyable format, you can use
the `tidyr` package.  See what `gather` does in the code below.  Then
see what `spread` does.  Note that you can remove a column by having a
minus `-` sign in front of a variable when you use `select`.


~~~r
library(tidyr)
## Compare this:
ds2 %>%
  select(-Infant.Mortality) %>%
  rename(County = X)
~~~

~~~
## Source: local data frame [47 x 6]
## 
##          County Fertility Agriculture Examination Education Catholic
## 1    Courtelary      80.2        17.0          15        12     9.96
## 2      Delemont      83.1        45.1           6         9    84.84
## 3  Franches-Mnt      92.5        39.7           5         5    93.40
## 4       Moutier      85.8        36.5          12         7    33.77
## 5    Neuveville      76.9        43.5          17        15     5.16
## 6    Porrentruy      76.1        35.3           9         7    90.57
## 7         Broye      83.8        70.2          16         7    92.85
## 8         Glane      92.4        67.8          14         8    97.16
## 9       Gruyere      82.4        53.3          12         7    97.67
## 10       Sarine      82.9        45.2          16        13    91.38
## ..          ...       ...         ...         ...       ...      ...
~~~

~~~r
## With this:
ds2 %>%
  select(-Infant.Mortality) %>%
  rename(County = X) %>%
  gather(Measure, Value, -County)
~~~

~~~
## Source: local data frame [235 x 3]
## 
##          County   Measure Value
## 1    Courtelary Fertility  80.2
## 2      Delemont Fertility  83.1
## 3  Franches-Mnt Fertility  92.5
## 4       Moutier Fertility  85.8
## 5    Neuveville Fertility  76.9
## 6    Porrentruy Fertility  76.1
## 7         Broye Fertility  83.8
## 8         Glane Fertility  92.4
## 9       Gruyere Fertility  82.4
## 10       Sarine Fertility  82.9
## ..          ...       ...   ...
~~~

~~~r
## And back again:
ds2 %>%
  select(-Infant.Mortality) %>%
  rename(County = X) %>%
  gather(Measure, Value, -County) %>%
  spread(Measure, Value)
~~~

~~~
## Source: local data frame [47 x 6]
## 
##        County Fertility Agriculture Examination Education Catholic
## 1       Aigle      64.1        62.0          21        12     8.52
## 2     Aubonne      66.9        67.5          14         7     2.27
## 3    Avenches      68.9        60.7          19        12     4.43
## 4      Boudry      70.4        38.4          26        12     5.62
## 5       Broye      83.8        70.2          16         7    92.85
## 6     Conthey      75.5        85.9           3         2    99.71
## 7    Cossonay      61.7        69.3          22         5     2.82
## 8  Courtelary      80.2        17.0          15        12     9.96
## 9    Delemont      83.1        45.1           6         9    84.84
## 10  Echallens      68.3        72.6          18         2    24.20
## ..        ...       ...         ...         ...       ...      ...
~~~

Combined with `dplyr`'s `group_by` and `summarise` you can quickly
summarise data or do further, more complicated analyses. `group_by`
makes it so further analyses or operations work on the groups.
`summarise` transforms the data to only contain the new variable(s)
created, in this case the mean.


~~~r
ds2 %>%
  select(-X) %>%
  gather(Measure, Value) %>%
  group_by(Measure) %>%
  summarise(mean = mean(Value))
~~~

~~~
## Source: local data frame [6 x 2]
## 
##            Measure     mean
## 1        Fertility 70.14255
## 2      Agriculture 50.65957
## 3      Examination 16.48936
## 4        Education 10.97872
## 5         Catholic 41.14383
## 6 Infant.Mortality 19.94255
~~~

You can extend this to be created as a table in the generated `.md` or
`.html` file using the `kable` command (short for 'knitr table').


~~~r
library(knitr)
ds2 %>%
  select(-X) %>%
  gather(Measure, Value) %>%
  group_by(Measure) %>%
  summarise(mean = mean(Value)) %>%
  kable()
~~~



|Measure          |     mean|
|:----------------|--------:|
|Fertility        | 70.14255|
|Agriculture      | 50.65957|
|Examination      | 16.48936|
|Education        | 10.97872|
|Catholic         | 41.14383|
|Infant.Mortality | 19.94255|

# Generate this document #

Check out the documentation on
[`knitr`](http://yihui.name/knitr/options/) or
[R Markdown](http://rmarkdown.rstudio.com/authoring_rcodechunks.html)
for R code chunk options.  If you look at the raw `.Rmd` file for this
[document](./main.Rmd), you can see that the below code chunk uses
`eval = FALSE`, which tells knitr to not run this code chunk.

These two commands generate either a html or a md file.


~~~r
## into html
library(rmarkdown)
render('lesson.Rmd') ## or can use rmarkdown::render('main.Rmd')

## into md
library(knitr)
knit('lesson.Rmd') ## or can use knitr::knit('main.Rmd')
~~~

# Challenge: Try this out for yourself! #

Make a table with the means of Agriculture, Examination, Education,
and Infant.Mortality for each category of Fertility (hint: convert it
into a factor by values >50 vs <50), when Catholic is less than 60
(hint, use `dplyr` commands + `gather`).  Have the Fertility groups as
two columns in the new table (hint, use `spread` + `kable`).
