---
layout: page
title: 'Making interactive plots using Shiny in R'
visible: true
---

#R Shiny Tutorial

 - **Authors**: Lanna Jin
 - **Research field**: Ecology & Evolutionary Biology
 - **Lesson topic**: Interactive Visualizations with the Shiny library in R
 - **Lesson content URL**: <https://github.com/UofTCoders/studyGroup/tree/gh-pages/lessons/Shiny>

<h1>Introduction</h1>
Introduction to Data Set

<h1>Module 1</h1>
First familiarize ourselves with the basic layout of the Shiny user interface. It is important to note, that while we set-up interactivity, user interactivity is not included within this first shiny App activity.

<h2>ui.R</h2>
1. After initially loading the shiny library and relevant data, the overall UI is wrapped within the `shinyUI` function
2. Next, we define a page that is fluid (`fluidPage`)--that can change based on the user's input. For this page, we name it with a title (`titlePanel`)
3. The set-up of the page is one based on a template (`sidebarLayout`): a sidebar (`sidebarPanel`; on the left, from which the user will make their selections); and a main Panel (`mainPanel`) which changes based on the user's input in the left side-bar panel
4. The `mainPanel` will display the PCA of the metrics, which is identified as `pcaplot`. This object is created/assigned within the `server.R` script.

<h3>TASK:</h3>
 1. Change the `title` to something more relevant, e.g., `PCA of Metrics`

<h2>server.R</h2>
1. The shiny library and relevant data is first loaded
2. We define the server for the Shiny app as something with both objects that are input (from the `ui.R`) and output (from the `server.R`)
3. We create a reactive Shiny plot that is output from `server.R` to `ui.R` with the function `renderPlot`. `renderPlot` is an reactive function that can take input data from the `ui.R` script and feed it into the `server.R` script. It then actively updates the information within its function. We name the object that has the `renderPlot` function to plot the PCAs as `pcaplot`. `pcaplot` is then output and displayed through the `ui.R` within the `plotOutput` function.

<h3>TASKS:</h3>
1. Change the plot's x- and y-axis label names to `PC1` and `PC2`.
2. Instead of plotting points, plot the metrics as text points instead

<h4>HINTS:</h4>
1. use `xlab` and `ylab` within the function `plot` to change the axes labels
2. For the function `plot`, enter the parameter `type="n"` to create a blank plot that maintains the axes labels and plotting parameters:

   ~~~
   plot(PC2 ~ PC1, data=foo, type="n", xlab="PC1", ylab="PC2")
   ~~~

   Next use the function `text` to plot the text values. Use `foo$metric` as the label values

   ~~~
   text(PC2 ~ PC1, data=foo, labels=foo$metric)
   ~~~

<h1>Module 2</h1>
Add interactivity to the plot. In the `sidebarPanel` in the `ui.R`, we add a `sliderInput` widget, which allows the user to (a) select a value from the ui interface, which is then (b) fed to the server script. The server script then (c) readjusts the plot with the new input value and (d) feeds the output plot to the ui interface.

<h2>ui.R</h2>
<h3>TASK:</h3>
1. Change the size of label of the cexSlider with the wrapper, `h4`
2. Adjust the maximum `cexSlider` `cex` size to 5
3. The PCA plot (`pcaplot`) currently is showing all the values, disregarding the different variables (Var: colless, numsp, Spatial). We however would like to show the PCA plot for each variable scenario.


To do so:

1. Create a drop-down list of the variables with the function `selectInput` within the `sidebarPanel` function.

2. Assign the `selectInput` object as `var`, and the `label` as `h3('Variable')`

3. for the choices, use:

   ~~~
   choices = c(
               "Colless" = "colless",
               "Species Pool Size" = "numsp",
               "Spatially Contiguous" = "spatial"
           )
   ~~~

4. Link `var` as `input$var` in `server.r` (refer to `server.r`)

<h4>HINTS:</h4>

1. `sliderInput(..., label = h4("Adjust cex"))`
2. `sliderInput(..., max = 5)`
3. ~~~
   selectInput(inputId='var', label = h3('Variable'),
               choices = c(
               "Colless" = "colless",
               "Species Pool Size" = "numsp",
               "Spatially Contiguous" = "spatial"
              )
   )
   ~~~

<h2>server.R</h2>
<h3>TASKS:</h3>
1. The PCA plot (`pcaplot`) currently is showing all the values, disregarding the different variables (Var: colless, lambdaE, lambdaR, Landscape, Numsp, Repulsion, Spatial). We however would like to show the PCA plot for each variable scenario.
   To do so:

   1. Complete Task 3 in `ui.r` to create the `selectInput` drop-down menu, which we will call `var`
   2. subset the `foo` dataframe for only instances when `foo$Var==input$var`

