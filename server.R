library(shiny) 

function(input, output) {
  output$hist <- renderPlot({
    text <-scan("brt-2018-07-24.txt","character",sep="\n");
    frequent_terms <- freq_terms(text, input$num)
    plot(frequent_terms)
    })
}