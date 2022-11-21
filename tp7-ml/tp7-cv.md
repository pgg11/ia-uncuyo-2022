## create_folds()

<pre><code>
create_folds <- function(dataframe,folds_num){
  
  folds <- list()
  rows <- nrow(dataframe)
  fold_len <- as.integer(rows / folds_num)
  remaining_indexes = seq(1:rows)
  
  for (i in 1:folds_num){
    fold_indexes <- sample(remaining_indexes,fold_len,replace=FALSE)
    folds[[i]] <- dataframe[fold_indexes,]
    remaining_indexes <- setdiff(remaining_indexes, fold_indexes)
  }
  
  return(folds)
}
</code></pre>

## cross_validation()

<pre><code>
cross_validation <- function(dataframe,folds_num){
  
  train_formula<-formula(inclinacion_peligrosa ~ especie+altura+diametro_tronco+seccion+long+lat)
  folds <- create_folds(dataframe,folds_num)
  
  results <- list()

  for(i in 1:folds_num){
    test_data <- folds[[i]]
    if(i < folds_num){
      train_data = folds[[i+1]]
    }else{
      train_data = folds[[1]]
    }
    
    for(j in 1:folds_num){
      if(i == j | (i==folds_num & j==1)){
        next
      }
      
      train_data <- merge(train_data,folds[[j]],all=TRUE)
    }
    
  test_data$especie[which(!(test_data$especie %in% unique(train_data$especie)))] <- NA  
    
  tree_model<-rpart(formula=train_formula, data=train_data)
  
  p <- predict(tree_model,test_data,type="class")
  
  results[[i]] <- metrics_confusion_Matrix(test_data[[length(test_data)]],p)
  
  }
  result_matrix <- mean_std_confusion_matrix(results,folds_num)
  
  return(result_matrix)
}
</code></pre>
