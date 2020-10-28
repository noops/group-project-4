## Data Preprocessing

description of preliminary data preprocessing with images

Our dataset consists of 150,500 rows with 13 columns. A separate dataframe was created containing all of the location data as it is not needed for the initial machine learning model. Columns that will not affect the machine learning model such as "PdId", and "IncidntId" are dropped from the dataset completely. The remaining columns are "Category", "PdDistrict", and "Resolution". These columns make up the cleaned dataframe that will be used with the preliminary machine learning models. Several different models will be tested to find the best balance of accuracy scores and speed. This is a supervised machine learning problem focusing on classification. The dataset is labeled, and there is a clear binary outcome we can predict with our features. The resolution column is our target column. It contains 14 unique values. Analysis revealed that out of those 150,500 columns only 3,304 contained resolutions other than "ARREST, BOOKED" and "NONE". Making up just 2% of the dataset, these other values were bucketed and dropped. The resolution column can then easily be used as a binary classifier by converting "ARREST, BOOKED" to 1 and "NONE" to 0.

## Feature Engineering

description of preliminary feature engineering, selection, and decision making process

The feature engineering process for this dataset consisted of principal component analysis (PCA). PCA is a feature extraction method used to speed up machine learning algorithms when the number of features is too high. By finding the eigenvalues and eigenvectors, they come in pairs, of the covariance matrix we are able to get the principal components. The eigenvectors of the covariance matrix are the directions of the axes where there is the most variance, these are the principal components. The eigenvalues are the coefficients attached to the eigenvectors. They give us the amount of variance carried in each principal component. This allows us to reduce the dimensions of our dataset when we are not able to identify features to completely remove from consideration.  

![](./images/PCA_graph.png)

## Training and Testing Sets

description of how data was split into training and testing sets

## Explanation of model choice

ML model comparisons 