<h4>HINTS:</h4>
1. ~~~
   output$pcaplot <- renderPlot({
       #Subset for input$var and assign this subset to new object, "fbar"
       fbar<-droplevels(foo[which(foo$Var==input$var),])
   #Change "foo" to "fbar" for the plot and text
   plot(PC2 ~ PC1, data=fbar, type="n", xlab="PC1", ylab="PC2")
   text(PC2 ~ PC1, data=fbar, labels=fbar$metric, cex=input$cexSlider)
   })
   ~~~

<h1>Module 3</h1>
We've now added interactivity to the plot. The user can (a) specify the Variable (`Var`) scenario they wish to plot the PCA of, and (b) adjust the text's `cex` values. The `server.r` script now includes code to add colors that correspond to each selected variable's parameter values (`param`), as well as a legend.

<h2>ui.R</h2>
<h3>TASK:</h3>
1. Depending on the variable that people choose (`input$var`), we now want to display the chosen variable's parameter (`foo$param`) values as a check box group. Even though logically we would begin with the `checkboxGroupInput` function on the `ui.R` script to display check box options, first remember what the capabilities of the user side (`ui.R`) are. `ui.R` cannot evaluate/process information, but only displays output values calculated on the server side (`server.R`). In other words, the `ui.R` only takes in the values a user specifies and then sends this information to be evaluated/processed on the server side.
   So to create a `checkboxgroup` of `param` values that will change based on what the user selects for a variable (`input$var`), our first step is to evaluate what the user selects as a variable. This evaluation can only take place on the server side. We therefore need to create an object on the server side (`output$paramchkbxgrp`) that will evaluate the user's Variable selection (`input$var`), which will then decide which check box options to display. This decision of what to display is then fed back to the `ui.R` with the object `uiOutput`.

   1. With the function `uiOutput`, display the computation result of the output function `paramchkbxgrp`

<h4>HINTS:</h4>

1. Place the following snippet of code in `ui.R` within the `sidebarPanel`, after the `selectInput` for the variables:

   ~~~
   uiOutput(outputId="paramchkbxgrp")
   ~~~

<h2>server.R</h2>
<h3>TASKS:</h3>
1. Depending on the variable that people choose (`input$var`), we now want to display the chosen variable's parameter (`param`) values as a check box group. Even though logically we would begin with the `checkboxGroupInput` function on the `ui.R` script to display check box options, first remember what the capabilities of the user side (`ui.R`) are. `ui.R` cannot evaluate/process information, but only displays output values calculated on the server side (`server.R`). In other words, the `ui.R` only takes in the values a user specifies and then sends this information to be evaluated/processed on the server side.

   So to create a `checkboxgroup` of `param` values that will change based on what the user selects for a variable (`input$var`), our first step is to evaluate what the user selects as a variable. This evaluation can only take place on the server side. We therefore need to create an object on the server side (`output$paramchkbxgrp`) that will evaluate the user's Variable selection (`input$var`), which will then decide which check box options to display.  This decision of what to display is then fed back to the `ui.R` with the object `uiOutput`.

   1. Depending on what Variable is selected by the user (`input$var`), generate a different set of check box options to display (with the function `checkboxGroupInput`). For instance, if `colless` is selected as the variable, display the parameters values that correspond to `colless`, e.g., `loIc`, `midIc` and `hiIc`. This `switch` function takes the given value (`input$var`) and then evaluates it. When `input$var=="colless"`, then it evaluates the `checkboxGroupInput` function with the choices of  `c("Low" = "loIc", "Mid" = "midIc", "High" = "hiIc")`.

   Use the following script as a framework for the `paramchkbxgrp` object:

   ~~~
   output$paramchkbxgrp <- renderUI({
                if (is.null(input$var))
                 return()
           # Depending on input$var, we'll generate a different
           # UI component and send it to the client.
               switch(input$var,
               "colless" = checkboxGroupInput(inputId = "PARAMS", label = "",
                   choices = c(
                       "Low" = "loIc",
                       "Mid" = "midIc",
                       "High" = "hiIc"
                       ),
                    selected = c("loIc","midIc","hiIc")),
               #Fill in the ellipses with the corresponding parameter values
                "numsp" = checkboxGroupInput(...),
                "spatial" = checkboxGroupInput(...),
                )
             })
           })
   ~~~

