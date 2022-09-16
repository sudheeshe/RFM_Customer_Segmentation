
# Project Title

RFM Segmentation using KMeans Clustering


## Documentation

[What is RFM stands for...??](https://linktodocumentation)


RFM segmentation is a well-known user segmentation strategy based on three user characteristics:

- Recency (R): How recent was the customer's last purchase?
- Frequency (F): How often does the customer transact?
- Monetary (M): How much money did the customer spend in a given period??

The RFM Analysis will help the businesses to segment their customer base into different homogenous groups so that they can engage with each group with different targeted marketing strategies. 
Sometimes RMF is also used to identify the High-Value Customers (HVCs).

[Business Scenario](https://linktodocumentation)

We want to segment our customers to help 
the marketing department to give personalized offers or rewards based on the customer segments. 
Therefore, we will save our time and money 
for marketing and customers can also get beneficial.

[Data understanding](https://linktodocumentation)


###### 🔗 Data Description
[click here](https://archive.ics.uci.edu/ml/datasets/online+retail)



Lets see the sample of data which is provided

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/sample_data_head_snap.jpg?raw=true)


![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_1.jpg?raw=true)

- We have 8 variables in the data
- Around 1.4 lakh missing records (3.1% of total data)
- 4879 duplicate records (0.9% of total data)

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_2.jpg?raw=true)


Now lets see each column in detail

- Ignoring `InvoiceNo.` , `StockCode`, `Description` columns for now

`Column - Quantity`

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_3.jpg?raw=true)

- There are extreme minimum and maximum values (outliers)
- There are Negatives values (2% of whole data)

Now lets see the value_counts

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_4.jpg?raw=true)


`Column - UnitPrice`

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_7.jpg?raw=true)

- There are extreme minimum and maximum values (outliers)
- There are 2 Negatives values
- There are `2515` zero values which is (0.5% of whole data)

Now lets see the value_counts

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_8.jpg?raw=true)



`Column - CustomerID`

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_11.jpg?raw=true)

- There is Missing values (24.9% of whole data)


`Column - Country`

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_12.jpg?raw=true)


- Frequency of UK is very dominant (91.4% of whole data)

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_13.jpg?raw=true)



![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_14.jpg?raw=true)


[Approach](https://linktodocumentation)

### Feature Engineering

- Keeping only `United_Kindom` records in the data other countries are removed
- Removed Negative records from `Quantity` and `UnitPrice` columns. since these cannot be Negative
- Created a new column called `TotalPrice` by taking the product between `Quantity` and `UnitPrice` 

- Now the new dataframe will be looking like this

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_16.jpg?raw=true)



- Let's understand how RMF table is getting created. Since in the case given data,
  the data provided was till `2011-12-09`. 

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_15.jpg?raw=true)


- So I'm setting the `current_date` as `2011-12-10`. 
  current_date is calculated to know the number of days from recent purchase of each customer (`Recency`)
- To find the RMF I'm first grouping the dataframe based on `CustomerID`. 
- Then `Recency` is calculated by applying `current_date - recent_invoice_date` per customer_group
- Then `Frequency` is calculated based on `sum of number of invoices` per customer group
- Then `Monetary` is calucualted based on `sum of TotalPrice` per customer group

- Let's see the created RMF Table

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_17.jpg?raw=true)

- Renaming `InvoiceDate to Recency`,`InvoiceNo to Frequency`, `TotalPrice to Monetary`

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_18.jpg?raw=true)

- Let's see the distribution of `Recency`,  `Frequency`, ` Monetary`

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_19.jpg?raw=true)

- We can notice there is skewness and outliers in RMF data, lets visualize outliers

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_20.jpg?raw=true)


#### Let's handle the skewness and outliers by applying various transformations and imputation methods

- Let's see how dropping outliers affects the distribution and applying various transformations when considering `5 percentile` and `95 percentile`

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_21.jpg?raw=true)

- We can see 29% of data is getting lost, which is not good

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_22.jpg?raw=true)


- Let's see how dropping outliers affects the distribution and applying various transformations when considering `1 percentile` and `99 percentile`

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_23.jpg?raw=true)

- Let's see how capping outliers affects the distribution and applying various transformations by finding `minimum` and `maximum` value using `Inter Quartile Range (IQR)`
  and imputing outliers with minimum and maximum values

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_24.jpg?raw=true)

- But capping the outliers increases the frequency at the postive tail end of distribution.

- Let's see how KNNImputer works on outliers & see how it affects the distribution and also applying various transformations.

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_25.jpg?raw=true)


- Finalizing KNNImputer for outlier removal and Yeo_Johnson transformation for skewness handling and standardizing data.
  
  Lets see final data sample:

  ![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_26.jpg?raw=true)




### Modeling

- I'm using KMeans algorithm for segmentation.
- To find the optimal number of cluster we have two methods

- `Method-1` is  plotting `elbow_plot`, with `wcss` and `number of clusters` in X and Y axis

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_27.jpg?raw=true)

- `Method-2` is using `KneeLocator` class from `kneed library`. we have used the KneeLocator Method.
   The optimal number of cluster is `k = 4`

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_28.jpg?raw=true)

- I build final KMean model with `n_clusters=4,  
  and combining the cluster predictions with the dataset. 
  So here the final data will look like:

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_29.jpg?raw=true)

- Let's visualize the clusters predicted by KMeans

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_30.jpg?raw=true)

- We can clearly see that clusters `PURPLE` is good set of customers
- Cluster `YELLOW` seems like about to churn customers
- Cluster `LIGHT_ORANGE` maybe a churned or about to churn customers since Recency is high(i.e. no recent purchase) Frequency is less, Monetary is also average
- Clsuter `BLUE` would be possibly new set of customers since Recency is low (i.e. they made recent purchases), Frequency and Monetary is low, may be because they just started using the company services

### Deployment

- Created a new dataset by combining CustomerID column and mapping the cluster with a meaningful names.
  the data sample is below:

![alt text](https://github.com/sudheeshe/RFM_Customer_Segmentation/blob/main/Images_for_readme/df_overview_31.jpg?raw=true)

- I've used 4 segments names as below:

> * LOYAL CUSTOMERS
> * ABOUT TO CHURN
> * CHURNED CUSTOMER
> * NEW CUSTOMER

- By the UI provided the user can input CustomerID and check which segment the customer belongs to

##### 🔗 Find the deployment link on Heroku

[click here](https://rfm-customer-segmentation.herokuapp.com/)


