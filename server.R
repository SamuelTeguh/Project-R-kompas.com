library(shiny) 
library(qdap)
library(stopwords)
library(tm)

function(input, output) {
  output$hist <- renderPlot({
    stopwords <- read.csv("word.csv", header = FALSE)
    stopwords <- as.character(stopwords$V1)
    stopwords <- c(stopwords, stopwords())
    
    createCorpus <- function(filepath) {
      conn <- file(filepath, "r")
      fulltext <- readLines(conn)
      close(conn)
      
      vs <- VectorSource(fulltext)
      Corpus(vs, readerControl=list(readPlain, language="en", load=TRUE))
    }
    
    news_corpus <- createCorpus("brt-2018-07-24.txt")
    news_corpus_proc <- tm_map(news_corpus, content_transformer(tolower))
    news_corpus_proc <- tm_map(news_corpus_proc, removePunctuation)
    news_corpus_proc <- tm_map(news_corpus_proc, removeNumbers)
    news_corpus_proc <- tm_map(news_corpus_proc, removeWords, stopwords)
    frequent_terms <- freq_terms(news_corpus_proc, input$num)
    plot(frequent_terms)
    })
}
