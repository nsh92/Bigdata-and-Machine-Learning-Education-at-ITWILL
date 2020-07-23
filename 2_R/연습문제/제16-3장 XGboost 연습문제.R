################################
## 제16-3장 XGBboost 연습문제 
################################

# 01. UniversalBank.csv 데이터셋을 이용하여 다음과 같이 XGBoost에 적용하여 분류하시오. 
# 조건1> 포물라 : formula <- Personal.Loan ~.
# 조건2> 모델 성능 평가
# 조건3> 중요변수 보기
library(xgboost)
# 대출 수락 or 거절 prediction
setwd("c:/ITWILL/2_Rwork/Part-IV")
Data = read.csv('UniversalBank.csv',  stringsAsFactors = F)
str(Data)
Data = Data[c(-1, -5)] # 1, 5번 칼럼 제외 


# Personal.Loan -> y변수(대출여부) 
str(Data)

# 1. data set 생성 
idx <- sample(nrow(Data), nrow(Data)*0.7)
train <- Data[idx, ]
test <- Data[-idx, ]
dim(train) # 3500   12
dim(test) # 1500  12

# 2. xgb.DMatrix 생성 : data(x):matrix, label(y):vecor 
train_mat <- as.matrix(train[-8]) # matrix
train_mat[1,]

# y변수 : vector 
train_y <- train$Personal.Loan

# 3. model 생성 : xgboost matrix 객체 이용   
dtrain <- xgb.DMatrix(data = train_mat, label = train_y)
dtrain

xgb_model <- xgboost(data = dtrain, max_depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic", verbose = 0)

# 4. prediction 
names(test)
test_y <- test$Personal.Loan
test_x <- as.matrix(test[,-8])
pred <- predict(xgb_model, test_x)

# 5. cut off 적용 
range(pred)
y_pred <- ifelse(pred >= 0.5, 1, 0)

# 6. confusion matrix
tab <- table(test_y, y_pred)
tab

# 7. 모델 성능평가 : Accuracy
acc <- (tab[1,1]+tab[2,2])/length(test_y)
cat("모델 성능 :", acc*100, '%')

# 8. 중요변수 보기(model 비교) 
import <- xgb.importance(colnames(train_mat), model = xgb_model)
import
xgb.plot.importance(importance_matrix = import)