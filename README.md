# ISELab Debugger

This project is something I am doing as an independent study project under 
Dr. Julie Rursch in the fall of 2020 at Iowa State University. 

In general, this is intended to be a tool for people new to network management
or the more complex ISELAB environment to understand what is happening on their
networks. It is deisgned to work in an ISELab, a product of the [ISEAGE research 
lab](https://iseage.org), who I worked for from my junior through super-senior years
at Iowa State.


# Running
There are two supported ways to run the application. The first is natively on your
machine. To do this, see [INSTALL.md](INSTALL.md). The second is using Docker. 
Assuming you have Docker installed, you can use the following command to run the 
application on port 8000 (change the first of the `8000`'s to change the local port).

    docker run -p 8000:8000 thetoddluci0/iselab_debugger


### A Note to Educators on Deployment
When deploying this to a large number of students using the Docker method, it is
preferred that you pull the container once on a template VM, and deploy copies of that.
This is because Docker limits anonymous user pulls of a container to 100 per six hours.
Because an ISELab has one public facing IP address, this causes Docker to count 
__all pulls__ in the environment against that, which may result in rate limiting. 
For more information, see 
["What are the rate limits for pulling Docker images from the Docker Hub Registry?"](https://www.docker.com/pricing/resource-consumption-updates)
in the Docker documentation. 


# Platform Specific Service Checks

### LDAP
`python-ldap` does not support Windows at this time (or likely ever), so LDAP checks are on a
separate branch to maintain cross-platform support. You can checkout the branch 
[ldap_support](https://github.com/TheToddLuci0/ISELab_Debugger/tree/ldap_support) if you want
this. Note that it is ___LINUX ONLY___. There also exists a 
[docker image](https://hub.docker.com/repository/docker/thetoddluci0/iselab_debugger/tags?page=1).