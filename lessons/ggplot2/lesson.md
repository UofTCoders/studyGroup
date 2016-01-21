---
layout: page
title: ggplot2
visible: true
---

### What is ggplot2? ###

ggplot2 is meant to be an implementation of the Grammar of Graphics, hence gg-plot. The basic notion is that there is a grammar to the composition of graphical components in statistical graphics, and by direcly controlling that grammar, you can generate a large set of carefully constructed graphics tailored to your particular needs. Each component is added to the plot as a layer. 

### Components of a ggplot2 plot ###

Plots convey information through various aspects of their aesthetics. Some aesthetics that plots use are:

* x position
* y position
* size of elements
* shape of elements
* color of elements

The elements in a plot are geometric shapes, like

* points
* lines
* line segments
* bars
* text

Some of these geometries have their own particular aesthetics. For instance:

**points**

  * point shape
  * point size
  
**lines**

  * line type
  * line weight
  
**bars**

  * y minimum
  * y maximum
  * fill color
  * outline color
  
**text**

  * label value

## R code ##

~~~
library(ggplot2)

summary(mpg)

g <- ggplot(mpg, aes(displ, hwy))

g + geom_point()

g + geom_point() + geom_smooth(method="lm")

g + geom_point() + geom_smooth(method="lm") + facet_grid(drv~.)

g + geom_point(color="steelblue", size=4, alpha=1/2)

g + geom_point(aes(color=drv)) + 
labs(title="Fuel ecomony...", 
     x= "Engine displ", y="highway milage") + theme_bw(base_family = "Times")

ggplot(mpg, aes(displ)) + geom_histogram(aes(color=drv)) + theme_bw()

library(reshape2)
library(plyr)
library(dplyr)

mt <- select(mtcars, c(1,3,4,5,6,7))
mt2 <- cor(mt)
mt3 <- melt(mt2)
ggplot(mt3, aes(x=Var1, y=Var2, fill=value)) + geom_tile()

mtcars %>%
  select(c(1,3,4,5,6,7)) %>%
  cor() %>%
  melt() %>%
  ggplot(aes(x=Var1, y=Var2, color=value)) + geom_point()
  
~~~
