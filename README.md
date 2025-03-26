# ai-project-url_phishing
```

Latest Update on the Dataset
We have decided to update our dataset by removing unnecessary features and focusing on three main categories:

Address-Based Features (9 sub-features)

Domain of URL

Presence of IP Address

Presence of '@' Symbol

URL Length

URL Depth

Redirection using '//'

Presence of 'http/https'

Use of URL Shortening Services

Presence of Prefix-Suffix in Domain

Domain-Based Features (3 sub-features)

Availability of DNS Record

Age of the Domain

Domain Expiry Period

HTML & JavaScript-Based Features (3 sub-features)

Presence of Iframe Redirection

Disabling of Right-Click Functionality

Website Forwarding

Current Handling of Features & Dataset
We are randomly selecting 5,000 legitimate websites and 5,000 phishing websites.

For each website, we extract 16 key features based on the categories mentioned above.

The collected 10,000 websites are shuffled and stored in a dataset named final.csv.

This structured approach ensures that our dataset remains relevant, efficient, and optimized for phishing detection.

