LDAP
^^^^
Uses ldapsearch to login to ldap server. Once authenticated, it performs a lookup of all users in the same domain

Uses Accounts

Custom Properties:
  - domain: The domain of the username
  - base_dn: The base dn value of the domain (Ex: dc=example,dc=com)
