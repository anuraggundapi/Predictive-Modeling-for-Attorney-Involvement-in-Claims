# Predictive-Modeling-for-Attorney-Involvement-in-Claims

➢ Business Objective:
The goal of this project is to develop a model that predicts whether an attorney will be involved in a claim based on various claim-related factors. This will help insurance companies optimize their processes, reduce legal costs, and better allocate resources.

Dataset Details

The dataset contains 1,340 rows and 13 columns:

1. CASENUM - Numerical (Integer): Unique case identifier.
2. ATTORNEY - Binary (0 or 1): Indicates if an attorney was involved (1 = Yes, 0 = No).
3. CLMSEX - Categorical (0 or 1): Gender of the claimant (1 = Male, 0 = Female).
4. CLMINSUR - Binary (0 or 1): Whether the claimant was insured (1 = Yes, 0 = No).
5. SEATBELT - Binary (0 or 1): Seatbelt usage (1 = Yes, 0 = No).
6. CLMAGE - Numerical (Integer): Age of the claimant.
7. LOSS - Numerical (Float): Financial loss associated with the claim.
8. Accident_Severity - Categorical (Minor, Moderate, Severe): Level of severity.
9. Claim_Amount_Requested - Numerical (Float): Initial claim amount requested.
10. Claim_Approval_Status - Binary (0 or 1): Whether the claim was approved (1 = Yes, 0 = No).
11. Settlement_Amount - Numerical (Float): Final settlement amount paid.
12. Policy_Type - Categorical (Comprehensive, Third-Party): Type of insurance policy.¶
13. Driving_Record - Categorical (Clean, Minor Offenses, Major Offenses): Claimant's driving history.

In this project, "Attorney" refers to a lawyer who gets involved in an insurance claim on behalf of the claimant (the person filing the claim).
What It Represents in Your Dataset?
•	The target variable in your dataset is ATTORNEY, which is binary: 
o	1 → An attorney was involved in the claim.
o	0 → No attorney was involved.
Why Is This Important?
•	Attorney involvement can increase costs for insurance companies due to legal fees, negotiations, and prolonged claim settlements.
•	Predicting attorney involvement helps insurers proactively manage claims, reduce legal expenses, and allocate resources efficiently.
•	Early identification of claims likely to involve attorneys allows insurers to handle them strategically (e.g., better settlement offers, fraud detection, etc.).
The model is designed to predict whether an attorney will be involved in a claim based on claim details like accident severity, policy type, financial loss, and claimant demographics.

➢ MODEL BUILDING:

Model building in Python refers to the process of creating a predictive or analytical model using statistical or machine learning techniques.

It typically involves several steps:

✅ Data Collection: Load data from sources like CSV files, databases, or APIs.
✅ Data Preprocessing: Handle missing values, encode categorical variables, and normalize data.
✅ Exploratory Data Analysis (EDA): Analyze distributions, relationships, and correlations
✅ Feature Engineering: Create new features, select important ones, and transform data.
✅ Splitting Data: Divide data into training and testing sets (e.g., using train_test_split from sklearn).
✅ Model Selection: Choose a model based on the problem (e.g., Linear Regression for regression, Decision Tree for classification).
✅ Model Training: Fit the model to the training data.
✅ Model Evaluation: Assess model performance using metrics like accuracy, RMSE, R², or F1-score
✅ Hyper parameter Tuning: Optimize model parameters for better performance.
✅ Model Deployment: Deploy the model for real-world use.

➢ Model Selection:
Model is selected based on the accuracy’s that we are gained with respective models and all ML Supervised Classification model are trained, tested and finally evaluated based on this evaluation final model is selected. 

➢ Model Accuracy’s:
➔ Random Forest: 57%
➔ Logistic Regression: 54%
➔ Support Vector Machine (SVM): 49%
➔ Decision Tree: 56%
➔ KNN: 52%
➔ Naive Bayes: 50%
➔ Gradient Boosting: 53%
➔ Neural Networks : 51%

 ☑️ Selecting a Suitable Model: We all found that Random Forest which is an Ensemble model doing well in both Testing and Training as well as in prediction.

 ☑️ Deployment of Model:

✔ Build ML model is converted into Pickle file and then Model is Deployed through stream lit Application for client easiness.
✔ The Input need to be given in and Output displays on screen either Attorney is involved or not. 
✔ insure.py is the deployment file and Here are the Reference Interfaces of model which are deployed.
✔ On shows Attorney involved and other show No attorney is involved.













