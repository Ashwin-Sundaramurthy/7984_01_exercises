library(dplyr)
library(lubridate)
library(readxl) #read excel files
library(tidyr)
library(varhandle) #unfactor
library(readr) #read_lim
library(descr) #crosstab
library(imputeTS)#impute values
library(mltools)#create bins
library(assertr)
library(stringr)
# df['genre']<-apply(df>%>select(16,44),1,function(x) paste(names(x[x==1]),collapse=" "))
df.2<-read_delim("imdb.csv", delim=',', escape_double=FALSE, escape_backslash=TRUE)
df.3<-read_delim("diamonds.csv", delim=',', escape_double=FALSE, escape_backslash=TRUE)
df.1=read_delim('movie_metadata.csv', delim=',', escape_double=FALSE, escape_backslash=TRUE)

#qn 3
bonus.3<-function(df.3)
{
df.3$z[df.3$z=="None"]<-NA
df.3$z<-as.numeric(df.3$z)
x<-na_mean(df.3)
x$volume <- ifelse(x$depth>60,(x$x)*(x$y)*(as.integer(x$z)), 8)
x$quant<-as.numeric(bin_data(x$volume,bins=5,binType="quantile"))
y<-crosstab(x$quant,x$cut,plot=FALSE,prop.c=TRUE)
print(y)
}
#Qn 2
bonus.2<-function(df.2)
{ 
  x<-na_mean(df.2)
  x$year=floor(x$year)
  x$len=nchar(x$wordsInTitle)
  x[is.na(x$wordsInTitle),"len"]=nchar(as.character(unlist(x[is.na(x$wordsInTitle),"title"])))
  x$percentile<-bin_data(x$duration,bins=4,binType = "quantile")
  d<-as.data.frame.matrix(table(x$year,x$percentile))
  colnames(d)<-c("num_videos_less_than25Percentile","num_videos_25_50Percentile ","num_videos_50_75Percentile","num_videos_greaterthan75Precentile")
  y<-x%>%group_by(year)%>%summarise(min=min(len),max=max(len))
  print(cbind(y,d))
}

bonus.5<-function(df.2)
{
  df.2=na_mean(df.2)
  df.2$decile=as.numeric(bin_data(df.2$duration,bins=10,binType="quantile"))
  a<-df.2[,17:45]
  b<-a%>%group_by(decile)%>%summarise_all(sum)
  x<-df.2%>%group_by(decile)%>%summarise(nominations=sum(nrOfNominations),wins=sum(nrOfWins),count=n())
  x$top_genres=top_genre=col_concat(t(as.data.frame(apply(b,1,function(x) head(names(b)[order(-x)],3)),stringsAsFactors = FALSE)),sep="|")
print(x)
}

bonus.1<-function(df)
{
  x<-df%>%select(16:44)
  df$genre_combo<-apply(x,1,function(x) paste(names(x[x==1]),collapse=" "))
  y<-df%>%group_by(year,type,genre_combo)%>%summarise(avg=mean(imdbRating),min=min(imdbRating),max=max(imdbRating),total_run_time=(sum(duration)/60))
  return(y)
}


bonus.4<-function(df.1)
{
    df=na.omit(df.1)
    x<-df%>%group_by(title_year)
    x=x[with(x,order(-gross)),]
    x<-x%>%group_map(~head(.x,ifelse (nrow(.x)<10,1, as.numeric(0.1*nrow(.x)))),keep=TRUE) %>%bind_rows()
    t<-x%>%group_by(title_year,genres)%>%summarise(avg=mean(imdb_score),count=n())
    return(t)
}
