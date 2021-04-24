This folder contain my ML learning path.

1. Data Preparation
   In this part, preprocessing is performed before it is used for the main model
   - Converting data to the dataframes\n
     Using pandas module to read the data and transform it into the dataframes
   - Scaling the data using normalization (transforming data to 0-1 range) and standardization (transforming data using Z-score)
     Normalization using MinMaxScaler class and standardization using StandardScaler class from sklearn.preprocessing module  
   - Splitting the dataset into train set, validation set, and test set
     Using sklearn.train_test_split 
   - Test the validation predict score (85% - 99% is great)
     Using sklearn.cross_val_score to check the validation prediction score from the whole dataset. Using K-Fold Cross Validation (divide the dataset into the k fold)
