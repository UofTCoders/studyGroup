#BASE PLOTTING FUNCTIONS
data()
plot(cars)
hist(cars$speed)

#We'll investigate the dataset we're going to use to make some graphs....
library(ggplot2)
str(diamonds)

#Our first graph?
ggplot(diamonds, aes(x=cut, y=carat))

#We've defined the structure of our graph, but we need to add a "layer" to it in order to define what type of graph it is. 
#Let's make a scatterplot:
ggplot(diamonds, aes(x=carat, y=price)) + 
  geom_point()

#You can also save the structure of the graph to a variable and then add layers and other attributes to it. Let's do that:
g <- ggplot(diamonds, aes(x=carat, y=price))
g + geom_point()

#We can add other "layers" of graphs to our first graph. Let's add a trend line to our scatterplot:
g + geom_point() + geom_smooth() 

#We can also "facet" our graphs, which means dividing a plot into subplots based on the values of one or more discrete variables.
g + geom_point() + geom_smooth() + facet_grid(cut~.)

#Let's say we don't want to facet, but we want to colour the dots depending on the cut of the diamonds:
ggplot(diamonds, aes(x=carat, y=price, color=cut)) + geom_point()

#We can also change some aesthetic features of the graph. 
#Let's get rid of the color aspect of our structure and change the colour and size of the points:
ggplot(diamonds, aes(x=carat, y=price)) + geom_point(color="steelblue", size=4)

#Let's look at how to change the theme and labels:
g + geom_point() +
  ylab("Diamond Price") +
  xlab("Carat") +
  ggtitle("Diamond Price by Weight") +
  theme_bw()

#What about a bar plot? Let's find out how many diamonds of each cut are in the dataset.
ggplot(diamonds, aes(cut)) + geom_bar()

#What about making interactive graphs in R?
#There is a package called plotly that lets us make our ggplot2 graphs interactive:
library(plotly)
g <- ggplot(diamonds, aes(cut)) + geom_bar()
p=ggplotly(g)
p

#Finally, here is qplot, a way of making super quick scatterplots in R.
qplot(carat, price, data = diamonds)
