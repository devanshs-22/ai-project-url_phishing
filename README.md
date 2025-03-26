# ai-project-url_phishing
This project aims to develop an AI-based model for detecting phishing websites using machine learning techniques.
```
Latest Updates on the Dataset
1. Improvements in Dataset Handling
>The dataset has been optimized by removing unnecessary features and focusing only on relevant ones.
>It now consists of 5,000 legitimate websites and 5,000 phishing websites to ensure a balanced dataset.
>Each website is analyzed based on 16 key features categorized into three main groups.
>The final dataset, named final.csv, contains 10,000 shuffled entries for improved training efficiency.

2. Feature Categories & Sub-Features
(A) Address-Based Features (9 Features)
>Domain of URL
>Presence of IP Address
>Presence of ‘@’ Symbol
>URL Length
>URL Depth
>Redirection using ‘//’
>Presence of ‘http/https’
>Use of URL Shortening Services
>Presence of Prefix-Suffix in Domain

(B) Domain-Based Features (3 Features)
>Availability of DNS Record
>Domain Age (How old the domain is)
>Domain Expiry Period (Remaining validity)

(C) HTML & JavaScript-Based Features (3 Features)
>Presence of Iframe Redirection
>Right-Click Disabling
>Website Forwarding
>This structured dataset enhances the efficiency and accuracy of the phishing detection model.

3. Model Training and Evaluation
>Random Forest Classifier
>Decision tree
>XGBoost Classifier
>XGBoost achieved the highest accuracy of 85%

Further Feature engineering is in process to enhance the accuracy.
