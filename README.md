# mobile-travel-demo
Couchbase Solution Engineer Mobile Travel Demo repository

This repository provides the following items:
1. Couchbase Server
2. Couchbase Sync Gateway
3. Couchbase Web-App Front-end
4. Sync Gateway User creation script
5. Full-text index used for travel sample front-end 

This simplifies the building of a mobile demo by the SE for a customer.
If you need to build it this Dockerfile consolidates CBSG and CBEE instances to a single container and simplifies clean-up required.

The current version of this container already built can be found here: 
`https://hub.docker.com/repository/docker/agonyou/couchbase-travel-demo/`

and can be downloaded via the command:
`docker pull agonyou/couchbase-travel-demo`

The original web front-end application which has its own python requirements can be found here:
`git clone -b 5.0 https://github.com/couchbaselabs/try-cb-python.git `

Finally, the mobile application can be found here: 
`git clone -b master --depth 1 https://github.com/couchbaselabs/mobile-travel-sample.git `
