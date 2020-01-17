library(dplyr)
library(lubridate)
library(readxl)
library(tidyr)
library(varhandle)
df<-read_xlsx("SaleData.xlsx")

question.one<-function(df)
{
  return (tapply(df$Sale_amt,df$Item,FUN=min))
}

question.two<-function(df)
{ 
  ans.1<-tapply(df$Sale_amt,df$Region,FUN=sum)
  ans.2<-tapply(df$Sale_amt,year(df$OrderDate),FUN=sum)
  return(list(ans.1,ans.2))
}

question.three<-function(df,ref.date)
{ 
  df$days_diff<-round(difftime(ref.date,df$OrderDate))
  return(df)
  
}

question.four<-function(df)
{ a<-df %>%group_by(Manager) %>%arrange(SalesMan) %>%
  unique() %>%  summarise(Sale=list(unique(SalesMan))) %>%ungroup()
  return (a)
}

question.five<-function(df)
{  
 return(df%>%group_by(Region)%>%summarise(Salesman_count=n_distinct(SalesMan),total_sales=sum(Sale_amt))%>%ungroup())
}

question.six<-function(df)
{ 
  t=sum(df$Sale_amt)
  return(df%>%group_by(Manager)%>%summarise(percentage=(sum(Sale_amt)/t)*100)%>%ungroup())
}

df.2<-read.csv("imdb.csv")

question.seven<-function(df.2)
{
  return(df.2[5,6])
}

question.eight<-function(df.2)
{
  return(arrange(df.2,duration)[c(1,nrow(df.2)),'title'])
}

question.nine<-function(df.2)
{
  return(arrange(df.2,year,desc(imdbRating)))
}

question.ten.c<-function(df.2)
{
  return(subset(df.2,between(duration,30,180)))
}

df.3<-read.csv("Diamonds.csv")

question.eleven<-function(df.3)
{
  return(sum(duplicated(df.3)))
}  

question.twelve<-function(df.3)
{
  df.3<-drop_na(df.3,c("carat","cut"))
  return(df.3)
}

question.thirteen<-function(df.3)
{
  return(df.3[sapply(df.3,is.numeric)])
}

question.fourteen<-function(df.3)
{
  x<-na.omit(df.3)
  x<-unfactor(x)
  x$volume <- ifelse(x$depth>60,(x$x)*(x$y)*(as.integer(x$z)), 8)
  print((x))
}

question.fifteen<-function(df.3)
{
  df.3$price[is.na(df.3$price)]<-mean(df.3$price,na.rm=T)
  return (df.3)
}