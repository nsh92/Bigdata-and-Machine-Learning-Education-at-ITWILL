if (!require(tidyquant)) install.packages("tidyquant", repos = "https://cloud.r-project.org/", verbose = F)
library(tidyquant)
tq_get_options()

ss2 <- tq_get("^KS11", from="1980-01-01", to="2016-05-05")
ss <- tq_get("005930.KS", from="1980-01-01", to="2016-05-05")
ss1 <- tq_get("005380.KS", from="1980-01-01", to="2016-05-05")

if (!require(remotes)) install.packages("remotes", verbose = F)
library(remotes)
if (!require(tqk)) install_github("mrchypark/tqk", verbose = F)
library(tqk)
code <- code_get()

sscode <- code[grep("^삼성전자$", code$name),1]
samsung <- tqk_get(sscode, from="1990-01-01", to="2016-05-05")

sscode1 <- code[grep("^현대자동차$", code$name),1]
samsung <- tqk_get(sscode1, from="1990-01-01", to="2016-05-05")
