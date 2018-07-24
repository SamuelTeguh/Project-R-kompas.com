library(shiny)

fluidPage(  
  headerPanel(HTML("<div align=center>Project R Kompas.com</div>")),
  
  sidebarLayout(
    sidebarPanel(
      numericInput("wordNum", 
                   "Number of Words:", 
                   20 , 
                   min = 1, 
                   max = 1000)
    ),

    mainPanel(
      titlePanel(HTML("<div align=center>Words Frequency</div>")),
      plotOutput("hist")
    )
  
  )
)
