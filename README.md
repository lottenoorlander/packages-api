# packages-api

Package Search Service­
Description

On the Linux distributions derived from Debian, users are able to search for available packages using the apt search command. This searches through the local package database to find packages matching the user’s search query. This path to this database is typically /var/lib/dpkg/available but for this assignment an example file has been provided.

Your task is to build a REST API that will allow users to search for a package given a search query. The package information returned should include the following details:
    • Package name
    • Version
    • Description
    • SHA256 hash
    • Dependencies, Recommends, Conflicts. 
        ◦ May have specific versions denoted by the syntax (>= 5.2). 
        ◦ May be fulfilled by multiple packages denoted by the | symbol. 

The format for the returned data should be in JSON.

Acceptance Criteria
    • A HTTP REST service that exposes a /search endpoint, allowing us to query for packages.
    • We should be able to run this service easily. 
        ◦ Use of a database or some other 3rd party tools is fine, but do make it easy for us to set it up.
    • The service should be in Python or NodeJS.
    • The service should be as production ready as possible.


Please do not spend more than a few hours on this assignment. The reality of deadlines means that at times we may not be able to implement everything and what we chose to leave out is just as interesting as what we choose to implement.

Good luck!


