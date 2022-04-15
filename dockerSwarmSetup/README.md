# Setup

Here Docker Swarm is used for container orchestration on all hosts.

1. SSH into control node
   `vagrant ssh control`
2. Install docker
   `sudo apt-get install docker.io`
3. Make it the manager node
   `sudo docker swarm init --advertise-addr 172.16.1.50`
4. A docker swarm join command containing a token and IP address of manager is printed on the screen
5. Copy this command, SSH into node1, node2 and paste
6. This will add node1 and node2 as worker nodes
7. In the manager node, list all available nodes
   `sudo docker node ls`
8. Create a Nginx service with three replicas
   `sudo docker service create --name nginx --replicas=3 nginx:alpine`
9. View all services
   `sudo docker service ls`
10. List the tasks of the service
    `sudo docker service ps <service id>` //copy service id from prev step
11. Finally remove the service `docker service rm nginx`
12. SUCCESS!

## To clean up all VMs, `vagrant destroy -f`
