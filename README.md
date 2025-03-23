# ai-project-url_phishing
```

So, some infromation about how we are now handling the features and extracting them
like now ,
i am picking 5000 random legit websites and 5000 phishing webistes and extracting 16 featrues for each of them, then contacting them
10,000 websites and shuffeling them into dataset named final.csv




Latest Update on the dataset 
We have decided to change the older dataset and reduce the unnecesary features from the dataset 
now our dataset contains features based on basically three things 
1. Address Type
2. Domain Based
3. Html and java script based

So, like for Address based features we have 9 sub features -
1.Domain of Url
2.IP Address
3.@ symbol
4.Length of Url
5.Depth of url
6.Redirection '//'
7.'http/https' present
8.Url shortening service
9.prefix - suffix used 


Now for the Domain based features
1.DNS record
2.Age of Domain
4.End period of Domain

HTML based features

1.Iframe Redirection
2.Disabling Right click
3.Website Fordwarding 


About the Dataset
The dataset is named dataset_phishing.csv.

It contains approximately 11,000 instances, consisting of 50% phishing websites and 50% legitimate websites.

It includes 89 features, out of which:

56 are extracted from the structure and syntax of URLs.
24 are extracted from the content of their corresponding pages.
7 are extracted by querying external services.
Some of the features include:

length_url
length_hostname
ip
nb_comma
nb_dslash
port
prefix_suffix
etc.


ALTERNATIVE DATASET 

Larger Dataset: dataset_full.csv
It contains:

Total number of instances: 88,647
Legitimate website instances (labeled as 0): 58,000 (65%)
Phishing website instances (labeled as 1): 30,647 (35%)
Total number of features: 111 (excluding the target variable).
Features (Brief Overview)
URL-Based Features:

qty_dot_url → Count of . in the URL
qty_hyphen_url → Count of - in the URL
qty_underline_url → Count of _ in the URL
qty_slash_url → Count of / in the URL
qty_questionmark_url → Count of ? in the URL
qty_equal_url → Count of = in the URL
qty_at_url → Count of @ in the URL
qty_and_url → Count of & in the URL
qty_exclamation_url → Count of ! in the URL
qty_space_url → Count of (space) in the URL
qty_tilde_url → Count of ~ in the URL
qty_comma_url → Count of , in the URL
qty_plus_url → Count of + in the URL
qty_asterisk_url → Count of * in the URL
qty_hashtag_url → Count of # in the URL
qty_dollar_url → Count of $ in the URL
qty_percent_url → Count of % in the URL
qty_tld_url → Top-level domain length
length_url → URL length
Domain-Based Features:

qty_dot_domain → Count of . in the domain
qty_hyphen_domain → Count of - in the domain
qty_underline_domain → Count of _ in the domain
qty_slash_domain → Count of / in the domain
qty_questionmark_domain → Count of ? in the domain
qty_equal_domain → Count of = in the domain
qty_at_domain → Count of @ in the domain
qty_and_domain → Count of & in the domain
qty_exclamation_domain → Count of ! in the domain
qty_space_domain → Count of (space) in the domain
qty_tilde_domain → Count of ~ in the domain
qty_comma_domain → Count of , in the domain
qty_plus_domain → Count of + in the domain
qty_asterisk_domain → Count of * in the domain
qty_hashtag_domain → Count of # in the domain
qty_dollar_domain → Count of $ in the domain
qty_percent_domain → Count of % in the domain
qty_vowels_domain → Count of vowels in the domain
domain_length → Domain length
domain_in_ip → Whether the domain is in an IP address format
server_client_domain → Whether the domain contains the keywords "server" or "client"
Directory-Based Features:

qty_dot_directory → Count of . in the directory
qty_hyphen_directory → Count of - in the directory
qty_underline_directory → Count of _ in the directory
qty_slash_directory → Count of / in the directory
qty_questionmark_directory → Count of ? in the directory
qty_equal_directory → Count of = in the directory
qty_at_directory → Count of @ in the directory
qty_and_directory → Count of & in the directory
qty_exclamation_directory → Count of ! in the directory
qty_space_directory → Count of (space) in the directory
qty_tilde_directory → Count of ~ in the directory
qty_comma_directory → Count of , in the directory
qty_plus_directory → Count of + in the directory
qty_asterisk_directory → Count of * in the directory
qty_hashtag_directory → Count of # in the directory
qty_dollar_directory → Count of $ in the directory
qty_percent_directory → Count of % in the directory
directory_length → Directory length
File-Based Features:

qty_dot_file → Count of . in the file
qty_hyphen_file → Count of - in the file
qty_underline_file → Count of _ in the file
qty_slash_file → Count of / in the file
qty_questionmark_file → Count of ? in the file
qty_equal_file → Count of = in the file
qty_at_file → Count of @ in the file
qty_and_file → Count of & in the file
qty_exclamation_file → Count of ! in the file
qty_space_file → Count of (space) in the file
qty_tilde_file → Count of ~ in the file
qty_comma_file → Count of , in the file
qty_plus_file → Count of + in the file
qty_asterisk_file → Count of * in the file
qty_hashtag_file → Count of # in the file
qty_dollar_file → Count of $ in the file
qty_percent_file → Count of % in the file
file_length → File length
Parameter-Based Features:

qty_dot_params → Count of . in parameters
qty_hyphen_params → Count of - in parameters
qty_underline_params → Count of _ in parameters
qty_slash_params → Count of / in parameters
qty_questionmark_params → Count of ? in parameters
qty_equal_params → Count of = in parameters
qty_at_params → Count of @ in parameters
qty_and_params → Count of & in parameters
qty_exclamation_params → Count of ! in parameters
qty_space_params → Count of (space) in parameters
qty_tilde_params → Count of ~ in parameters
qty_comma_params → Count of , in parameters
qty_plus_params → Count of + in parameters
qty_asterisk_params → Count of * in parameters
qty_hashtag_params → Count of # in parameters
qty_dollar_params → Count of $ in parameters
qty_percent_params → Count of % in parameters
params_length → Parameters length
tld_present_params → Presence of TLD in arguments
qty_params → Number of parameters
Miscellaneous Features:


