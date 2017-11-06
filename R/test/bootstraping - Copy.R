recr=read.csv(file.choose(),header=TRUE,sep=",")   ##reading the csv file : filename- boot.csv
names(recr)                        ## the 8 factors are No..of.Social.Media,Company.Age,Employee.Strength,Social.Media.Score,No.of.Subsidiaries,Gross.Profit,Revenue_latest.year,
                                 ##Net.Income[excluding the factors with binomial data]         

library(boot)                                    ##loading the boot package
      
mat=matrix(0,50,8)             ##defining a null matrix with 50 rows & 8 columns

##for generating 50 more values for each of the factors
for(i in 1:8)
{
  d=recr[,i]
  d1=data.frame(d)


  tstat=function(x,indices)		#defining the mean statistic
  {
   t1=mean(x[indices,])             
   return(t1)
}

b1=boot(data=d1,statistic=tstat,R=10000)     #using the boot package
b1                    
mat[,i]=b1$t[1:50]
}
   
mat                                     ##compiling the data for the 8 factors in matrix form
write.csv(mat,"D:/bootstrap.csv")        ##storing it in a new csv file for further use

#----------------------------------------------------------------------------------------------------------------------------------
generating new data values for 
data1=read.csv(file.choose(),header=TRUE,sep=",")    ##reading the data : filename - sample_new_data.csv


a=matrix(0,50,47)                                 ##defining a null matrix 
generating new samples for each factor 
for(i in 1:47)
{
  x=data1[,i]
  x=sample(x,size=50,replace=TRUE)                 ##sampling with replacement
  a[,i]=x
}
a                                                                      ##compiling the data  in matrix form
write.csv(a,"D:/binomialsample.csv")              ##storing it in a new csv file for further use


