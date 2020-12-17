#install the packages
install.packages("finreportr")
install.packages("tidyverse")
library(finreportr)
library(tidyverse)

#Accessing financial data from EDGAR
#finreportr
#Data frame
company <- data.frame(ticker=c('WFC','JPM',"WAL"),
                     name=c("Wells Fargo & Company",
                            "J P Morgan Chase & Co",
                            "Western Alliance Bancorporation"))

#Get balance sheet data
bs <- data.frame()
for (i in company$ticker) {
  x <- GetBalanceSheet(i,2018)
  x <- mutate(x, ticker = rep(i,nrow(x)))
  bs <- rbind(bs, x)
}

#Get income statement for the banks in the sample
inc <- data.frame()
for (i in company$ticker) {
  x <- GetIncome(i,2018)
  x <- mutate(x, ticker = rep(i,nrow(x)))
  inc <- rbind(inc, x)
}

#Get cash flow data
bs <- data.frame()
for (i in company$ticker) {
  x <- GetCashFlow(i,2018)
  x <- mutate(x, ticker = rep(i,nrow(x)))
  bs <- rbind(bs, x)
}

#Get company info
bs <- data.frame()
for (i in company$ticker) {
  x <- CompanyInfo(i,2018)
  x <- mutate(x, ticker = rep(i,nrow(x)))
  bs <- rbind(bs, x)
}

#Get annual reports
bs <- data.frame()
for (i in company$ticker) {
  x <- AnnualReports(i,2018)
  x <- mutate(x, ticker = rep(i,nrow(x)))
  bs <- rbind(bs, x)
}


