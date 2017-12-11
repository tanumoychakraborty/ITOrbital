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
library(rJava)
library(wordnet)

tweets<-read.csv(file.choose())
tweets
names(tweets)
tweets=tweets[,1:5]
tw=tweets[,3]
tw1=gsub("(RT|via)((?:\\b\\w*@\\w+)+)","",tw)
tw2=gsub("http[^[:blank:]]+","",tw1)
tw3=gsub("@\\w+","",tw2)
tw3
tw=tolower(tw)
tw_cln=rep(0,length(tw))

cl_list=as.character(c("in","on","to","of","for","from","at","am","is","are","was","were","'s","we","'re","the","our","there","me","my","you","https://t","http://t","https","a","and","or","with","how","what","where","why","you","your","it","that","those","there","their","'ve","i","be","by","who","but","t","an","as"))

for( i in 2:length(tw)){

tw_cln[i]=removeWords(as.character(tw[i]), stopwords(kind="en"))
tw_cln[i]=removeWords(as.character(tw[i]), cl_list)

}
tw_cln


pal=brewer.pal(8,"Dark2")
wordcloud(tw_cln,min.freq=1,max.words=1000,width=1000,height=10200,random.order=F,color=pal)

sentiment=get_nrc_sentiment(tw_cln)
sentiment_scores=data.frame(colSums(sentiment[,]))
names(sentiment_scores)="scores"
sentiment_scores=cbind("sentiment"=rownames(sentiment_scores),sentiment_scores)
rownames(sentiment_scores)=NULL

ggplot(data=sentiment_scores,aes(x=sentiment,y=scores))+geom_bar(aes(fill=sentiment),stat="identity")+theme(legend.position="none")+
        xlab("sentiment")+ylab("scores")+ggtitle("Total sentimental scores")

word=rep(NA,100*length((as.character(tw_cln))))
w=0


for(r in 1:length(tw_cln)){
twi=as.character(tw_cln[r])
j=0

for(i in 1:nchar(twi))
{
if(substr(twi,i,i)==" "||substr(twi,i,i)==","||substr(twi,i,i)=="!"||substr(twi,i,i)=="?"||substr(twi,i,i)=="."||substr(twi,i,i)=="'"||substr(twi,i,i)=="?"||substr(twi,i,i)=="."||substr(twi,i,i)=="&"||substr(twi,i,i)=="-" )
{
word[w]=substr(twi,j,i-1)
j=i+1	
}
w=w+1
}
}
word
tabw=table(word)
tabww=data_frame(word = names(tabw), count = as.numeric(tabw)) 
wordc=arrange(tabww, desc(count))

wordf=data.frame(wordc)
wordf[1:100,]
dim(wordf)

get_sentiment_dictionary()
get_sentiment_dictionary('bing')
get_sentiment_dictionary('afinn')
get_sentiment_dictionary('nrc')


write.csv(wordf, file = "word.csv")




#extracting hash words to gauge sentiment on hashtags.

library(stringr)
tw3
x<- str_extract(tw3, "#\\S+")
x
a= na.omit(x)
wordcloud(a,min.freq=1,max.words=1000,width=1000,height=1000,random.order=F,color=pal)

