## Data Preprocessing

description of preliminary data preprocessing with images

Our dataset consists of 150,500 rows with 13 columns. A separate dataframe was created containing all of the location data as it is not needed for the initial machine learning model. Columns that will not affect the machine learning model such as "PdId", and "IncidntId" are dropped from the dataset completely. The remaining columns are "Category", "PdDistrict", and "Resolution". These columns make up the cleaned dataframe that will be used with the preliminary machine learning models. Several different models will be tested to find the best balance of accuracy scores and speed. This is a supervised machine learning problem focusing on classification. The dataset is labeled, and there is a clear binary outcome we can predict with our features. The resolution column is our target column. It contains 14 unique values. Analysis revealed that out of those 150,500 columns only 3,304 contained resolutions other than "ARREST, BOOKED" and "NONE". Making up just 2% of the dataset, these other values were bucketed and dropped.

![](./images/correlation_heatmap.png)



## Feature Engineering

description of preliminary feature engineering, selection, and decision making process

Since our dataset consists primarily of non-ordinal categorical variables sci-kit learn onehotencoder is the best choice for our variable encoding. The onehotencoder is a good choice for a tree based model because the result is binary rather than ordinal, and everything sits in orthogonal vector space. In addition to encoding, the data is scaled using sci-kit learn StandardScaler. This decision was made after realizing that the zipcodes need to be included for the ML model. The zipcodes are much larger than the rest of our encoded data, which was primarily 1's and 0's. A downside of the onehotencoder is that it can create a large number of features resulting in the curse of dimensionality. This can be averted by employing principal component analysis (PCA) after encoding categorical variables.

 PCA is a feature extraction method used to speed up machine learning algorithms when the number of features is too high. It allows us to reduce the dimensions of our dataset when we are not able to identify features to completely remove from consideration. Initially zipcode was excluded in PCA, but after reviewing the correlation heatmap it was included again because it has a strong correlation to our resolutions. After PCA we were able to reduce our features from 63 down to 50, while still capturing 97% of the variance.  

![](./images/PCA_graph.png)

## Training and Testing Sets

description of how data was split into training and testing sets

Since almost 60% of the resolutions are "NONE" randomly selecting a resolution gives a pretty good chance of selecting "NONE". In order to better utilize the model our training split is 50% of the data. The remaining 50% is split into 25% testing data and 25% validation data. This allows us to test the model twice, once with the testing data, and again with the validation set. This ensures that our accuracy numbers are accurate. 

## Explanation of model choice

ML model comparisons 

Random forests are robust to overfitting, can handle thousands of input variables without variable decision, and run efficiently on large datasets. In addition to that random forests handle categorical data well, and run quickly. We tested an ada-boost classifier, easy ensemble classifier, support vector machine, and a random forest. Out of those machine learning models, the random forest returned close to the highest initial accuracy score, and it ran the fastest. The graph below shows the feature ranking in the baseline model which used default parameters. This model was improved upon by reducing the number of dimensions.  

![](./images/GINI_graph.png)

## Accuracy Score

Our random forest model trained on our principal component dataset achieved an accuracy score of 98%. 

## Additional Training

Ideally we would implement a storage system for the user inputs and use those to continually retrain our model to get even more accurate results. 


## Problems Encountered

changes in model choice

After creating our interactive dashboard and linking it to our machine learning model I encountered a value error. We initially trained our model with an encoded dataframe containing 63 columns. This was reduced to 50 columns via principal component analysis, and the model used for the dashboard was trained with this dataframe. Our dashboard only asks for 4 user inputs right now. It does not seem realistic to ask the user to input 50 features. Right now the dataframe created with user input is populated with columns containing 0 to meet the 50 feature requirement for the model to predict. This is definitely causing accuracy issues. 