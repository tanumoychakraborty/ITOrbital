recr=read.csv(file.choose(),header=TRUE)
com=data.frame(recr$Company.Names)
app=recr$App
d=data.frame(app)

aa1=c("Robert Half 
Dhr International 
Sthree PLC 
Heidrick & Struggles
On Assignment 
True Blue 
Volt Information Sciences
Hudson Global
USG People 
Practicus
 
 
                  
                          
",
"Robert Walters
Kforce
CDI
Adecco
HAYS
Korn Ferry 
Randstad 
Kelly Services 
Manpower Group 
Page Group 
Brunel
                  
                 
             
")

a=c(47.619047,52.380952)
barplot(a,names.arg=aa1,las=1,col=c(5,7),col.axis=c(1),cex.lab=2.5)

ct2=c("Dhr International
USG People
Practicus
                     
",
"Robert Half
Robert Walters
Sthree PLC
Kforce
Korn Ferry
Heidrick & Struggles
Randstad
Kelly Services
Manpower Group
CDI
Adecco
On Assignment
HAYS
Brunel
True Blue
Volt Information Sciences
Hudson Global
Page Group

                   
")
ct=c(14.2857,85.7142)
barplot(ct,names.arg=ct2,las=1,col=c(3,5))



