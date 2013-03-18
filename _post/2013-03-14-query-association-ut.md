# Querying Association is not implemented in Grails Unit Test

## Querying Association is not supported in Grails Unit Test

From the Grails official documentation, we can get:

```
The following features of GORM for Hibernate can only be tested within an integration test:

* String-based HQL queries
* composite identifiers
* dirty checking methods
* any direct interaction with Hibernate
```

Today, I found that Querying Association is not supported as well. No error reported but it doesn't work as expected.
An alternative way is to use "in" in the Criteria.
