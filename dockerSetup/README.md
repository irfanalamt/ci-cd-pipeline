# Setup

Here Docker is used to containerize our Flask web application.

1. SSH into a node
   `vagrant ssh node1`
2. Check if docker is working
   `docker run hello-world`
3. Navigate to the dockerSetup folder in the node
   `cd /vagrant/dockerSetup`
4. Start and run our web app defined in docker-compose.yml
   `docker-compose up`
5. To test, open another terminal ssh into the control node
   `vagrant ssh control`
6. If mistake is made in one of the files, you will have to re-do the image build with `docker-compose build`
7. Test the app running on node1 port 5000
   `curl node1:5000`
8. SUCCESS!