2. When certain checkboxes are unselected, display the text as grey with some transparency. To do this, within the `renderPlot` function, adjust the `cols` object such that the unselected are black with high transparency (display as grey). To do this for the `cols` object, subset for when `input$PARAMS` is not in `levels(fbar$PARAMS)`:

   ~~~
   cols[which(!(levels(fbar$param) %in% input$PARAMS))]
   ~~~

   Then assign all of these instances as black `rgb(0,0,0, maxColorValue=255)` with very high transparency `rgb(0,0,0, alpha =25, maxColorValue=255)`:

   ~~~
   cols[which(!(levels(fbar$param) %in% input$PARAMS))]<- rgb(0,0,0, alpha=25,maxColorValue=255)
   ~~~

<h4>HINTS:</h4>

1. ~~~
   ## Drop-down menu to select Factor
   output$paramchkbxgrp <- renderUI({
        if (is.null(input$var))
          return()

     # Depending on input$var, we'll generate a different
     # UI component and send it to the client.
      switch(input$var,
        "colless" = checkboxGroupInput("PARAMS", "",
          choices = c("Low" = "loIc",
                      "Mid" = "midIc",
                      "High" = "hiIc"
                      ),
          selected = c("loIc","midIc","hiIc")),
        "numsp" = checkboxGroupInput("PARAMS", "",
          choices = c("16 Species" = 16,
                      "64 Species" = 64,
                      "256 Species" = 256),
          selected = c(16,64,256)),
        "spatial" = checkboxGroupInput("PARAMS", "",
          choices = c("True" = "TRUE",
                      "False" = "FALSE"),
          selected = c("TRUE","FALSE")),
      )
      })
   ~~~

2. ~~~
   output$pcaplot <- renderPlot({
            #Match user's variable input selection by subsetting for when foo$Var==input$var
            fbar<-droplevels(foo[which(foo$Var==input$var),])

           # Generate colors to correspond to the different Variables' parameters. E.g., for the variable "colless", different colors for "loIc","midIc", and "hiIc"
            cols<-c("#1f77b4","#ff7f0e","#2ca02c")[1:length(levels(fbar$param))]

            #***********************ADD THIS TO EXISTING SCRIPT *************************
            #If the param is not selected, set the color value to grey with transparency
            cols[which(!(levels(fbar$param) %in% input$PARAMS))]<- rgb(0,0,0, alpha=25,maxColorValue=255)
            #****************************************************************************

            #Render the scatterplot of PCA
            plot(PC2 ~ PC1, data=fbar, type="n", xlab="PC1", ylab="PC2")

            #For each of the different parameter values (different colors), plot the text names of the metrics
            for(i in levels(fbar$param)){
                foo2<-subset(fbar,param==i)
                text(PC2 ~ PC1, data=foo2, labels=foo2$metric, col=cols[which(levels(fbar$param)==i)],  cex=input$cexSlider)
            }

            #Add a legend for the different parameter values (with corresponding colors) of the selected Variable
            legend("topright", fill=cols, legend=levels(fbar$param))

      })
   ~~~

<h1>Module 4</h1>

