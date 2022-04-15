# Setup

1. Install Vagrant
   `https://www.vagrantup.com/docs/installation`
2. Install VirtualBox
   `https://www.virtualbox.org/wiki/Downloads`
3. Start Vagrant environment and provision VM's
   `vagrant up`
4. SSH into control node
   `vagrant ssh control` //Default password = vagrant
5. Copy host file into control station hostfile
   `sudo cp /vagrant/hosts /etc/hosts`
6. Generate keypair to make hosts ssh accessible
   `ssh-keygen`
7. Copy SSH keys to servers
   `ssh-copy-id node1 && ssh-copy-id node2`
8. Test SSH access
   `vagrant ssh@node1`
9. To stop and delete everything
   `vagrant destroy -f`
10. SUCCESS!
