library(tidytext)

library(tm)
library(plyr)
library(dplyr)
library(stringr)
library(RColorBrewer)
library(wordcloud)
library(sentimentr)
library(syuzhet)
library(ggplot2)

tweets<-read.csv(file.choose(),sep=",",header=TRUE)
tweets
names(tweets)
tweets=tweets[,1:5]
tw=tweets[,3]
tw
tw=tolower(tw)
length(tw)

tw_cln=rep(0,length(tw5))

cl_list=as.character(c("in","on","to","of","for","from","at","am","is","are","was","were","'s","we","'re","the","our","there","me","my","you","https://t","http://t","https","a","and","or","with","how","what","where","why","you","your","it","that","those","there","their","'ve","i","be","by","who","but","t","an","as"))

for( i in 2:length(tw)){

tw_cln[i]=removeWords(as.character(tw[i]), stopwords(kind="en"))
tw_cln[i]=removeWords(as.character(tw[i]), cl_list)

}

for(i in 1:length(tw_cln)){
if(tw_cln[i]=="")
tw_cln[i]=NA
}
tw_cln=na.omit(tw_cln)

sent_posts=rep(0,length(tw))


  for(i in 2:length(tw_cln)){

       sentiment=get_nrc_sentiment(tw_cln[i])
       sentiment_scores=data.frame(colSums(sentiment[,]))
       names(sentiment_scores)="scores"
       sentiment_scores=cbind("sentiment"=rownames(sentiment_scores),sentiment_scores)
       rownames(sentiment_scores)=NULL
     if(sentiment_scores[4,2]>0){   ##fear sentiment
     sent_posts[i]=tw_cln[i]
     }else{ 
     sent_posts[i]=NA
   }
}
sent_posts
sent_posts2=na.omit(sent_posts)
length(sent_posts2)
sentiment_scores   
pal=brewer.pal(8,"Dark2")

wordcloud(sent_posts2,min.freq=2,max.words=1000,width=30000,height=3000,random.order=F,color=pal)