We've now learned some of the basic tools for building a shiny app. Now complete the tasks to add additional bells and whistles to the shiny app. After you have finished with your app, you can deploy it to the world to see. There are a number of options for this, which I won't go into detail because it depends on your personal preference for how you want the data shared (See http://shiny.rstudio.com/tutorial/lesson7/)

<h2>ui.R</h2>

<h3>TASK:</h3>

1. Create the ability to zoom in or out of the plots. Create two `sliderInput` objects to adjust the x- and y-axes of the plot depending on the Variable selected. To do so:
   1. Within the `sidebarPanel` of the `ui.R` script, add two `uiOutput` objects, containing the `outputId` names of `sliderX` and `sliderY`
   2. In `script.R`, create the `output$sliderX` and `output$sliderY` objects with the function `renderUI`. (see `script.R`)
2. Change the plot `width`. For `plotOutput(outputId="pcaplot")`, add width `(width = "750px")` and height `(height = "650px")` parameters

<h4>HINTS:</h4>

1. ~~~
   sidebarPanel(
        selectInput(inputId='var', ...),
        uiOutput(outputId="paramchkbxgrp"),
        sliderInput(inputId = "cexSlider", ...),
        #********ADD THIS SCRIPT********
        uiOutput(outputId="sliderX"),
        uiOutput(outputId="sliderY")
        #*******************************
   )
   ~~~

2. ~~~
   plotOutput(outputId="pcaplot",  width="750px",height="750px")
   ~~~

<h2>server.R</h2>
<h3>TASKS:</h3>
1. Create two `sliderInput` objects to adjust the x- and y-axes of the plot depending on the Variable selected. To do so:
   1. Within the `sidebarPanel` of the `ui.R` script, add two `uiOutput` objects, containing the `outputId` names of `sliderX` and `sliderY` (see `ui.R`)
   2. In `server.R`, create the `output$sliderX` and `output$sliderY` objects with the function `renderUI`. The `renderUI` function allows the function within to be reactive.
      1. within the `renderUI` wrapper, use the `sliderInput` function:

         ~~~
         sliderInput(inputId, label, min, max, value)
         ~~~

         `inputId`
         : `SLIDERX` for the x-axis; `SLIDERY` for the y-axis

         `label`
         : `h5("x-axes")` for the x-axis; `h5("y-axes")` for the y-axis

         `min`
         : subset the object `foo` (with the function `subset`) for the minimum (use function `min`) value of PC1 (for x-axis) or PC2 (for y-axis) when `Var==input$var`

         `max`
         : subset the object `foo` (with the function `subset`) for the maximum (use function `max`) value of PC1 (for x-axis) or PC2 (for y-axis) when `Var==input$var`

         `value`
         : the concatenated values of the two aforementioned `min` and `max` values: subset the object `foo` for the minimum/maximum value of PC1/PC2 when `Var==input$var`

   3. For the scatterplot (`plot`) of PCA within the `output$pcaplot` function, change the plot parameters `xlim` and `ylim` to change with the `input$SLIDERX` and `input$SLIDERY` values.

2. After evaluating the `plot` function, add red (`col = "red"`) dotted lines (`lty = 2`) at x=0 (`h=0`) & y=0 (`v=0`) with the function `abline`.

3. Implement the percent variation explained into the plot axes.
   1. First, within the `output$pcaplot`'s `renderPlot` function, create an object `pcaper` to subset `pca_percent` for when `pca_percent$Var==input$var`
   2. Within the `plot` function, adjust the `xlab` and `ylab` parameters. With the `paste` function, for `xlab`, add `pcaper[2]` as the x-axis percent variation explained: `xlab=paste("PCA Axis 1 (",pcaper[2],"%)")`

      Do the same for `ylab`, where instead use `pcaper[3]`

4. Use the R `expressions` instead to display labels. Paste the following code into your script:

   ~~~
   output$pcaplot <- renderPlot({
            ...
            for(i in levels(fbar$param)){
                foo2<-subset(fbar,param==i)
                labs<-paste("c(",paste("expression(",foo2$Rexpression,")",sep="",collapse=","),")",sep="")
                text(PC2 ~ PC1, data=foo2, labels=eval(parse(text=labs)), col=cols[which(levels(fbar$param)==i)],  cex=input$cexSlider)
            }
            #...
        })
   ~~~

<h4>HINTS:</h4>
1. ~~~
   shinyServer(function(input, output) {
        output$paramchkbxgrp <- renderUI({...})

       ********ADD THIS SCRIPT********
        #X-axis
              output$sliderX <-renderUI({
                sliderInput(inputId="SLIDERX",
                    label = h5("x-axes"),
                    min = min(subset(foo,Var==input$var)[,"PC1"]),
                    max = max(subset(foo,Var==input$var)[,"PC1"]),
                    value = c(min(subset(foo,Var==input$var)[,"PC1"]),max(subset(foo,Var==input$var)[,"PC1"])))
            })
       # Y-axis
              output$sliderY <-renderUI({
                sliderInput(inputId="SLIDERY",
                    label = h5("y-axes"),
                    min = min(subset(foo,Var==input$var)[,"PC2"]),
                    max = max(subset(foo,Var==input$var)[,"PC2"]),
                    value = c(min(subset(foo,Var==input$var)[,"PC2"]),max(subset(foo,Var==input$var)[,"PC2"])))
            })
       *******************************

        output$pcaplot <- renderPlot({...})
    })
   ~~~

2. ~~~
   output$pcaplot <- renderPlot({
       #...
       plot(PC2 ~ PC1, data=fbar, type="n", xlab="PC1", ylab="PC2", xlim=input$SLIDERX, ylim=input$SLIDERY)
       #...
   })
   ~~~

3. ~~~
   output$pcaplot <- renderPlot({
        #...
        plot(PC2 ~ PC1, data=fbar, type="n", xlab="PC1", ylab="PC2", xlim=input$SLIDERX, ylim=input$SLIDERY)
        abline(h=0,v=0,col="red",lty=2)
        #...
   })
   ~~~

4. ~~~
   output$pcaplot <- renderPlot({
        fbar<-droplevels(...)

        pcaper<-pca_percent[which(pca_percent$Var==input$var),]

        plot(PC2 ~ PC1, data=fbar, type="n", xlim=input$SLIDERX, ylim=input$SLIDERY,
            xlab=paste("PCA Axis 1 (",pcaper[2],"%)"),
            ylab=paste("PCA Axis 2 (",pcaper[3],"%)"))
        #    ...
   })
   ~~~

<h1>Module 5</h1>

Running this module should create the final output acheived when completing all the tasks.
