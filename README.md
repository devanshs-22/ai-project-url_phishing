# ai-project-url_phishing
```

Latest Update on the Dataset
1. Changes in Dataset Handling
-We have updated our dataset by removing unnecessary features and focusing on relevant ones.

-We are now selecting 5,000 legitimate websites and 5,000 phishing websites.

-For each website, we extract 16 key features based on three main categories.

-The collected 10,000 websites are shuffled and stored in a dataset named final.csv.

2. Feature Categories & Sub-Features
(A) Address-Based Features (9 Features)
-Domain of URL

-Presence of IP Address

-Presence of '@' Symbol

-URL Length

-URL Depth

-Redirection using '//'

-Presence of 'http/https'

-Use of URL Shortening Services

-Presence of Prefix-Suffix in Domain

(B) Domain-Based Features (3 Features)
Availability of DNS Record

-Age of the Domain

-Domain Expiry Period

(C) HTML & JavaScript-Based Features (3 Features)
Presence of Iframe Redirection

-Disabling of Right-Click Functionality

-Website Forwarding

-This structured dataset will improve the efficiency and accuracy of our phishing detection model.
