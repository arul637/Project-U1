# Phishing URL Manager SQL

this MySQL command is used to create phishing url Detection SQL manager

```
create table phishingDetectionSQL(url varchar(1000));

Ex:-

INSERT into phishingDetectionSQL VALUES("https://srmvalliammai.ac.in");
```

# register SQL

this is registering the user detials 

```
create table register(firstname varchar(1000), lastname varchar(1000), email varchar(1000), password varchar(1000));
```

# Password Manager SQL

this password manager is used to manage the password and user credentials in securely.

```
CREATE table passwordManagerSQL(website varchar(1000), username varchar(1000), password varchar(1000), description varchar(1000));

Ex:-
 INSERT INTO passwordManagerSQL VALUES("https://google.com", "sarulkumaran.21042004@gmail.com", "Ak@21042004", "this is sample description");
```

# Domain Blocking SQL

this is used to block the domains, as per user needs

```
CREATE TABLE domainBlockingSQL(domain varchar(1000));

Ex:-
INSERT into domainBlockingSQL VALUES("srmvalliammai.ac.in");
```

