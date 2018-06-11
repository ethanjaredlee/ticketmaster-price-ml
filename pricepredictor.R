library(glmnet); library(car)
shows = read.csv("/Users/ryanrawitscher/Desktop/ticketmaster-price-ml/mintry.csv")
head(shows)
row.names(shows) = shows$X
shows$X=NULL
set.seed(12345)
train = runif(nrow(shows))<.9    # pick train/test split
dim(shows)
table(shows$minprice)
hist(shows$minprice)

# Residual plot
fit = lm(minprice ~ weekend+pop+score+genre+month, shows, subset=train)
plot(fit, pch=16)

# full model
fit = lm(minprice ~ weekend+pop+score+genre+month, shows, subset=train)
plot(fit, which=1, pch=16, cex=.8)
yhat = predict(fit, shows[!train,])
mean((shows$minprice[!train] - yhat)^2)      # compute test set MSE as 296.3087
summary(fit)
vif(fit)

# stepwise model
fit2 = step(fit)
yhat = predict(fit2, shows[!train,])
mean((shows$minprice[!train] - yhat)^2)       # compute test set MSE as 296.5095
summary(fit)

# ridge model
x = model.matrix(minprice ~ weekend+pop+score+genre+month, shows)
fit.ridge = glmnet(x[train,], shows$minprice[train], alpha=0)
plot(fit.ridge, xvar="lambda")
fit.cv = cv.glmnet(x[train,], shows$minprice[train], alpha=0) # find optimal lambda
fit.cv$lambda.min        # optimal value of lambda
plot(fit.cv)          # plot MSE vs. log(lambda)
yhatridge = predict(fit.ridge, s=fit.cv$lambda.min, newx=x[!train,])  # find yhat for best model
mean((shows$minprice[!train] - yhatridge)^2)     # compute test set MSE as 302.556

#lasso model
fit.lasso = glmnet(x[train,], shows$minprice[train], alpha=1)
plot(fit.lasso, xvar="lambda")
fit.cv = cv.glmnet(x[train,], shows$minprice[train], alpha=1)
yhatlasso = predict(fit.lasso, s=fit.cv$lambda.min, newx=x[!train,])
mean((shows$minprice[!train] - yhatlasso)^2)       # compute test set MSE as 300.4573

# Transformations
plot(shows[train,-1,-7], pch=16, cex=.5)
par(mfrow=c(1,1))
for(i in 3:7){
  plot(shows[,i], shows$minprice, pch=16, cex=.5, main=names(shows)[i])
  lines(smooth.spline(shows[,i], shows$minprice, df=2),)
} 
par(mfrow=c(1,1))
plot(minprice ~ log(score), shows, pch=16)

# forward stepwise model
fit= lm(minprice ~ 1, shows, subset=train)
fit2 = step(fit, scope=~weekend+pop+score+genre+month)
plot(fit2, pch=16, cex=.5)
yhat = predict(fit2, shows[!train,])
mean((shows$minprice[!train] - yhat)^2) #MSE=296.5095


# forward stepwise GAM model
library(gam)
fit= gam(minprice ~ 1, data=shows, subset=train)
fit2 = step.gam(fit, scope=list("Weekend"=~1+weekend,
                                "Population"=~1+pop+s(pop),
                                "Genre"=~1+genre,
                                "Artist Score"=~1+score+s(score),
                                "Month"=~1+month+s(month)
))
summary(fit2)
plot(fit2, ask=T, se=T)
yhat = predict(fit2, shows[!train,])
mean((shows$minprice[!train] - yhat)^2) #MSE is 283.8466
plot(fit2$fitted.values, fit2$residuals, pch=16, cex=.7)
lines(smooth.spline(fit2$fitted.values, fit2$residuals, df=5), col=2)

# try tree
library(tree)
fit = tree(minprice ~ weekend+pop+score+genre+month, shows[train,])
fit
yhat = predict(fit, newdata=shows[!train,])
mean((shows$minprice[!train] - yhat)^2) #MSE is 348.4048

# overgrow the tree
fit = tree(minprice ~ weekend+pop+score+genre+month, shows[train,], mindev= .0001)
plot(cv.tree(fit))
yhat = predict(prune.tree(fit, best=10), newdata=shows[!train,]) #MSE is 417.9521
mean((shows$minprice[!train] - yhat)^2) # 
yhat = predict(prune.tree(fit, best=20), newdata=shows[!train,]) #MSE is 395.9752
mean((shows$minprice[!train] - yhat)^2) # 
yhat = predict(prune.tree(fit, best=30), newdata=shows[!train,]) #MSE is 384.4649
mean((shows$minprice[!train] - yhat)^2) # 
yhat = predict(prune.tree(fit, best=40), newdata=shows[!train,]) #MSE is 394.1503
mean((shows$minprice[!train] - yhat)^2) #

# Random Forest
yz=shows[-7]
library(randomForest)
set.seed(12345)
fit  = randomForest(x=yz[train,-1], y=shows$minprice[train], xtest=yz[!train,-1], ntree=100)
varImpPlot(fit)
mean((shows$minprice[!train] - fit$test$predicted)^2) # MSE is 250.9376

# Random forest with more trees
fit  = randomForest(x=yz[train, -1], y=shows$minprice[train], xtest=yz[!train,-1], ntree=1000)
mean((shows$minprice[!train] - fit$test$predicted)^2) # 248.0282

# now try bagging
fit  = randomForest(x=yz[train, -1], y=shows$minprice[train], xtest=yz[!train,-1], ntree=100, mtry=2)
varImpPlot(fit)
mean((shows$minprice[!train] - fit$test$predicted)^2) #  225.1693

# bagging with more trees
fit  = randomForest(x=yz[train, -1], y=shows$minprice[train], xtest=yz[!train,-1], ntree=500, mtry=2)
mean((shows$minprice[!train] - fit$test$predicted)^2) # 215.9549


# boosted tree
library(gbm)
fit = gbm(minprice ~ ., data=shows[train,], interaction.depth=2, n.trees=500)
yhat = predict(fit, newdata=shows[!train,], n.trees=500)
mean((shows$minprice[!train] - yhat)^2) # 289.4104

